from unittest.mock import Mock

fake = Mock()
fake.get_data.return_value={"status":200}

print(fake.get_data())