# generate_tests.py
for i in range(1, 101):
    with open(f"test_{i}.py", "w+") as f:
        f.write(f'''import time
def test_case_{i}():
    time.sleep(0.11)
    assert {i} + {i} == {i*2}''')