# NAGIOS Check for Cup

> Cup is the easiest way to check for container image updates.

For more info check: [https://github.com/sergi0g/cup](https://github.com/sergi0g/cup)

## What's 'cup_nagios_check'?
cup_nagios_check uses a Cup container for checking the local docker instance for updates.

It returns the result in the correct syntax for monitoring with Nagios (i. e. OpenITCockpit).

## How to use it
The following guide shows how to set up 'cup_nagios_check' with OpenITCockpit.

1. Connect via ssh to your docker host and check requirements
    - Python 3.12
    - Python Venv

2. Configure your ssh-key to connect from OpenITCockpit host to the docker host without password.

3. Clone that repository to your docker host

    ```
    git clone <https://-repo-url->
    ```

4. CD into the repo folder and create a new virtual environment and activate it

    ``` bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

5. Install all python requirements

    ``` bash
    pip install -r requirements.txt
    ```
6. Run the script an check the output

    ``` bash
    python3 main.py

    # Possible outputs:
    # OK - All containers up to date.
    # WARNING - Container image updates available!
    # UNKNOWN - Error while checking for updates!

7. Configure check in OpenITCockpit

    coming soon...
