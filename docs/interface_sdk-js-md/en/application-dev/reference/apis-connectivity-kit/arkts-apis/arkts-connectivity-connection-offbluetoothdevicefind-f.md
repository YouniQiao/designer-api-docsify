# offBluetoothDeviceFind

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## offBluetoothDeviceFind

```TypeScript
function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

