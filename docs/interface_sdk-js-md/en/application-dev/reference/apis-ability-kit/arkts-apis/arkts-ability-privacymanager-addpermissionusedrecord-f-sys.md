# addPermissionUsedRecord (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: int,
    permissionName: Permissions,
    successCount: int,
    failCount: int,
    options?: AddPermissionUsedRecordOptions
  ): Promise<void>
```

受权限保护的应用在被其他服务、应用调用时，可以使用该接口增加一条权限使用记录。建议在访问敏感权限后调用此接口，以便系统记录对应的敏感权限访问事件。使用Promise异步回调。

权限使用记录包括：调用方的应用身份标识、使用的应用权限名称，以及调用方访问本应用成功和失败的次数。

权限使用记录受[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus)设置的开关状态控制。开关关闭时，调用此接口不会产生权限使用记录。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 需要记录的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| successCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 访问成功的次数。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：取值必须为非负整数。 |
| failCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 访问失败的次数。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：取值必须为非负整数。 |
| options | [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) | No | 添加权限使用记录可选参数，用于指定敏感权限使用类型和扩展身份。当需要区分权限访问方式（如通过Picker或安全控件访问）或标识调用方扩展身份时传入此参数。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100008 | Out of memory. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, the count value is invalid, usedType in AddPermissionUsedRecordOptions is invalid, or the enhancedIdentity in AddPermissionUsedRecordOptions exceeds 48 characters. |
| 202 | Not system app. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist or refer to an application process. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // Obtained from the accessTokenId field of ApplicationInfo in the BundleInfo of the application.
// Add permission usage record
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
// with options param
let options: privacyManager.AddPermissionUsedRecordOptions = {
  usedType: privacyManager.PermissionUsedType.PICKER_TYPE,
  enhancedIdentity: 'test'
};
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, options).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
```


## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: int,
    permissionName: Permissions,
    successCount: int,
    failCount: int,
    callback: AsyncCallback<void>
  ): void
```

受权限保护的应用在被其他服务、应用调用时，可以使用该接口增加一条权限使用记录。建议在访问敏感权限后调用此接口，以便系统记录对应的敏感权限访问事件。使用callback异步回调。

权限使用记录包括：调用方的应用身份标识、使用的应用权限名称，以及调用方访问本应用成功和失败的次数。

权限使用记录受[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus)设置的开关状态控制。开关关闭时，调用此接口不会产生权限使用记录。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 需要记录的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| successCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 访问成功的次数。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：取值必须为非负整数。 |
| failCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 访问失败的次数。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：取值必须为非负整数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当添加使用记录成功时，err为undefined；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100008 | Out of memory. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, or the count value is invalid. |
| 202 | Not system app. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist or refer to an application process. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // Obtained from the accessTokenId field of ApplicationInfo in the BundleInfo of the application.
// Add permission usage record
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('addPermissionUsedRecord success');
  }
});
```

