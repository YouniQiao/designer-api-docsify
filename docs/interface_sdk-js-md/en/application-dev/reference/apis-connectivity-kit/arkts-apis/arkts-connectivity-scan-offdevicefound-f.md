# offDeviceFound

## Modules to Import

```TypeScript
import { scan } from '@kit.ConnectivityKit';
```

## offDeviceFound

```TypeScript
function offDeviceFound(callback?: Callback<ScanResults[]>): void
```

Unsubscribes from NearLink scan results.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void--><!--Device-scan-function offDeviceFound(callback?: Callback<ScanResults[]>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScanResults](arkts-connectivity-scan-scanresults-i.md)[]&gt; | No | Callback used to listen for the scan result event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |

