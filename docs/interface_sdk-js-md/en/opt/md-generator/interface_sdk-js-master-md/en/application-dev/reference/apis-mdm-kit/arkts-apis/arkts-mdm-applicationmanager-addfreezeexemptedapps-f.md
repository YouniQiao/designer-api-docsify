# addFreezeExemptedApps

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addFreezeExemptedApps

```TypeScript
function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void
```

Adds applications to the background freeze-exempt application list for a specified user. This policy applies only to installed applications. If the parameter list contains uninstalled applications, error code 9200012 will be returned. If an application in the list is uninstalled after the policy is set, the uninstalled application will be removed from the list. Adding an application that already exists in the list will return success, but the application will not be added repeatedly to the policy list. Freezing operations include suspending the target application, and managing software resource agents, hardware resource agents, and high-power consumption.

**Since:** 22

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void--><!--Device-applicationManager-function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void-End-->

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
  applicationManager.addFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding FreezeExempted applications.');
} catch(err) {
  console.error(`Failed to add FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```
