# setOtaUpdateNonceEnable

## Modules to Import

```TypeScript
```

## setOtaUpdateNonceEnable

```TypeScript
function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void
```

Sets whether to enable nonce for OTA update (nonce is enabled by default). When nonce is enabled, the system verifies the validity of the nonce during the OTA update process to prevent replay attacks and enhance system security. > **NOTE：**> > To ensure system security, it is not advised to disable nonce verification unless required by specific use cases > such as intranet updates.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void--><!--Device-systemManager-function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isEnable | boolean | Yes |

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
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let isEnable: boolean = true;
try {
  systemManager.setOtaUpdateNonceEnable(wantTemp, isEnable);
  console.info('Succeeded in setting OTA update Nonce enable.');
} catch (err) {
  console.error(`Failed to set OTA update Nonce enable. Code is ${err.code}, message is ${err.message}`);
}
```
