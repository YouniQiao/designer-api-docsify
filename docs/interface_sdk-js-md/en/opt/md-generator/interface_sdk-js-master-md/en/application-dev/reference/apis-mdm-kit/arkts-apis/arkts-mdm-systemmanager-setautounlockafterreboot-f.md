# setAutoUnlockAfterReboot

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setAutoUnlockAfterReboot

```TypeScript
function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void
```

Sets automatic unlocking upon device reboot. This setting takes effect only on devices without a screen lock password. This API is applicable to enterprise unattended devices or scenarios where services need to be quickly restored through a restart, avoiding device downtime caused by manual unlocking, thereby improving device operation and maintenance efficiency and service continuity.

**Since:** 20

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void--><!--Device-systemManager-function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isAllowed | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let isAllowed: boolean = true;
try {
  systemManager.setAutoUnlockAfterReboot(wantTemp, isAllowed);
  console.info('Succeeded in setting setAutoUnlockAfterReboot.');
} catch (err) {
  console.error(`Failed to set auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
}
```
