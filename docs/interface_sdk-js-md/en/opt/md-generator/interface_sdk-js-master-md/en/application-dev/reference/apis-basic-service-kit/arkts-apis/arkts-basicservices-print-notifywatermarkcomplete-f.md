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

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void--><!--Device-print-function notifyWatermarkComplete(jobId: string, result: WatermarkHandleResult): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| result | [WatermarkHandleResult](arkts-basicservices-print-watermarkhandleresult-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
    console.info('Watermark callback triggered, jobId: ' + jobId + ', fd: ' + fd);

    try {
        // Notify the system that the watermark processing is successful.
        print.notifyWatermarkComplete(jobId, print.WatermarkHandleResult.WATERMARK_HANDLE_SUCCESS);
        console.info('notifyWatermarkComplete success');
    } catch (error) {
        console.error('notifyWatermarkComplete error: ' + JSON.stringify(error));
    }
}

try {
    print.registerWatermarkCallback(watermarkCallback);
    console.info('registerWatermarkCallback success');
} catch (error) {
    console.error('registerWatermarkCallback error: ' + JSON.stringify(error));
}
```
