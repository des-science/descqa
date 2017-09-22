import os
from ValidationTest import BaseValidationTest, TestResult

__all__ = ['ListAvailableQuantities']

class ListAvailableQuantities(BaseValidationTest):
    """
    validation test to list all available quantities
    """
    @staticmethod
    def _save_quantities(catalog_name, quantities, filename):
        quantities = list(quantities)
        quantities.sort()
        with open(filename, 'w') as f:
            f.write('# ' + catalog_name + '\n')
            for q in quantities:
                f.write(str(q))
                f.write('\n')

    def run_validation_test(self, galaxy_catalog, catalog_name, base_output_dir):
        self._save_quantities(catalog_name, galaxy_catalog.list_all_quantities(), os.path.join(base_output_dir, 'quantities.txt'))
        self._save_quantities(catalog_name, galaxy_catalog.list_all_native_quantities(), os.path.join(base_output_dir, 'native_quantities.txt'))
        return TestResult(0, passed=True)
