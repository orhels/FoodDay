# coding=UTF-8
import sys

from fabric.context_managers import cd, shell_env, settings, prefix
from fabric.operations import local, run

TEST_SETTINGS = "FoodDay.Settings.test_settings"
LOCAL_SETTINGS = "FoodDay.Settings.local_settings"


def deploy_to_test(run_tests="yes", debug="no"):
    print "Deploying to test"
    print ""
    with shell_env(DJANGO_SETTINGS_MODULE=LOCAL_SETTINGS):
        if debug != "no":
            _print_debug_info()
        if run_tests == "yes":
            _run_tests()
        print "TODO: compare output from pip freeze with the current requirements.txt"
        _push_to_test()
        _restart_server()


def _push_to_test():
    _add_test_as_remote()
    print "Pushing HEAD to test servers master branch"
    local('git config --local push.default current')
    local('git push test +HEAD:master ')


def _add_test_as_remote():
    if not "test	foodaytest@fooday.no:repo/foodaytest.git" in local('git remote -v', capture=True):
        local('git remote add test foodaytest@fooday.no:repo/foodaytest.git')


def _restart_server():
    print ""
    print "Restarting server"
    code_dir = '/home/foodaytest/app/FooDay'
    with settings(host_string='foodaytest@fooday.no'), cd(code_dir), shell_env(DJANGO_SETTINGS_MODULE=TEST_SETTINGS):
        # run('git reset --hard')
        run('git fetch')
        run('git checkout origin/master')
        with prefix('source env/bin/activate'):
            run('which python')
            run('pip install -r requirements.txt')
            run('python manage.py syncdb')
            run('python manage.py migrate')
            run('python manage.py collectstatic')
    print "TODO: emit restart signal"


def _virtualenv_has_been_activated():
    return hasattr(sys, 'real_prefix')


def _validate():
    if not _virtualenv_has_been_activated():
        print "Please activate your virtualenv before running this script"


def _print_debug_info():
    print "Debug info:"
    _print_python_path()
    print ""


def _print_python_path():
    print "Python version:"
    local('which python')


def _run_tests():
    print "Runnning tests:"
    local('python manage.py test')
    print ""
    print "TODO: run test coverage"