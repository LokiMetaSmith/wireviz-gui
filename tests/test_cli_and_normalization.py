import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path
from click.testing import CliRunner
import yaml

from wireviz_gui.__main__ import main
from wireviz_gui.app import normalize_connections, preprocess_yaml_data


class TestCliAndNormalization(unittest.TestCase):
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("--graphviz-path", result.output)
        self.assertIn("--loglevel", result.output)

    @patch("wireviz_gui.__main__.Application")
    def test_cli_file_and_graphviz_path(self, mock_app):
        runner = CliRunner()
        with runner.isolated_filesystem():
            # Create a dummy yaml file
            test_file = Path("test.yaml")
            test_file.write_text("connectors: {}", encoding="utf-8")

            result = runner.invoke(
                main,
                [str(test_file), "--graphviz-path", "/usr/bin", "--loglevel", "DEBUG"],
            )
            self.assertEqual(result.exit_code, 0)
            mock_app.assert_called_once()
            args, kwargs = mock_app.call_args
            self.assertEqual(kwargs.get("initial_file"), str(test_file))
            self.assertEqual(kwargs.get("loglevel"), 10)  # logging.DEBUG is 10

    def test_preprocess_yaml_multi_key_and_none(self):
        # Test handling multi-key connections dict
        data = {
            "connectors": {
                "J1": {"pincount": 2},
                "J2": {"pincount": 2},
            },
            "cables": {
                "W1": {"label": "Main Cable", "notes": "Existing note"},
                "W2": {"label": "Second Cable"},
            },
            "connections": [
                {
                    "J1.1": "J2.1",
                    "J1.2": "J2.2",
                }
            ],
        }

        normalized = normalize_connections(data)

        # Label moved to notes
        self.assertNotIn("label", normalized["cables"]["W1"])
        self.assertEqual(normalized["cables"]["W1"]["notes"], "Existing note\nMain Cable")
        self.assertEqual(normalized["cables"]["W2"]["notes"], "Second Cable")

        # Check connections contains both connections flattened/parsed
        connections = normalized["connections"]
        self.assertEqual(len(connections), 2)
        self.assertEqual(connections[0], [{"J1": 1}, {"J2": 1}])
        self.assertEqual(connections[1], [{"J1": 2}, {"J2": 2}])

    def test_preprocess_yaml_edge_cases(self):
        # Test None inputs and missing sections
        self.assertIsNone(normalize_connections(None))
        self.assertEqual(normalize_connections("not a dict"), "not a dict")

        empty_data = {"connections": None}
        self.assertEqual(normalize_connections(empty_data), {"connections": None})

        # Test star-topology list of dicts with multi-key dict items
        data = {
            "connectors": {"X1": {}, "X2": {}},
            "connections": [
                {
                    "X1.1": [
                        {"X2.1": "W1:1"}
                    ]
                }
            ]
        }
        res = normalize_connections(data)
        self.assertEqual(len(res["connections"]), 1)
        self.assertEqual(res["connections"][0], [{"X1": 1}, "W1:1", {"X2": 1}])


if __name__ == "__main__":
    unittest.main()
