# getPasswordPolicy

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getPasswordPolicy

```TypeScript
function getPasswordPolicy(admin: Want): PasswordPolicy
```

Obtains the device screen lock password policy.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getPasswordPolicy(admin: Want): PasswordPolicy--><!--Device-securityManager-function getPasswordPolicy(admin: Want): PasswordPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |


## getPasswordPolicy

```TypeScript
function getPasswordPolicy(admin: Want | null): PasswordPolicy
```

Obtains the device screen lock password policy. Enterprises can use this API to query the current password policy for policy audit and compliance check, ensuring that the device password policy complies with enterprise security specifications.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getPasswordPolicy(admin: Want | null): PasswordPolicy--><!--Device-securityManager-function getPasswordPolicy(admin: Want | null): PasswordPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
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
  let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy(wantTemp);
  console.info(`Succeeded in getting password policy, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get password policy. Code: ${err.code}, message: ${err.message}`);
}
```
