# BLE

Provides methods to operate or manage Bluetooth.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [BLE](arkts-connectivity-bluetoothmanager-ble-n.md#BLE)

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
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md#createGattServer) | create a JavaScript Gatt server instance. |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md#createGattClientDevice) | create a JavaScript Gatt client device instance. |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md#getConnectedBLEDevices) | Obtains the list of devices in the connected status. |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md#startBLEScan) | Starts scanning for specified BLE devices with filters. |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md#stopBLEScan) | Stops BLE scanning. |
| [on_BLEDeviceFind](arkts-connectivity-ble-onbledevicefind-f.md#on_BLEDeviceFind) | Subscribe BLE scan result. |
| [off_BLEDeviceFind](arkts-connectivity-ble-offbledevicefind-f.md#off_BLEDeviceFind) | Unsubscribe BLE scan result. |

