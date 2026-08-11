# registerWatermarkCallback

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## registerWatermarkCallback

```TypeScript
function registerWatermarkCallback(callback: WatermarkCallback): void
```

Register to listen for watermark handling.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function registerWatermarkCallback(callback: WatermarkCallback): void--><!--Device-print-function registerWatermarkCallback(callback: WatermarkCallback): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [WatermarkCallback](arkts-basicservices-print-watermarkcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let watermarkCallback: print.WatermarkCallback = (jobId: string, fd: number) => {
    console.info('Watermark callback triggered, jobId: ' + jobId + ', fd: ' + fd);
}

try {
    print.registerWatermarkCallback(watermarkCallback);
    console.info('registerWatermarkCallback success');
} catch (error) {
    console.error('registerWatermarkCallback error: ' + JSON.stringify(error));
}
```
