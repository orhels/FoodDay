# coding=UTF-8
import sys

from fabric.context_managers import cd, shell_env, settings
from fabric.operations import local, run

LOCAL_SETTINGS = "FoodDay.Settings.local_settings"


def deploy_to_test(run_tests="yes", debug="no"):
    print "Deploying to test"
    print ""
    with shell_env(DJANGO_SETTINGS_MODULE=LOCAL_SETTINGS):
        if debug != "no":
            _print_debug_info()
        if run_tests == "yes":
            _run_tests()
        _push_to_test()
        _restart_server()


def _push_to_test():
    _add_test_as_remote()
    print "Pushing HEAD to test servers master branch"
    local('git push test master')


def _add_test_as_remote():
    if not "test	foodaytest@fooday.no:repo/foodaytest.git" in local('git remote -v', capture=True):
        local('git remote add test foodaytest@fooday.no:repo/foodaytest.git')


def _restart_server():
    print ""
    print "Restarting server"
    code_dir = '/home/foodaytest/app/FoodDay'
    with settings(host_string='foodaytest@fooday.no'), cd(code_dir):
        if not "test	foodaytest@fooday.no:repo/foodaytest.git" in run('git remote -v'):
            run('git remote add test foodaytest@fooday.no:repo/foodaytest.git')
        run('git clean -f -d')
        run('git pull --strategy=recursive --strategy-option=theirs test master')
        print "TODO: syncdb"
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