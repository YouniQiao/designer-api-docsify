# removeDockApp

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## removeDockApp

```TypeScript
function removeDockApp(admin: Want, bundleName: string, abilityName: string): void
```

Removes an application from the shortcut bar. > **NOTE：**> > The following applications cannot be removed from the shortcut bar using this API: Application Center, Task > Center, Files, and Recycle Bin. Otherwise, error code 9201018 will be reported.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeDockApp(admin: Want, bundleName: string, abilityName: string): void--><!--Device-applicationManager-function removeDockApp(admin: Want, bundleName: string, abilityName: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| abilityName | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [9201016](../errorcode-enterpriseDeviceManager.md#9201016-specified-application-not-in-dock) |
| [9201018](../errorcode-enterpriseDeviceManager.md#9201018-specified-application-inoperable) |
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

try {
  // Replace it as required.
  let bundleName: string = 'com.example.exampleapplication';
  let abilityName: string = 'EntryAbility';
  applicationManager.removeDockApp(wantTemp, bundleName, abilityName);
  console.info('Succeeded in removing dock app.');
} catch(err) {
  console.error(`Failed to remove dock app. Code: ${err.code}, message: ${err.message}`);
}
```
