# setScreenPrivacyMaskImage (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## setScreenPrivacyMaskImage

```TypeScript
function setScreenPrivacyMaskImage(screenId: number, image?: image.PixelMap): Promise<void>
```

Sets a privacy mask image for the screen. This API uses a promise to return the result.

**Since:** 19

<!--Device-screen-function setScreenPrivacyMaskImage(screenId: long, image?: image.PixelMap): Promise<void>--><!--Device-screen-function setScreenPrivacyMaskImage(screenId: long, image?: image.PixelMap): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |
| image | image.PixelMap | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
let options: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
image.createPixelMap(color, options).then((pixelMap: image.PixelMap) => {
  console.info('Succeeded in creating pixelmap.');
  // Obtain the screen ID using getAllScreens().
  let screenId: number = 1; // Screen ID.
  // Set a privacy mask image for the screen.
  screen.setScreenPrivacyMaskImage(screenId, pixelMap).then(() => {
    console.info('Succeeded in setting the privacy mask image for the screen.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the privacy mask image for the screen. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((error: BusinessError) => {
  console.error(`Failed to create pixelmap. Code: ${error.code}, message: ${error.message}`);
});
```
