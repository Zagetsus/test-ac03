import unittest
from unittest.mock import MagicMock, patch

from blog import Blog


class BlogTest(unittest.TestCase):
    @patch('blog.requests')
    def test_find_posts(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{}]
        mock_requests.get.return_value = mock_response

        self.assertEqual(Blog.posts(1),  [{}])

    @patch('blog.requests')
    def test_find_posts_fail(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = None

        mock_requests.get.return_value = mock_response

        self.assertIsNone(Blog.posts(1))

    @patch('blog.requests')
    def test_find_unique_post(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 67894,
            'userId': '14865',
            'status': True,
            'message': 'post about sea life'
        }
        mock_requests.get.return_value = mock_response

        self.assertEqual(Blog.post_by_user_id(1, '14865'),  {
            'id': 67894,
            'userId': '14865',
            'status': True,
            'message': 'post about sea life'
        })

    @patch('blog.requests')
    def test_find_unique_post_fail(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = None

        mock_requests.get.return_value = mock_response

        self.assertIsNone(Blog.post_by_user_id(1, '14865'))


if __name__ == '__main__':
    unittest.main()
