import unittest
import commands


class CommandsTestCase(unittest.TestCase):

    # Test unitest working
    def test_01_working(self):
        pass

    # Unitest to test create table
    def test_02_createBookmarksTableCommand(self):

        # Arrange
        expect_value = 'Bookmark_Table_Created!'

        # Actual
        actual_value = commands.CreateBookmarksTableCommand.execute(self)

        # assert
        self.assertEqual(expect_value, actual_value)

    # Test Add Bookmark function
    def test_03_add_bookmark_command(self):
        """ Removing testing data, If previously added while running test data
            Search Python to remove before adding testing data 
        """
        # arrange
        self.order_by = "date_added"
        bookMarksList = commands.ListBookmarksCommand.execute(self)
        clear_test_list = []
        for i in bookMarksList:
            if i[1] == 'Python':
                clear_test_list.append(i[0])
        print(clear_test_list)

        for j in clear_test_list:
            print(j)
            commands.DeleteBookmarkCommand.execute(self, j)

        bookMarkTestData = {
            'title': 'Python', 'url': 'https://www.w3schools.com/python/python_dictionaries.asp', 'notes': 'Dictionaries'}
        expect_value = 'Bookmark added!'

        # act
        actual_value = commands.AddBookmarkCommand.execute(
            self, bookMarkTestData)
        # assert
        self.assertEqual(expect_value, actual_value)

    # Test List BookMarks function by date
    def test_04_list_bookmarks_command(self):
        # arrange
        expect_value = 'Python'
        self.order_by = "date_added"

        # act
        bookMarksList = commands.ListBookmarksCommand.execute(self)
        actual_value = ''
        for i in bookMarksList:
            if i[1] == 'Python':
                actual_value = i[1]
        print(actual_value)

        # assert
        self.assertEqual(expect_value, actual_value)

    # Test List BookMarks function by title
    def test_05_list_bookmarks_command(self):
        # arrange
        expect_value = 'Python'
        self.order_by = "title"

        # act
        bookMarksList = commands.ListBookmarksCommand.execute(self)
        actual_value = ''
        for i in bookMarksList:
            if i[1] == 'Python':
                actual_value = i[1]
        print(actual_value)

        # assert
        self.assertEqual(expect_value, actual_value)

    # Test delete bookmark function
    def test_06_delete_bookmark_command(self):

        # arrange
        expect_value = 'Bookmark deleted!'
        self.order_by = "date_added"

        # act
        bookMarksList = commands.ListBookmarksCommand.execute(self)
        clear_test_list = []
        for i in bookMarksList:
            if i[1] == 'Python':
                clear_test_list.append(i[0])
        print(clear_test_list)

        for j in clear_test_list:
            print(j)
            actual_value = commands.DeleteBookmarkCommand.execute(self, j)

        # assert
        self.assertEqual(expect_value, actual_value)

    # Test import github stars function
    def test_07_import_github_stars_command(self):
        # arrange
        expect_value = 'Imported 0 bookmarks from starred repos!'
        data = {'github_username': 'bilkiskhan'}

        # act

        actual_value = commands.ImportGitHubStarsCommand.execute(self, data)

        # assert
        self.assertEqual(expect_value, actual_value)
