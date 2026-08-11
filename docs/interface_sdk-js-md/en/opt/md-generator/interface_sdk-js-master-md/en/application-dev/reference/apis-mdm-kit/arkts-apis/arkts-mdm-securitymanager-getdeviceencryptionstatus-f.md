# getDeviceEncryptionStatus

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## getDeviceEncryptionStatus

```TypeScript
function getDeviceEncryptionStatus(admin: Want): DeviceEncryptionStatus
```

Queries the encryption status of the device file system.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [securityManager.getSecurityStatus](arkts-mdm-securitymanager-getsecuritystatus-f.md#getsecuritystatus)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getDeviceEncryptionStatus(admin: Want): DeviceEncryptionStatus--><!--Device-securityManager-function getDeviceEncryptionStatus(admin: Want): DeviceEncryptionStatus-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceEncryptionStatus](arkts-mdm-securitymanager-deviceencryptionstatus-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
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
  let result: securityManager.DeviceEncryptionStatus = securityManager.getDeviceEncryptionStatus(wantTemp);
  console.info(`Succeeded in getting device encryption status. isEncrypted: ${result.isEncrypted}`);
} catch(err) {
  console.error(`Failed to get device encryption status. Code: ${err.code}, message: ${err.message}`);
}
```
