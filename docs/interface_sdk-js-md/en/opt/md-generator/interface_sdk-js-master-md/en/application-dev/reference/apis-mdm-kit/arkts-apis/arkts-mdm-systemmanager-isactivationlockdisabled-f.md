# isActivationLockDisabled

## Modules to Import

```TypeScript
```

## isActivationLockDisabled

```TypeScript
function isActivationLockDisabled(admin: Want): Promise<boolean>
```

Checks whether the device activation lock is disabled. This API is applicable to scenarios where you need to verify the device activation lock status. It helps enterprise administrators confirm the device's security configuration, especially when understanding the activation lock state is necessary for device transfer or recycling.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function isActivationLockDisabled(admin: Want): Promise<boolean>--><!--Device-systemManager-function isActivationLockDisabled(admin: Want): Promise<boolean>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

systemManager.isActivationLockDisabled(wantTemp).then(result => {
  console.info(`Succeeded in getting activation lock status: ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set activation lock status. Code: ${err.code}, message: ${err.message}`);
});
```
