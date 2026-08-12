# registerWatermarkCallback

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## registerWatermarkCallback

```TypeScript
function registerWatermarkCallback(callback: WatermarkCallback): void
```

Register to listen for watermark handling.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function registerWatermarkCallback(callback: WatermarkCallback): void--><!--Device-print-function registerWatermarkCallback(callback: WatermarkCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) | Yes | Indicates the callback type used in registering to listen for watermark handling. &lt;br&gt;Indicates the callback type used in registering to listen for watermark handling. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | the application does not have permission to call this function. |

