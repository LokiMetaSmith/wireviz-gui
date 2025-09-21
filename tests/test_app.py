import unittest
from wireviz_gui.app import _generate_homebox_csv_content

class TestApp(unittest.TestCase):
    def test_generate_homebox_csv_content(self):
        bom = [
            {
                'pn': 'IPN-001', 'mpn': 'MPN-001', 'manufacturer': 'Manu A',
                'description': 'Desc A', 'qty': 2, 'designators': ['C1', 'C2'],
                'supplier': 'Sup A', 'spn': 'SPN-A'
            },
            {
                'pn': 'IPN-002', 'mpn': 'MPN-002', 'manufacturer': 'Manu B',
                'description': 'Desc B', 'qty': 1, 'designators': ['R1'],
                'supplier': 'Sup B', 'spn': 'SPN-B'
            }
        ]

        csv_content = _generate_homebox_csv_content(bom)

        # Using \n for line endings to be more portable, csv module handles it.
        expected_content = (
            "name,label,description,location,quantity,price,asset_code,serial_number,notes\n"
            "MPN-001,Manu A,Desc A,,2,,IPN-001,,\"Designators: C1, C2, Supplier: Sup A, SPN: SPN-A\"\n"
            "MPN-002,Manu B,Desc B,,1,,IPN-002,,\"Designators: R1, Supplier: Sup B, SPN: SPN-B\"\n"
        )

        # The csv writer in python 3 on linux uses \r\n by default. Let's stick to that.
        expected_content = (
            "name,label,description,location,quantity,price,asset_code,serial_number,notes\r\n"
            "MPN-001,Manu A,Desc A,,2,,IPN-001,,\"Designators: C1, C2, Supplier: Sup A, SPN: SPN-A\"\r\n"
            "MPN-002,Manu B,Desc B,,1,,IPN-002,,\"Designators: R1, Supplier: Sup B, SPN: SPN-B\"\r\n"
        )

        self.assertEqual(csv_content, expected_content)

if __name__ == '__main__':
    unittest.main()
