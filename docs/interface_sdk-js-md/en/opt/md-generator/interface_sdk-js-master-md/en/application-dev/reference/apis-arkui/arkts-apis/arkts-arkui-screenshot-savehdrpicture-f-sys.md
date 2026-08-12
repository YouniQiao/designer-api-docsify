# saveHdrPicture (System API)

## Modules to Import

```TypeScript
import { screenshot } from '@kit.ArkUI';
```

## saveHdrPicture

```TypeScript
function saveHdrPicture(options?: HdrScreenshotOptions): Promise<Array<image.PixelMap>>
```

Obtains a screenshot. This API uses a promise to return the result. SDR stands for Standard Dynamic Range, and HDR stands for High Dynamic Range.

- If the screen contains HDR resources (even if they are partially obscured), this API returns an array with both  
SDR and HDR PixelMaps, regardless of whether HDR is enabled.  
- If there are no HDR resources, it returns an array with a single SDR PixelMap. Unlike the  
[save](arkts-arkui-screenshot-save-f-sys.md#save) API, which returns a single SDR PixelMap, this API always returns an array. Additionally, this API does not support cropping,stretching, or rotating features available in the  
[save](arkts-arkui-screenshot-save-f-sys.md#save) API.

**Since:** 20

**Required permissions:** 
- API version 22+: ohos.permission.CAPTURE_SCREEN or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 20 - 21: ohos.permission.CAPTURE_SCREEN

<!--Device-screenshot-function saveHdrPicture(options?: HdrScreenshotOptions): Promise<Array<image.PixelMap>>--><!--Device-screenshot-function saveHdrPicture(options?: HdrScreenshotOptions): Promise<Array<image.PixelMap>>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [HdrScreenshotOptions](arkts-arkui-screenshot-hdrscreenshotoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;image.PixelMap & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1400004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400004-parameter-error) |
| [1400001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let hdrScreenshotOptions: screenshot.HdrScreenshotOptions = {
  displayId: 0,
  isNotificationNeeded: true,
  isCaptureFullOfScreen: true,
  displayIntent: screenshot.DisplayIntentType.CANONICAL
};
try {
  let promise = screenshot.saveHdrPicture(hdrScreenshotOptions);
  promise.then((pixelMapArray: Array<image.PixelMap>) => {
    for (let i = 0; i < pixelMapArray.length; i++) {
      const pixelMap = pixelMapArray[i];
      console.info(`succeeded in saving screenshot ${i}. Pixel bytes number: ${pixelMap.getPixelBytesNumber()}`);
      pixelMap.release();
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to save SDR and HDR screenshot. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to save SDR and HDR screenshot. Code: ${exception.code}, message: ${exception.message}`);
}
```
