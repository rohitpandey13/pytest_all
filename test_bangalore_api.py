from app import get_weather
import pytest
from unittest.mock import patch
def test_get_weather():
     with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"title":"Python 101",
                                                    "author": "Guido"}

        result = get_weather("Bangalore")

        assert result["title"] == "Python 101"
        assert result["author"] == "Guido"
        mock_get.assert_called_once()