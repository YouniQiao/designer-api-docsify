# setDisallowedPermission

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## setDisallowedPermission

```TypeScript
function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void
```

Disables the specified permission of the specified user. After the permission is disabled, all applications under the specified user will be denied by default when applying for or using the specified permission. This API is applicable to enterprise security compliance scenarios, such as disabling high-risk permissions like camera and microphone to prevent privacy leaks, or disabling specific features (such as Bluetooth sharing) to prevent enterprise data from being transferred out.

> **NOTE：**
> 
> 1. Only permissions with an
> [APL level](../../../security/AccessToken/app-permission-mgmt-overview.md#basic-concepts-in-the-permission-mechanism)
> of normal or system_basic can be disabled. Otherwise, error code 9201045 is returned.
> 
> 2. A maximum of 200 permissions can be disabled per user.
> 
> 3. After a permission is disabled, only applications (system and common applications) are affected. System SAs
> can still use the permission.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void--><!--Device-securityManager-function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| permission | string | Yes | Name of the permission. |
| disallow | boolean | Yes | Whether to disable the permission. The value **true** indicates yes, and the value **false** indicates no. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. You can call [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) of **@ohos.account.osAccount** to obtain the user ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9201045](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201045-specified-permission-cannot-be-disabled) | This permission cannot be disallowed. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

