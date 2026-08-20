# removeAllowedPermissionBundle

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## removeAllowedPermissionBundle

```TypeScript
function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

Removes an application from the permission usage exception list. After the application is removed, it cannot use the corresponding permission any more.

> **NOTE：**
> 
> The permission must first be disabled via the &gt; [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md) API before an application can be removed &gt; from the permission usage exception list. Otherwise, error code 9201044 is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void--><!--Device-securityManager-function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| permission | string | Yes | Name of the permission. |
| applicationInstance | common.ApplicationInstance | Yes | Information about the application instance to be removed from the permission exception list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9201044](../errorcode-enterpriseDeviceManager.md#9201044-specified-permission-not-disabled) | This permission is not disallowed. Applications cannot be added to or removed from the trustlist. |

