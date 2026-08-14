# offScanModeChange

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## offScanModeChange

```TypeScript
function offScanModeChange(callback?: Callback<ScanMode>): void
```

Unsubscribe to an event indicating that the scanning mode of the local device has changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function offScanModeChange(callback?: Callback<ScanMode>): void--><!--Device-connection-function offScanModeChange(callback?: Callback<ScanMode>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ScanMode&gt; | No | Callback used to listen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
function ScanModeChangeEvent(scanMode: connection.ScanMode) {
    console.info(`Scan mode has changed, new mode: ${scanMode}`);
}
try {
    connection.offScanModeChange(ScanModeChangeEvent);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

