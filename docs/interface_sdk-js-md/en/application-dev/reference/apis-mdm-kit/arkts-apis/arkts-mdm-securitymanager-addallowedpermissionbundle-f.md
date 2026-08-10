# addAllowedPermissionBundle

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## addAllowedPermissionBundle

```TypeScript
function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

将应用添加至权限使用例外名单，例外名单中的应用不受[setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setdisallowedpermission)设置的权限禁用策略限制。适用于企业应用场景，如相机权限被禁用时，允许考勤应用、协作办公应用继续使用相机功能，保障企业关键业务正常运行。

> **说明：**
> 
> 1.必须先通过[setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setdisallowedpermission)接口禁用权限后，才能添加应用到权限使用例外名单，否则返回错误码920
> 1044。
> 
> 2.应用实际未申请指定权限时，不可将应用添加到权限使用例外名单中。例如相机权限被禁用时，A应用实际未申请相机权限，则不能添加A应用到相机权限使用例外名单中，返回错误码9200012。可以通过
> [bm dump](../../../tools/bm-tool.md#查询应用信息命令dump)命令查询应用是否申请指定权限。
> 
> 3.当指定权限通过[setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setdisallowedpermission)接口取消禁用后，该权限对应的权限使用例外名单会同步清理。
> 
> 4.所有用户下单个权限最多可以设置1024个应用到权限使用例外名单。
> 
> 5.系统应用和普通应用都可以添加。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void--><!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| permission | string | Yes | 权限名称。 |
| applicationInstance | common.ApplicationInstance | Yes | 需添加到权限使用例外名单的应用实例信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 9201044 | This permission is not disallowed. Applications cannot be added to or removed from the trustlist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9201015 | The application is not installed. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { securityManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let permission: string = 'ohos.permission.CAMERA';
let disallow: boolean = true;
let accountId: number = 100;
// The application has requested the ohos.permission.CAMERA permission.
let appInstance: common.ApplicationInstance = {
  appIdentifier: '123456789',
  appIndex: 0,
  accountId: 100
};
try {
  // Disable the ohos.permission.CAMERA permission.
  securityManager.setDisallowedPermission(wantTemp, permission, disallow, accountId);
  // Set a specified application to continue using the ohos.permission.CAMERA permission.
  securityManager.addAllowedPermissionBundle(wantTemp, permission, appInstance);
  console.info(`Succeeded in adding allowed permission bundle.`);
} catch(err) {
  console.error(`Failed to add allowed permission bundle. Code: ${err.code}, message: ${err.message}`);
}
```

