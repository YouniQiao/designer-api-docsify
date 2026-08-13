# getInstallLocalEnterpriseAppEnabled

## Modules to Import

```TypeScript
import { systemManager } from '@kit.MDMKit';
```

## getInstallLocalEnterpriseAppEnabled

```TypeScript
function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean
```

Checks whether local installation of enterprise applications is supported. This API is applicable to scenarios where there is a need to verify whether the local installation of enterprise applications is enabled on the device, helping enterprise administrators confirm the policy configuration status to ensure that enterprise applications can be properly installed.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean--><!--Device-systemManager-function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let isEnable: boolean = systemManager.getInstallLocalEnterpriseAppEnabled(wantTemp);
  console.info('Succeeded in getting installLocalEnterpriseAppEnabled.');
} catch (err) {
  console.error(`Failed to get installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
}
```
