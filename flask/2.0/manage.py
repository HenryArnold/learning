import os
from app import create_app, db
from app.models import

@manager.command
def test():
    """run the unit tests """
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
