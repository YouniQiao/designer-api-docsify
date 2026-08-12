# addPermissionUsedRecord (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
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

When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses a promise to return the result.

The permission usage record includes the application identity of the caller, the name of the application permission,and the number of successful and failed accesses to this application by the caller.

> **NOTE：**
> The permission usage record is controlled by the toggle status set by [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus). When the toggle is off, calling this API will not generate a
permission usage record.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accessTokenId) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: This parameter must be an integer greater than 0. &lt;br&gt;For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getBundleInfoSync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to be recorded. Passing an invalid value returns error code 12100001. &lt;br&gt;Value constraint: The permission name length cannot exceed 256 characters. |
| successCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of successful accesses. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: The value must be a non-negative integer. |
| failCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of failed accesses. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: The value must be a non-negative integer. |
| options | [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) | No | Optional parameter for adding a permission usage record, used to specify the sensitive permission usage type and extension identity. Pass this parameter when you need to distinguish the permission access method (such as access via Picker or security control) or identify the caller's extension identity.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12100009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, the count value is invalid, usedType in AddPermissionUsedRecordOptions is invalid, or the enhancedIdentity in AddPermissionUsedRecordOptions exceeds 48 characters. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist or refer to an application process. |
| [12100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // You can use getApplicationInfo to obtain accessTokenId.
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError) => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
// with options param
let options: privacyManager.AddPermissionUsedRecordOptions = {
  usedType: privacyManager.PermissionUsedType.PICKER_TYPE
};
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, options).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError) => {
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

When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses an asynchronous callback to return the result.

The permission usage record includes the application identity of the caller, the name of the application permission used, and the number of successful and failed accesses to this application by the caller.

The permission usage record is controlled by the toggle status set by  
[setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus). When the toggle is off, calling this API will not generate a permission usage record.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accessTokenId) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: This parameter must be an integer greater than 0. &lt;br&gt;For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getBundleInfoSync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to be recorded. Passing an invalid value returns error code 12100001. &lt;br&gt;Value constraint: The permission name length cannot exceed 256 characters. |
| successCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of successful accesses. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: The value must be a non-negative integer. |
| failCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of failed accesses. Passing an invalid value returns error code 12100001. &lt;br&gt;The value should be an integer. Value constraint: The value must be a non-negative integer. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12100009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, or the count value is invalid. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist or refer to an application process. |
| [12100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // You can use getApplicationInfo to obtain accessTokenId.
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('addPermissionUsedRecord success');
  }
});
```

