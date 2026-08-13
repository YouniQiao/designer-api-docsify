# cancelScreenWatermarkImage

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## cancelScreenWatermarkImage

```TypeScript
function cancelScreenWatermarkImage(admin: Want): void
```

Cancels a screen watermark policy, which takes effect for all users. After the cancellation is successful, the watermark on the device screen disappears. When a device no longer requires screen watermark protection, enterprises can call this API to cancel the watermark policy. Only the user who sets the screen watermark can cancel it. For example, user 101 cannot cancel the screen mark set by user 100

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function cancelScreenWatermarkImage(admin: Want): void--><!--Device-securityManager-function cancelScreenWatermarkImage(admin: Want): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    securityManager.cancelScreenWatermarkImage(wantTemp);
    console.info(`Succeeded in canceling screen watermark image.`);
} catch(err) {
    console.error(`Failed to cancel screen watermark image. Code: ${err.code}, message: ${err.message}`);
}
```
