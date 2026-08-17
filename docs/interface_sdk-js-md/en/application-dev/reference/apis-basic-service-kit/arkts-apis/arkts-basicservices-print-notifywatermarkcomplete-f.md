# notifyWatermarkComplete

## Modules to Import

```TypeScript
import { print } from 'print';
```

## notifyWatermarkComplete

```TypeScript
function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void
```

Notify watermark complete.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void--><!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | Indicates the job ID. <br>Print job ID in preview. |
| result | [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) | Yes | Indicates the result. <br>Watermark processing results. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

