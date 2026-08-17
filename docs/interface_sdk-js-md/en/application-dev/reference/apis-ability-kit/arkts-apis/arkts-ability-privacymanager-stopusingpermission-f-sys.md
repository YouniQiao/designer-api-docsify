# stopUsingPermission (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'privacyManager';
```

## stopUsingPermission

```TypeScript
function stopUsingPermission(tokenID: int, permissionName: Permissions): Promise<void>
```

A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result. This API must be used in conjunction with [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api).

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function stopUsingPermission(tokenID: int, permissionName: Permissions): Promise<void>--><!--Device-privacyManager-function stopUsingPermission(tokenID: int, permissionName: Permissions): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to stop using. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, or the type of the specified tokenID is not of the application type. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is not used in pair with 'startUsingPermission'. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // You can use getApplicationInfo to obtain accessTokenId.
privacyManager.stopUsingPermission(tokenID, 'ohos.permission.READ_AUDIO').then(() => {
  console.info('stopUsingPermission success');
}).catch((err: BusinessError) => {
  console.error(`stopUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
```


## stopUsingPermission

```TypeScript
function stopUsingPermission(tokenID: int, permissionName: Permissions, callback: AsyncCallback<void>): void
```

A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses an asynchronous callback to return the result. This API must be used in conjunction with [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api).

**Since:** 23

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function stopUsingPermission(tokenID: int, permissionName: Permissions, callback: AsyncCallback<void>): void--><!--Device-privacyManager-function stopUsingPermission(tokenID: int, permissionName: Permissions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to stop using. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, or the type of the specified tokenID is not of the application type. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is not used in pair with 'startUsingPermission'. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // You can use getApplicationInfo to obtain accessTokenId.
privacyManager.stopUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', (err: BusinessError, data: void) => {
  if (err) {
    console.error(`stopUsingPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('stopUsingPermission success');
  }
});
```


## stopUsingPermission

```TypeScript
function stopUsingPermission(
    tokenID: int,
    permissionName: Permissions,
    pid?: int,
    options?: PermissionUsingOptions
  ): Promise<void>
```

A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result. The PID must be the same as the PID passed in [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api).

**Since:** 26.0.0

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function stopUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int,    options?: PermissionUsingOptions  ): Promise<void>--><!--Device-privacyManager-function stopUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int,    options?: PermissionUsingOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to stop using. Passing an invalid value returns error code 12100001. |
| pid | int | No | Process ID of the caller, which must be the same as the pid passed in [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api). Failure to meet the matching relationship may cause the API call to fail (error code 12100004). <br>The value should be an integer. Default value: -1, indicating no response based on the process lifecycle. |
| options | [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) | No | Optional parameter for permission usage, used to specify the extension identity. This parameter is passed in when the caller's extension identity information needs to be identified. <br>Default value: Please refer to [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md#permissionusingoptions-system-api) for the default values of each property in the structure. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, the type of the specified tokenID is not of the application type, or the enhancedIdentity in PermissionUsingOptions exceeds 48 characters. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is not used in pair with 'startUsingPermission'. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |


## stopUsingPermission

```TypeScript
function stopUsingPermission(
    tokenID: int,
    permissionName: Permissions,
    pid?: int
  ): Promise<void>
```

A system application calls this API to mark that the specified permission is no longer in use. After a successful call, the privacy service notifies all subscribers of this permission usage status change event of this status change. It is suitable for notifying the system that permission usage has ended when an application completes a sensitive operation or exits the foreground. This API uses a promise to return the result. The pid must be the same as the pid passed into [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api).

**Since:** 23

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function stopUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int  ): Promise<void>--><!--Device-privacyManager-function stopUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int  ): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to stop using. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| pid | int | No | Process PID of the caller. Must be the same as the pid passed to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startusingpermission-system-api). A mismatch may cause the API call to fail (error code 12100004). <br>The value should be an integer. Default value: -1, indicating no response based on process lifecycle. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters, or the type of the specified tokenID is not of the application type. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is not used in pair with 'startUsingPermission'. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit'

let tokenID: number = rpc.IPCSkeleton.getCallingTokenId(); // accessTokenId can also be obtained by using getApplicationInfo.
let pid: number = rpc.IPCSkeleton.getCallingPid();

// without pid
privacyManager.stopUsingPermission(tokenID, 'ohos.permission.READ_AUDIO').then(() => {
  console.info('stopUsingPermission success');
}).catch((err: BusinessError) => {
  console.error(`stopUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});

// with pid
privacyManager.stopUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid).then(() => {
  console.info('stopUsingPermission success');
}).catch((err: BusinessError) => {
  console.error(`stopUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

