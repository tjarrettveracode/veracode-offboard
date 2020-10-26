# Veracode Offboard

Uses the Veracode Identity API to deactivate a list of users.

## Setup

Clone this repository:

    git clone https://github.com/tjarrettveracode/veracode-offboard

Install dependencies:

    cd veracode-offboard
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## Run

If you have saved credentials as above you can run:

    python vcoffboard.py (arguments)

Otherwise you will need to set environment variables:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python vcoffboard.py (arguments)

Arguments supported include:

* --usernames, -u : list of user names to deactivate, separated by spaces

## NOTES

1. The script only deactivates users (by setting the `Active` flag to `False`). It does not delete them.
