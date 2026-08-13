# removeFreezeExemptedApps

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## removeFreezeExemptedApps

```TypeScript
function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void
```

Removes the background freeze-exempt application list for a specified user. After the removal, the applications can be frozen by the system. If the parameter list includes uninstalled applications, the removal will still succeed. Installed applications will be removed from the list, while uninstalled ones will not impact the removal process.

**Since:** 22

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void--><!--Device-applicationManager-function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| applicationInstances | Array & lt;common.ApplicationInstance & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // Replace it as required.
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.removeFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in removing FreezeExempted applications.');
} catch(err) {
  console.error(`Failed to remove FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```
