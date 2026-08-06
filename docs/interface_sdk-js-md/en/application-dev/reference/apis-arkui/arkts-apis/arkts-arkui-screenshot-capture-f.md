# capture

## capture

```TypeScript
function capture(options?: CaptureOption): Promise<image.PixelMap>
```

Takes a screenshot of the entire screen. This API uses a promise to return the result.

This API allows you to take screenshots of different screens by setting various **displayId** values, but only full  
-screen captures are supported. The [pick]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API allows you to take screenshots of a specified  
region.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 22+: ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CUSTOM_SCREEN_RECORDING
- API version 14 - 21: ohos.permission.CUSTOM_SCREEN_CAPTURE

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-screenshot-function capture(options?: CaptureOption): Promise<image.PixelMap>--><!--Device-screenshot-function capture(options?: CaptureOption): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Capture options. If this parameter is left blank, the display with ID 0 is captured by default.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 22 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;image.PixelMap&gt; | Promise used to return a PixelMap object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Incorrect parameter types. 2.Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported on this device. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let captureOption: screenshot.CaptureOption = {
  "displayId": 0
};
try {
  let promise = screenshot.capture(captureOption);
  promise.then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in saving screenshot. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
    pixelMap.release(); // Release the memory in time after the PixelMap is used.
  }).catch((err: BusinessError) => {
    console.error(`Failed to save screenshot. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to save screenshot. Code: ${exception.code}, message: ${exception.message}`);
};
```

