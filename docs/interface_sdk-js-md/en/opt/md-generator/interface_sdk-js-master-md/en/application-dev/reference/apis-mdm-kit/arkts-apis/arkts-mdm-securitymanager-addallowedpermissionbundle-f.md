# addAllowedPermissionBundle

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## addAllowedPermissionBundle

```TypeScript
function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void
```

Adds an application to the permission usage exception list. Applications in the list are not subject to the permission restriction policy set via [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission). This API is applicable to enterprise scenarios. For example, when the camera permission is disabled, attendance applications and collaborative office applications can still use the camera, ensuring that critical enterprise business operates normally. > **NOTE：**> > 1. The permission must first be disabled via the > [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission) API before an application can be added > to the permission usage exception list. Otherwise, error code 9201044 is returned. > > 2. An application cannot be added to the permission usage exception list if it has not actually requested the > specified permission. For example, if the camera permission is disabled and application A has not requested the > camera permission, it cannot be added to the exception list for the camera permission, and error code 9200012 is > returned. You can use the [bm dump](../../../tools/bm-tool.md#dump) command to check whether an application has > requested a specific permission. > > 3. When a specified permission is enabled via the > [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission) API, the corresponding permission usage > exception list is cleared synchronously. > > 4. For any given permission, a maximum of 1024 applications can be added to the exception list across all users. > > 5. Both system applications and third-party applications can be added.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void--><!--Device-securityManager-function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void-End-->

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
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201044](../errorcode-enterpriseDeviceManager.md#9201044-specified-permission-not-disabled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9201015](../errorcode-enterpriseDeviceManager.md#9201015-specified-application-not-installed) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

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
