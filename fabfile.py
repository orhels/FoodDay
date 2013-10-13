# coding=UTF-8
import sys

from fabric.context_managers import cd, shell_env
from fabric.contrib.console import confirm
from fabric.decorators import hosts
from fabric.operations import local, run

LOCAL_SETTINGS = "FoodDay.Settings.local_settings"

_old_environment_value = ""


def deploy_to_test():
    print "Deploying to test"
    print ""
    with shell_env(DJANGO_SETTINGS_MODULE=LOCAL_SETTINGS):
        _print_debug_info()
        _run_tests()
        _commit_to_test_branch()
        _push_to_remote()
        _update_on_server()
        _restart_server()


def _commit_to_test_branch():
    confirm("Your local changes will be commited to the test branch. Ok?")
    local('git checkout test')
    local('git commit -a')


def _restart_server():
    print "TODO: emit restart signal"


def _push_to_remote():
    local('git push origin test')


@hosts('foodaytest@fooday.no')
def _update_on_server():
    code_dir = '/home/foodaytest/app/FoodDay'
    with cd(code_dir):
        run('git pull origin test')


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