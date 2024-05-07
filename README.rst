Ogone
=====

This is a plugin for `pretix`_. 

Accept payments through the Ogone interface (legacy interface of Nexi Payengine / Wordline)

Assumed Ogone settings
----------------------

- Configuration

  - Technical Information

    - Global transaction parameters

      - Processing for individual transactions: Always online (immediate)

    - Global security parameters

      - Hash algorithm: SHA-512

    - Data and origin verification

      - No "URL of the merchant page" set

      - No "IP address" set

      - SHA-IN passphrase set

    - Transaction feedback

      - "I would like to receive transaction feedback parameters on the redirection URLs." **enabled**

      - "I would like Worldline to display a short text to the customer on the secure …" **disabled**

      - Direct HTTP server-to-server request

        - Timing: Online but switch to a deferred request when the online requests fail.

        - Both URL fields: ``https://pretix-domain/_ogone/hook/<PARAMVAR>/``

        - Request method: POST

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.

This plugin has CI set up to enforce a few code style rules. To check locally, you need these packages installed::

    pip install flake8 isort black

To check your plugin for rule violations, run::

    black --check .
    isort -c .
    flake8 .

You can auto-fix some of these issues by running::

    isort .
    black .

To automatically check for these issues before you commit, you can run ``.install-hooks``.


Upstream documentation
----------------------

- https://support-payengine.ecom-psp.com/de/integration-solutions/integrations/hosted-payment-page
- https://support.legacy.worldline-solutions.com/en/

License
-------


Copyright 2024 pretix team

Released under the terms of the Apache License 2.0



.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
