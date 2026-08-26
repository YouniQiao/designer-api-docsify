# BLE

Provides methods to operate or manage Bluetooth.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLE](arkts-connectivity-bluetoothmanager-ble-n.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import bas from '@kit.ConnectivityKit.bas';
import common from '@kit.ConnectivityKit.common';
import bluetooth from '@kit.ConnectivityKit';
import map from '@kit.ConnectivityKit.map';
import pan from '@kit.ConnectivityKit.pan';
import pbap from '@kit.ConnectivityKit.pbap';
import opp from '@kit.ConnectivityKit.opp';
import socket from '@kit.ConnectivityKit.socket';
import wearDetection from '@kit.ConnectivityKit.wearDetection';
import bluetoothManager from '@kit.ConnectivityKitManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createGattServer](arkts-connectivity-ble-creategattserver-f.md) | create a JavaScript Gatt server instance. |
| [createGattClientDevice](arkts-connectivity-ble-creategattclientdevice-f.md) | create a JavaScript Gatt client device instance. |
| [getConnectedBLEDevices](arkts-connectivity-ble-getconnectedbledevices-f.md) | Obtains the list of devices in the connected status. |
| [startBLEScan](arkts-connectivity-ble-startblescan-f.md) | Starts scanning for specified BLE devices with filters. |
| [stopBLEScan](arkts-connectivity-ble-stopblescan-f.md) | Stops BLE scanning. |
| [on](arkts-connectivity-ble-on-f.md#onbledevicefind) | Subscribe BLE scan result. |
| [off](arkts-connectivity-ble-off-f.md#offbledevicefind) | Unsubscribe BLE scan result. |
