# BLE

Provides methods to operate or manage Bluetooth.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [ble/ble](arkts-bluetooth-ble.md#@ohos.bluetooth.ble)

<!--Device-bluetoothManager-namespace BLE--><!--Device-bluetoothManager-namespace BLE-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from 'bluetoothManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md#createGattServer) | create a JavaScript Gatt server instance. |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md#createGattClientDevice) | create a JavaScript Gatt client device instance. |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md#getConnectedBLEDevices) | Obtains the list of devices in the connected status. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH. |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md#startBLEScan) | Starts scanning for specified BLE devices with filters. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH and MANAGE_BLUETOOTH and LOCATION to ACCESS_BLUETOOTH. |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md#stopBLEScan) | Stops BLE scanning. On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH. |
| [on_BLEDeviceFind](arkts-connectivity-ble-onbledevicefind-f.md#on_BLEDeviceFind) | Subscribe BLE scan result. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH. |
| [off_BLEDeviceFind](arkts-connectivity-ble-offbledevicefind-f.md#off_BLEDeviceFind) | Unsubscribe BLE scan result. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH. |

