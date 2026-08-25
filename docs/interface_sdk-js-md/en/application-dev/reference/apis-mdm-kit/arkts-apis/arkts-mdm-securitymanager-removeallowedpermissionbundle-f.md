# removeAllowedPermissionBundle

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## removeAllowedPermissionBundle

```TypeScript
function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

Removes an application from the permission usage exception list. After the application is removed, it cannot use the corresponding permission any more.

> **NOTE：**&gt;
> The permission must first be disabled via the
> [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md) API before an application can be removed
> from the permission usage exception list. Otherwise, error code 9201044 is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| permission | string | Yes |
| applicationInstance | common.ApplicationInstance | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201044](../errorcode-enterpriseDeviceManager.md#9201044-specified-permission-not-disabled) |
