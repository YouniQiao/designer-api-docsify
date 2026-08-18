# offStateChange

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## offStateChange

```TypeScript
function offStateChange(callback?: Callback<BluetoothState>): void
```

Unsubscribe the event reported when the Bluetooth state changes.

**Since:** 23

<!--Device-access-function offStateChange(callback?: Callback<BluetoothState>): void--><!--Device-access-function offStateChange(callback?: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;BluetoothState&gt; | No | Callback used to listen for the Bluetooth state event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900099 | Operation failed. |

