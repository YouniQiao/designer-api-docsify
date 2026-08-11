# setKioskFeatures

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## setKioskFeatures

```TypeScript
function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void
```

Sets the features of the kiosk mode. You can use this API to control whether the notification center and control panel can be accessed in kiosk mode.

Since API version 24, you can set whether to allow users to swipe up from the bottom to access the recent taskbar and swipe left or right to display the side dock.

In non-kiosk mode, this API can be called normally but does not take effect. The settings will take effect after kiosk mode is enabled.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_SET_KIOSK

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void--><!--Device-applicationManager-function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| features | Array&lt;KioskFeature&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let kioskFeatures: Array<applicationManager.KioskFeature> = [];
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_NOTIFICATION_CENTER);
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_CONTROL_CENTER);
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_GESTURE_CONTROL);
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_SIDE_DOCK);
try {
  applicationManager.setKioskFeatures(wantTemp, kioskFeatures);
  console.info('Succeeded in setting kiosk feature.');
} catch (err) {
  console.error(`Failed to set kiosk feature. Code is ${err.code}, message is ${err.message}`);
}
```
