# pick

## Modules to Import

```TypeScript
import { screenshot } from '@kit.ArkUI';
```

## pick

```TypeScript
function pick(): Promise<PickInfo>
```

Obtains this screenshot. Currently, only the screenshot of the display whose ID is **0** can be obtained. (If a screenshot of the extended screen is needed, you can use the [capture](arkts-arkui-screenshot-capture-f.md#capture) API.) This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-screenshot-function pick(): Promise<PickInfo>--><!--Device-screenshot-function pick(): Promise<PickInfo>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PickInfo](arkts-arkui-screenshot-pickinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Call the pick API to obtain the screenshot.
  let promise = screenshot.pick();
  promise.then((pickInfo: screenshot.PickInfo) => {
    console.info(`pick Pixel bytes number: ${pickInfo.pixelMap.getPixelBytesNumber()}`);
    console.info(`pick Rect: ${pickInfo.pickRect}`);
    pickInfo.pixelMap.release(); // Release the memory in time after the PixelMap is no longer needed.
  }).catch((err: BusinessError) => {
    console.error(`Failed to pick. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to pick. Code: ${exception.code}, message: ${exception.message}`);
}
```
