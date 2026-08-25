# setWatermarkImage

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## setWatermarkImage

```TypeScript
function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void
```

Sets a watermark policy for a specified application of a specified user. Currently, a maximum of 100 policies can be saved.

> **NOTE：**&gt;
> 1. This API is intended for setting watermarks on third-party applications in enterprise scenarios to reduce the
> risk of information leakage. You are not advised to set watermarks for system applications (such as the home
> screen application), as unknown exceptions may occur.&gt;
> 2. The watermark image will be tiled repeatedly to cover the entire application interface.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| source | string \| image.PixelMap | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
try {
    securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId);
    console.info(`Succeeded in setting set watermarkImage policy.`);
} catch(err) {
    console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```


## setWatermarkImage

```TypeScript
function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number, properties: WatermarkProperties): void
```

Sets a watermark policy for a specified application of a specified user. Currently, a maximum of 100 policies can be saved.

> **NOTE：**&gt;
> This API is intended for setting watermarks on third-party applications in enterprise scenarios to reduce the
> risk of information leakage. You are not advised to set watermarks for system applications (such as the home
> screen application), as unknown exceptions may occur.&gt;
> The row and column parameters in the watermark [properties](arkts-mdm-securitymanager-watermarkproperties-i.md) must be
> integers in the range [1, 255]. If a value less than 1 or greater than 255 is passed, the API returns error code
> 9200012.&gt;
> When both the row count and column count are set to **1**, a single watermark image is displayed at the center of
> the screen. When the row count is set to **m** and the column count to **n**, m × n watermark images are
> displayed in an m-by-n grid layout. If the specified row and column counts are too large for the grid layout to
> fit within the window, the watermark will be repeatedly tiled across the entire application window, starting from
> the top-left corner. Any part of the watermark image that exceeds the right or bottom edges of the window will be
> clipped. (For example, for a screen size of 1260 × 2720 pixels and a watermark image of 100 × 100 pixels, if the
> row count exceeds 27 or the column count exceeds 12, the watermark will be repeatedly tiled to cover the entire
> application window.)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| source | string \| image.PixelMap | Yes |
| accountId | number | Yes |
| properties | [WatermarkProperties](arkts-mdm-securitymanager-watermarkproperties-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

See [setWatermarkImage](#setwatermarkimage)
