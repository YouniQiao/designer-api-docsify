# getPermissionUsedTypeInfos (System API)

## getPermissionUsedTypeInfos

```TypeScript
function getPermissionUsedTypeInfos(
    tokenId?: int | null,
    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>
```

Obtains information about how a sensitive permission is used by an application.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedTypeInfos(    tokenId?: int | null,    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>--><!--Device-privacyManager-function getPermissionUsedTypeInfos(    tokenId?: int | null,    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenId | ArkTS-Dyn: number \| null  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int \| null | No | Application identity identifier for accessing sensitive permissions. It can be obtained through the [accessTokenId]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_field of ApplicationInfo. Pass a specific tokenId when querying the access type information of sensitive permissions for a particular app; 0 or null indicates querying the access type information of sensitive permissions for all apps. Starting from API version 20, the null type is newly supported.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Default value: 0. |
| permissionName | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Name of the sensitive permission being accessed. Pass a specific permission name when querying the access type information of a particular sensitive permission; empty indicates querying the access type information of all sensitive permissions. Passing an invalid value returns error code 12100001.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_Value constraint: The permission name length cannot exceed 256 characters. Default value: Empty string. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PermissionUsedTypeInfo&gt;&gt; | Promise used to return the list of permission access type |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission"ohos.permission.PERMISSION\_\_\_ESCAPED\_UNDERSCORE\_\_\_USED\_\_\_ESCAPED\_UNDERSCORE\_\_\_STATS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. PermissionName exceeds 256 characters. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The input tokenId does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The input permissionName does not exist. |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |

**Example**

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenId: number = 0; // You can use bundleManager.getApplicationInfo to obtain accessTokenId.
let permissionName: Permissions = 'ohos.permission.CAMERA';
// Without any parameter.
privacyManager.getPermissionUsedTypeInfos().then(() => {
  console.info('getPermissionUsedTypeInfos success');
}).catch((err: BusinessError) => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in tokenId only.
privacyManager.getPermissionUsedTypeInfos(tokenId).then(() => {
  console.info('getPermissionUsedTypeInfos success');
}).catch((err: BusinessError) => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in permissionName only.
privacyManager.getPermissionUsedTypeInfos(null, permissionName).then(() => {
  console.info('getPermissionUsedTypeInfos success');
}).catch((err: BusinessError) => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in tokenId and permissionName.
privacyManager.getPermissionUsedTypeInfos(tokenId, permissionName).then(() => {
  console.info('getPermissionUsedTypeInfos success');
}).catch((err: BusinessError) => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
```

