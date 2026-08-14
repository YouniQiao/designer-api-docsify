# offPinRequired

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## offPinRequired

```TypeScript
function offPinRequired(callback?: Callback<PinRequiredParam>): void
```

Unsubscribe the event of a pairing request from a remote Bluetooth device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function offPinRequired(callback?: Callback<PinRequiredParam>): void--><!--Device-connection-function offPinRequired(callback?: Callback<PinRequiredParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PinRequiredParam&gt; | No | Callback used to listen for the pairing request event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

