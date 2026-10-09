# BLE

```TypeScript
namespace BLE
```

Provides methods to operate or manage Bluetooth.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLE](arkts-connectivity-bluetoothmanager-ble-n.md)

<!--Device-bluetooth-namespace BLE--><!--Device-bluetooth-namespace BLE-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md) | create a JavaScript Gatt client device instance. |
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md) | create a JavaScript Gatt server instance. |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md) | Obtains the list of devices in the connected status. |
| [off](arkts-connectivity-ble-off-f.md#offbledevicefind) | Unsubscribe BLE scan result. |
| [on](arkts-connectivity-ble-on-f.md#onbledevicefind) | Subscribe BLE scan result. |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md) | Starts scanning for specified BLE devices with filters. |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md) | Stops BLE scanning. |
