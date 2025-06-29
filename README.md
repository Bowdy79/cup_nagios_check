# NAGIOS Check for Cup

> Cup is the easiest way to check for container image updates.

For more info check: [https://github.com/sergi0g/cup](https://github.com/sergi0g/cup)

## What's 'cup_nagios_check'?
cup_nagios_check uses a Cup container for checking the local docker instance for updates.

It returns the result in the correct syntax for monitoring with Nagios (i. e. OpenITCockpit).

## How to use it
The following guide shows how to set up 'cup_nagios_check' with OpenITCockpit.

1. Connect to your docker host and check requirements
    - Python 3.12
    - Python Venv

2.  clone that repository

    `git clone <https://-repo-url->`

