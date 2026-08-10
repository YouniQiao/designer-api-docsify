# offBluetoothDeviceFind

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## offBluetoothDeviceFind

```TypeScript
function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-connection-function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void--><!--Device-connection-function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | No | Callback used to listen for the discovering event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

