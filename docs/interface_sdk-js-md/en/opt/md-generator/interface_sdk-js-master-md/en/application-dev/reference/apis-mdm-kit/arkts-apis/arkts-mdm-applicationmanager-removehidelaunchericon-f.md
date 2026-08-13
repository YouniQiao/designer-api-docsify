# removeHideLauncherIcon

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## removeHideLauncherIcon

```TypeScript
function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void
```

Removes applications from the home screen icon hide list. > **NOTE：**> > After unhiding, applications will be placed in the first available slot starting from the second screen of the > home screen. If no empty slot is found on screens 2 to 18, it will search for an empty slot on the first screen. > If no empty slot is available on the first screen, a small folder will be created at the position of the first > application on the second screen to contain the applications.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void--><!--Device-applicationManager-function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleNames | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let bundleNames: Array<string> = ['com.example.test'];
try {
  applicationManager.removeHideLauncherIcon(wantTemp, bundleNames);
  console.info('Succeeded in removing hide launcher icon.');
} catch (err) {
  console.error(`Failed to remove hide launcher icon. Code is ${err.code}, message is ${err.message}`);
}
```
