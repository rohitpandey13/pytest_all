
def pytest_addoption(parser):
    print("HOOK: addoption")
    parser.addoption("--env",action="store",default="dev",help="Environment :dev/stage/prod")


def pytest_configure(config):
    print("HOOK: configure")
    config.addinivalue_line("markers","fast:marks fast tests")
    config.addinivalue_line("markers","veryfast:marks very fast tests")
    # we defined markers without changing the ini file 
    
def pytest_sessionstart(session):
    print("HOOK: sessionstart")

def pytest_collection_finish(session):
    print("HOOK: collection_finish")

def pytest_sessionfinish(session, exitstatus):
    print("HOOK: sessionfinish")