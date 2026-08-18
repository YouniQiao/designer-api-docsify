# checkPermissionInUse (System API)

## Modules to Import

```TypeScript
```

## checkPermissionInUse

```TypeScript
function checkPermissionInUse(permissionName: Permissions): boolean
```

Queries whether a specified sensitive permission is currently being used. It can be used in scenarios such as displaying the real-time permission usage status on the permission management interface. The judgment is based on whether there is currently an active call that has been marked as started by [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api) and has not yet been marked as stopped by [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission-system-api).

**Since:** 26.0.0

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function checkPermissionInUse(permissionName: Permissions): boolean--><!--Device-privacyManager-function checkPermissionInUse(permissionName: Permissions): boolean-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

**Examples**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Query whether a specified permission is being used
  let isPermissionInUse = privacyManager.checkPermissionInUse('ohos.permission.CAMERA');
  console.info('checkPermissionInUse success, result: ' + isPermissionInUse);
} catch (err) {
  let error = err as BusinessError;
  console.error(`checkPermissionInUse fail, code: ${error.code}, message: ${error.message}`);
}
```
