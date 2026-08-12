# notifyWatermarkComplete

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## notifyWatermarkComplete

```TypeScript
function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void
```

Notify watermark complete.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void--><!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | Indicates the job ID. &lt;br&gt;Print job ID in preview. |
| result | [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) | Yes | Indicates the result. &lt;br&gt;Watermark processing results. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

