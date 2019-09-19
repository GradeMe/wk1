import unittest
from base.docker.python_grading.suite import test_suite
from base.docker.python_grading.static_analysis import functionality_test


@test_suite('Basic testing')
class TestBasicFuncionality(unittest.TestCase):
    @functionality_test(
        0,
        desc='Tests `count_tweets`',
        hint='You can use `shape`, as in df.shape',
        hide_details=False,
        is_score_public=True)
    def test_count_tweets(self):
        print('IN TEST')
        
        
print('IMPORTED')
