# setScreenWatermarkImage

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setScreenWatermarkImage

```TypeScript
function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void
```

Sets a screen watermark policy, which takes effect for all users.

> **NOTE：**
> 
> 1. The screen watermark policy tiles the configured image across the entire screen. It is advised to use an image
> with transparency to ensure that the device screen content remains visible.
> 
> 2. If the watermark image size is smaller than the screen, the image will be stretched. If the watermark image
> size is larger than the screen, the image will be compressed. This implementation differs from the repeated
> tiling approach used for application-level watermarks.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void--><!--Device-securityManager-function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| pixelMap | image.PixelMap | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 'test.png' is only an example. Replace it with the actual one.
const path: string = context.filesDir + "/test.png";
// Create an ImageSource.
const imageSource: image.ImageSource = image.createImageSource(path);
// Create a PixelMap.
imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
  try {
    securityManager.setScreenWatermarkImage(wantTemp, pixelMap);
    console.info(`Succeeded in setting screen watermark image.`);
  } catch(err) {
    console.error(`Failed to set screen watermark image. Code: ${err.code}, message: ${err.message}`);
  }
}).catch((err: Error) => {
  console.error(`Failed to create PixelMap. message: ${err.message}`);
});
```
