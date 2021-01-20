.. _sec_ref:

Reference
=========

.. contents::
   :local:
   :depth: 1

.. _sec_ref_config_file:

Configuration File
------------------

Example configuration:

.. code-block:: cfg

  [client]
  hawkbit_server            = 127.0.0.1:8080
  ssl                       = false
  ssl_verify                = false
  tenant_id                 = DEFAULT
  target_name               = test-target
  auth_token                = bhVahL1Il1shie2aj2poojeChee6ahShu
  #gateway_token            = bhVahL1Il1shie2aj2poojeChee6ahShu
  bundle_download_location  = /tmp/bundle.raucb
  retry_wait                = 60
  connect_timeout           = 20
  timeout                   = 60
  log_level                 = debug

  [device]
  product                   = Terminator
  model                     = T-1000
  serialnumber              = 8922673153
  hw_revision               = 2
  key1                      = value
  key2                      = value

**[client] section**

Configures how to connect with the hawkBit server, etc.

Mandatory options:

``hawkbit_server=<host>[:<port>]``
  The ip or hostname of the hawkbitServer to connect to.
  The ``port`` can be provided optionally.
  It needs to be separated with colons.

``target_name=<name>``
  Unique ``name`` string to identify controller.

``auth_token=<token>``
  Controller-specific authentication token.
  This is set for each device individually.

  .. note:: Either ``auth_token`` or ``gateway_token`` must be provided

``gateway_token``
  Gateway authentication token.
  This is set by hawkBit.

  .. note:: Either ``auth_token`` or ``gateway_token`` must be provided

``bundle_download_location=<path>``
  Full path to where the bundle should be downloaded to.
  E.g. set to ``/tmp/_bundle.raucb`` to let rauc-hawkbit-updater use this
  location withing ``/tmp``.

Optional options:
  
``tenant_id=<ID>``
  ID of the tenant to connect with. Defaults to ``DEFAULT``.

``ssl=<boolean>``
  Whether to use SSL connections (``https``) or not (``http``).
  Defaults to true.

``ssl_verify``
  Whether to enforce SSL verification or not.
  Defaults to true.

``connect_timeout=<seconds>``
  HTTP connection setup timeout [seconds].
  Defaults to 20 seconds.

``timeout=<seconds>``
  HTTP request Timeout [seconds]
  Defaults to 60 seconds.

``retry_wait=<seconds>``
  Time in seconds to wait before retrying [seconds]
  Defaults to 60 seconds.

``log_level=<level>``
  Log level to print, where ``level`` is a string of

  * debug
  * info
  * message
  * critical
  * error
  * fatal

.. _keyring-section:

**[device] section**

This section allows to set a custom list of key-value pairs that will be used
as config data target attribute for device registration.
They can be used for target filtering.
