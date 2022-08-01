from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {} but expected not to".format(item.name))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 "The item with name {} does not exist but expected to exist".format(item.name))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              "The item with name {} exists but it should not".format(item.name))
