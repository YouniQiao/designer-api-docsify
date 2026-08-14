# addAllowedPermissionBundle

## Modules to Import

```TypeScript
import { securityManager } from 'securityManager';
```

## addAllowedPermissionBundle

```TypeScript
function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

Adds an application to the permission usage exception list. Applications in the list are not subject to the permission restriction policy set via [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission). This API is applicable to enterprise scenarios. For example, when the camera permission is disabled, attendance applications and collaborative office applications can still use the camera, ensuring that critical enterprise business operates normally. > **NOTE：**> > 1. The permission must first be disabled via the > [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission) API before an application can be added > to the permission usage exception list. Otherwise, error code 9201044 is returned. > > 2. An application cannot be added to the permission usage exception list if it has not actually requested the > specified permission. For example, if the camera permission is disabled and application A has not requested the > camera permission, it cannot be added to the exception list for the camera permission, and error code 9200012 is > returned. You can use the [bm dump](../../../tools/bm-tool.md#dump) command to check whether an application has > requested a specific permission. > > 3. When a specified permission is enabled via the > [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission) API, the corresponding permission usage > exception list is cleared synchronously. > > 4. For any given permission, a maximum of 1024 applications can be added to the exception list across all users. > > 5. Both system applications and third-party applications can be added.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void--><!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| permission | string | Yes | Name of the permission. |
| applicationInstance | common.ApplicationInstance | Yes | Information about the application instance to be added to the permission exception list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9201044](../errorcode-enterpriseDeviceManager.md#9201044-specified-permission-not-disabled) | This permission is not disallowed. Applications cannot be added to or removed from the trustlist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9201015](../errorcode-enterpriseDeviceManager.md#9201015-specified-application-not-installed) | The application is not installed. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

