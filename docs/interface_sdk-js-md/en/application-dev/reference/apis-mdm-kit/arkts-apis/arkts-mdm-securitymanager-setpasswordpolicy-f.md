# setPasswordPolicy

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setPasswordPolicy

```TypeScript
function setPasswordPolicy(admin: Want, policy: PasswordPolicy): void
```

Sets the device screen lock password policy. After the policy is set, when a user sets a lock screen password, if the password does not meet the requirements, a security prompt will be displayed asking the user to reset the password. This policy is applicable to enterprise security compliance scenarios, such as requiring employees to use strong passwords and change passwords periodically, to reduce the risk of enterprise data leakage.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| policy | [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-system-ability-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
