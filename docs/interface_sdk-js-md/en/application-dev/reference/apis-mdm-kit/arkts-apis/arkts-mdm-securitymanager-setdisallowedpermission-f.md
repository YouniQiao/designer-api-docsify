# setDisallowedPermission

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## setDisallowedPermission

```TypeScript
function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void
```

Disables the specified permission of the specified user. After the permission is disabled, all applications under the specified user will be denied by default when applying for or using the specified permission. This API is applicable to enterprise security compliance scenarios, such as disabling high-risk permissions like camera and microphone to prevent privacy leaks, or disabling specific features (such as Bluetooth sharing) to prevent enterprise data from being transferred out.

> **NOTE：**&gt;
> 1. Only permissions with an
> [APL level](../../../security/AccessToken/app-permission-mgmt-overview.md#basic-concepts-in-the-permission-mechanism)
> of normal or system_basic can be disabled. Otherwise, error code 9201045 is returned.&gt;
> 2. A maximum of 200 permissions can be disabled per user.&gt;
> 3. After a permission is disabled, only applications (system and common applications) are affected. System SAs
> can still use the permission.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| permission | string | Yes |
| disallow | boolean | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201045](../errorcode-enterpriseDeviceManager.md#9201045-specified-permission-cannot-be-disabled) |
