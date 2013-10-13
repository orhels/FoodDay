# coding=UTF-8
import os
import sys

from fabric.operations import local

LOCAL_SETTINGS = "FoodDay.Settings.local_settings"

_old_environment_value = ""


def deploy_to_test():
    print "Deploying to test"
    print ""
    try:
        _set_environment_variables()
        _print_debug_info()
        _run_tests()
        _commit_to_test_branch()
        _push_to_remote()
        _update_on_server()
        _restart_server()
    finally:
        _reset_environment_variables()


def _commit_to_test_branch():
    local('git checkout test')
    local('git commit -a')

def _set_environment_variables():
    _old_environment_value = os.getenv('DJANGO_SETTINGS_MODULE', "")
    os.putenv('DJANGO_SETTINGS_MODULE', LOCAL_SETTINGS)


def _reset_environment_variables():
    if _old_environment_value == "":
        os.unsetenv('DJANGO_SETTINGS_MODULE')
    else:
        os.putenv('DJANGO_SETTINGS_MODULE', _old_environment_value)


def _restart_server():
    print "TODO: sudo initctl restart foodaytest_gunicorn"


def _push_to_remote():
    local('git push origin test')

def _update_on_server():
    print "TODO: 'git pull origin test' as foodaytest@fooday.no"


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