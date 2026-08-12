# setWatermarkImageForAppWindows

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## setWatermarkImageForAppWindows

```TypeScript
function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>
```

Sets a watermark image for windows in the current application process. This API uses a promise to return the result. This API must be called after  
[loadContent()](arkts-arkui-window-window-i.md#loadContent)or [setUIContent()](arkts-arkui-window-window-i.md#setUIContent)takes effect.

**Since:** 21

<!--Device-window-function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>--><!--Device-window-function setWatermarkImageForAppWindows(pixelMap: image.PixelMap | undefined): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300003-abnormal-window-manager-service) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-window.md#1300016-parameter-verification-error) |

## Examples

```TypeScript
import { image } from "@kit.ImageKit";
import { BusinessError } from "@kit.BasicServicesKit";

let color: ArrayBuffer = new ArrayBuffer(96);
let initializationOptions: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.RGBA_8888,
  size: {
    height: 4,
    width: 6,
  },
};
image.createPixelMap(color, initializationOptions).then((pixelMap: image.PixelMap) => {
  console.info("Succeeded in creating pixelmap.");
  try {
    let promise = window.setWatermarkImageForAppWindows(pixelMap);
    promise.then(() => {
        console.info("Succeeded in setting watermark image.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to set watermark image. Cause code: ${err.code}, message: ${err.message}`);
    });
  } catch (exception) {
    console.error(`Failed to set watermark image. Exception code: ${exception.code}, message: ${exception.message}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to create PixelMap. Cause code: ${err.code}, message: ${err.message}`);
});
```
