# BLE

Provides methods to operate or manage Bluetooth.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLE](arkts-connectivity-bluetoothmanager-ble-n.md#ble)

<!--Device-bluetooth-namespace BLE--><!--Device-bluetooth-namespace BLE-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md#creategattserver) | create a JavaScript Gatt server instance. |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md#creategattclientdevice) | create a JavaScript Gatt client device instance. |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md#getconnectedbledevices) | Obtains the list of devices in the connected status. |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md#startblescan) | Starts scanning for specified BLE devices with filters. |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md#stopblescan) | Stops BLE scanning. |
| [on_BLEDeviceFind](arkts-connectivity-ble-onbledevicefind-f.md#onbledevicefind) | Subscribe BLE scan result. |
| [off_BLEDeviceFind](arkts-connectivity-ble-offbledevicefind-f.md#offbledevicefind) | Unsubscribe BLE scan result. |

