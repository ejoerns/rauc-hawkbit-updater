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

General notes about ``client`` section.

``key``
  Description

.. _keyring-section:

**[device] section**

General notes about ``device`` section.

``key``
  Description
