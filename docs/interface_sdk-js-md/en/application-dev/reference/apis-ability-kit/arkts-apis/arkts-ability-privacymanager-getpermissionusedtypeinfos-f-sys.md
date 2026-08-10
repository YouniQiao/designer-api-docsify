# getPermissionUsedTypeInfos (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedTypeInfos

```TypeScript
function getPermissionUsedTypeInfos(
    tokenId?: int | null,
    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>
```

查询设备上指定应用访问敏感权限时的信息（包括敏感权限名称、敏感权限访问方式）。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedTypeInfos(    tokenId?: int | null,    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>--><!--Device-privacyManager-function getPermissionUsedTypeInfos(    tokenId?: int | null,    permissionName?: Permissions): Promise<Array<PermissionUsedTypeInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenId | ArkTS-Dyn: number \| null  <br>ArkTS-Sta：int \| null | No | 访问敏感权限的应用身份标识。可通过应用[BundleInfo](arkts-ability-bundleinfo-i.md)中的 [ApplicationInfo](arkts-ability-applicationinfo-i.md)的accessTokenId字段获取。当需要查询特定应用的敏感权限访问类型信息 时传入具体的tokenId；为0或null时表示查询所有应用的敏感权限访问类型信息。从API version 20开始，新增支持null类型。 &lt;br&gt;默认值：0。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | No | 被访问的敏感权限名称。当需要查询特定敏感权限的访问类型信息时传入具体的权限名；为空时表示查询所有敏感权限的访问类型信息。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。默认值：空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PermissionUsedTypeInfo&gt;&gt; | Promise used to return the list of permission access type information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 12100001 | Invalid parameter. PermissionName exceeds 256 characters. |
| 202 | Not system app. Interface caller is not a system app. |
| 12100002 | The input tokenId does not exist. |
| 12100003 | The input permissionName does not exist. |

## Examples

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenId: number = 0; // Obtained from the accessTokenId field of ApplicationInfo in the BundleInfo of the application.
let permissionName: Permissions = 'ohos.permission.CAMERA';
// Without any parameter.
privacyManager.getPermissionUsedTypeInfos().then((data: Array<privacyManager.PermissionUsedTypeInfo>) => {
  console.info('getPermissionUsedTypeInfos success, result: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in tokenId only.
privacyManager.getPermissionUsedTypeInfos(tokenId).then((data: Array<privacyManager.PermissionUsedTypeInfo>) => {
  console.info('getPermissionUsedTypeInfos success, result: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in permissionName only.
privacyManager.getPermissionUsedTypeInfos(null, permissionName).then((data: Array<privacyManager.PermissionUsedTypeInfo>) => {
  console.info('getPermissionUsedTypeInfos success, result: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
// Pass in tokenId and permissionName.
privacyManager.getPermissionUsedTypeInfos(tokenId, permissionName).then((data: Array<privacyManager.PermissionUsedTypeInfo>) => {
  console.info('getPermissionUsedTypeInfos success, result: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedTypeInfos fail, code: ${err.code}, message: ${err.message}`);
});
```

