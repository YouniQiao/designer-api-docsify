# offReadData

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## offReadData

```TypeScript
function offReadData(callback?: Callback<DataParams>): void
```

Unsubscribes from the event reported when data is read from the port.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function offReadData(callback?: Callback<DataParams>): void--><!--Device-dataTransfer-function offReadData(callback?: Callback<DataParams>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataParams](arkts-connectivity-datatransfer-dataparams-i.md)&gt; | No | Callback used to listen for the port read event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

