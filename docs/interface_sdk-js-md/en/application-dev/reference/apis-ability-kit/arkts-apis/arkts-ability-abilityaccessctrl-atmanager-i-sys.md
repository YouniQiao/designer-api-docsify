# AtManager

Program access control management class, providing capabilities such as permission verification, runtime permission dialog box request, settings page authorization guidance, global switch request, and permission status monitoring. Obtain an instance through [createAtManager](arkts-ability-abilityaccessctrl-createatmanager-f.md).

**Since:** 23

<!--Device-abilityAccessCtrl-interface AtManager--><!--Device-abilityAccessCtrl-interface AtManager-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
```

## getPermissionFlags

```TypeScript
getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>
```

Obtains the flags of a specified permission for a specified app. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS or ohos.permission.GRANT_SENSITIVE_PERMISSIONS or ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>--><!--Device-AtManager-getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to query. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the queried permission flag value. For details about the meaning of the flag value, see the description of the grantFlags field in [PermissionStatusInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission specified below. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not declared in the module.json file. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The operation is not allowed. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
atManager.getPermissionFlags(tokenID, 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS').then((data: number) => {
  console.info(`getPermissionFlags success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`getPermissionFlags fail, code: ${err.code}, message: ${err.message}`);
});
```

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>
```

Obtains the toggle state of a permission. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>--><!--Device-AtManager-getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission whose pop-up switch status is to be queried. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md)&gt; | Promise used to return the toggle status of the dialog box for the specified permission. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission specified below. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionName exceeds 256 characters, or the specified permission is not a user_grant permission. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | This API must be used together with [setPermissionRequestToggleStatus](#setpermissionrequesttogglestatus).<br>**Applicable version:** 26.1.0 and later |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager = abilityAccessCtrl.createAtManager();
let permission: Permissions = 'ohos.permission.CAMERA';

atManager.getPermissionRequestToggleStatus(permission).then((res) => {
  if (res == abilityAccessCtrl.PermissionRequestToggleStatus.CLOSED) {
    console.info('getPermissionRequestToggleStatus: The toggle status is close');
  } else {
    console.info('getPermissionRequestToggleStatus: The toggle status is open');
  }
}).catch((err: BusinessError) => {
console.error(`getPermissionRequestToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(
      permissionName: Permissions,
      subProfileId: int): Promise<PermissionRequestToggleStatus>
```

Obtains the permission dialog toggle status for a specified permission under a specified sub-profile. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-getPermissionRequestToggleStatus(      permissionName: Permissions,      subProfileId: int): Promise<PermissionRequestToggleStatus>--><!--Device-AtManager-getPermissionRequestToggleStatus(      permissionName: Permissions,      subProfileId: int): Promise<PermissionRequestToggleStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission whose pop-up switch status is to be queried. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| subProfileId | int | Yes | ID of the sub-profile. It can be obtained from [OsAccountSubProfile.id](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id). <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md)&gt; | Promise used to return the toggle status of the dialog box for the specified permission. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission specified below. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, or the specified subProfileId does not exist for the current user. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |

## getPermissionsStatus

```TypeScript
getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>
```

Obtains the status of the specified permissions. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>--><!--Device-AtManager-getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names for which the permission status is to be obtained. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024 and cannot be empty. Value constraint: The permission name length cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[PermissionStatus](arkts-ability-abilityaccessctrl-permissionstatus-e.md)&gt;&gt; | Promise used to return the list of queried permission statuses. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0 or the permissionList is empty or exceeds the size limit. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
atManager.getPermissionsStatus(tokenID, ['ohos.permission.CAMERA']).then((data: Array<abilityAccessCtrl.PermissionStatus>) => {
  console.info(`getPermissionsStatus success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`getPermissionsStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## getVersion

```TypeScript
getVersion(): Promise<int>
```

Obtains the data version number of the current permission management. This API uses a promise to return the result.

**Since:** 23

<!--Device-AtManager-getVersion(): Promise<int>--><!--Device-AtManager-getVersion(): Promise<int>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the version number queried. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let promise = atManager.getVersion();
promise.then((data: number) => {
    console.info(`getVersion promise: data->${data}`);
});
```

## grantPermission

```TypeScript
grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

Grants an app permission. After the call is successful, the specified app obtains the permission and can access the corresponding protected resources. Unlike [grantUserGrantedPermission](#grantusergrantedpermission), which only supports permissions of the user_grant type, this API supports granting permissions of both the user_grant and manual_settings types. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to grant. The permission name cannot exceed 256 characters. If the limit is exceeded, error code 12100001 is returned. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in the permission management page of system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this time. The authorization is revoked when the app switches to the background or exits. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) | Unexpected permission. The specified permission is not a user_grant or manual_settings permission. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // System applications can obtain the token ID using bundleManager.getApplicationInfo.
let permissionFlags: number = 2;
atManager.grantPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('grantPermission success');
}).catch((err: BusinessError) => {
  console.error(`grantPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## grantUserGrantedPermission

```TypeScript
grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

Grants a user_grant permission to an app. After the call is successful, the app obtains the user_grant permission and can access the corresponding protected resources. This API uses a promise to return the result.

This API only supports granting permissions of the user_grant type. If you need to grant permissions of the user_grant or manual_settings type, you are advised to use [grantPermission](#grantpermission).

**Since:** 23

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to grant. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name cannot exceed 256 characters. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in the permission management page of system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this session. The authorization is revoked when the app switches to the background or exits. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
let permissionFlags: number = 1;
atManager.grantUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('grantUserGrantedPermission success');
}).catch((err: BusinessError) => {
  console.error(`grantUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## grantUserGrantedPermission

```TypeScript
grantUserGrantedPermission(
        tokenID: int,
        permissionName: Permissions,
        permissionFlags: int,
        callback: AsyncCallback<void>
    ): void
```

Grants a user_grant permission to an app. This API uses an asynchronous callback to return the result. After the call is successful, the app obtains the user_grant permission and can access the corresponding protected resources.

**Since:** 23

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void--><!--Device-AtManager-grantUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to grant. The permission name cannot exceed 256 characters. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this session. The authorization is revoked when the app switches to the background or exits. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the permission grant is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
let permissionFlags: number = 1;
atManager.grantUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`grantUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('grantUserGrantedPermission success');
  }
});
```

## offPermissionStateChange

```TypeScript
offPermissionStateChange(
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

Unsubscribes from changes in the state of the specified permissions for the token ID list and permission list. This API uses an asynchronous callback to return the result.

When unsubscribing, if no callback is passed in, all listening callbacks that completely match the tokenIDList and permissionList will be unsubscribed in batches.

> **NOTE：**
> This API is usually used together with
> [onPermissionStateChange](#onpermissionstatechange)
> to cancel the listening relationship created by onPermissionStateChange.

**Since:** 23

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-offPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-offPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | Array&lt;int&gt; | Yes | List of token IDs to unsubscribe from. If this parameter is left empty, it indicates unsubscribing from permission state changes of all apps. This parameter must be consistent with the input of [onPermissionStateChange](#onpermissionstatechange). The app identity can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each token ID in the list must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to unsubscribe from. If this parameter is left empty, it indicates unsubscribing from all permission state changes. This parameter must be consistent with the input of [onPermissionStateChange](#onpermissionstatechange). Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each permission name in the list must be a valid permission name, and its length cannot exceed 256 characters. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | No | Callback used to return the object for unsubscribing from state change events of the specified tokenID and permission name. This callback must be consistent with the callback registered in [onPermissionStateChange](#onpermissionstatechange). If this parameter is not passed, all listener callbacks that exactly match tokenIDList and permissionList will be canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenIDList or permissionList is not in the listening list. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

## off('permissionStateChange')

```TypeScript
off(
      type: 'permissionStateChange',
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

Unsubscribes from changes in the state of the specified permissions for the token ID list and permission list. This API uses an asynchronous callback to return the result.

When unsubscribing, if no callback is passed in, all listening callbacks that completely match the tokenIDList and permissionList will be unsubscribed in batches.

This API is usually used together with [on](#onpermissionstatechange) to cancel the listening relationship created by on.

**Since:** 9

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-off(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-off(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'permissionStateChange' | Yes | Event type. The value is **'permissionStateChange'**, which indicates the permission state changes. |
| tokenIDList | Array&lt;int&gt; | Yes | List of token IDs to unsubscribe from. If this parameter is left empty, it indicates unsubscribing from permission state changes of all apps. This parameter must be consistent with the input of [on](#onpermissionstatechange). The app identity can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each token ID in the list must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to unsubscribe from. If this parameter is left empty, it indicates unsubscribing from all permission state changes. This parameter must be consistent with the input of [on](#onpermissionstatechange). Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each permission name in the list must be a valid permission name, and its length cannot exceed 256 characters. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | No | Callback used to return the object for unsubscribing from state change events of the specified tokenID and permission name. This callback must be consistent with the callback registered in [on](#onpermissionstatechange). If this parameter is not passed, all listener callbacks that exactly match tokenIDList and permissionList will be canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenIDList or permissionList is not in the listening list. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let appInfo: bundleManager.ApplicationInfo = bundleManager.getApplicationInfoSync('com.example.myapplication', 0, 100);
let tokenIDList: Array<number> = [appInfo.accessTokenId];
let permissionList: Array<Permissions> = ['ohos.permission.DISTRIBUTED_DATASYNC'];
try {
    atManager.off('permissionStateChange', tokenIDList, permissionList);
} catch(err) {
    console.error(`catch errcode: ${err.code}, message: ${err.message}`);
}
```

## onPermissionStateChange

```TypeScript
onPermissionStateChange(
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

Subscribes to changes in the state of specified permissions for the given applications. This API uses an asynchronous callback to return the result.

Multiple callbacks can be registered for the specified **tokenIDList** and **permissionList**.

> **NOTE：**
> If a new subscription overlaps with an existing subscription in terms of the tokenID list and permission list,
> the same callback cannot be used for subscription.
> This API is usually used together with
> [offPermissionStateChange](#offpermissionstatechange).
> When listening is no longer needed, offPermissionStateChange should be called to unsubscribe.

**Since:** 23

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-onPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-onPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | Array&lt;int&gt; | Yes | List of token IDs to subscribe to. If left empty, it subscribes to permission status changes of all apps. The app identity can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each token ID in the list must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to subscribe to. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each permission name in the list must be a valid permission name, and its length cannot exceed 256 characters. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | Yes | Callback used to return the result. Callback for subscribing to the status change events of the specified tokenID and permission name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. Possible causes: 1. The tokenIDList or permissionList exceeds the size limit; 2. The tokenIDs or permissionNames in the list are all invalid. |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) | The registration time has exceeded the limit. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |

## on('permissionStateChange')

```TypeScript
on(
      type: 'permissionStateChange',
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

Subscribes to changes in the state of specified permissions for the given applications. This API uses an asynchronous callback to return the result.

Multiple callbacks can be registered for the specified **tokenIDList** and **permissionList**.

If a new subscription overlaps with an existing subscription in terms of the tokenID list and permission list, the same callback cannot be used for subscription.

This API is usually used together with [off](#offpermissionstatechange). When listening is no longer needed, off should be called to unsubscribe.

**Since:** 9

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-on(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-on(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'permissionStateChange' | Yes | Event type. The value is **'permissionStateChange'**, which indicates the permission state changes. |
| tokenIDList | Array&lt;int&gt; | Yes | List of token IDs to subscribe to. If left empty, it subscribes to permission status changes of all apps. The app identity can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024. Value constraint: Each token ID in the list must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to subscribe to. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024 and cannot be empty. Value constraint: Each permission name in the list must be a valid permission name, and its length cannot exceed 256 characters. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | Yes | Callback used to return the result. Callback for subscribing to the status change events of the specified tokenID and permission name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. Possible causes: 1. The tokenIDList or permissionList exceeds the size limit; 2. The tokenIDs or permissionNames in the list are all invalid. |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) | The registration time has exceeded the limit. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let appInfo: bundleManager.ApplicationInfo = bundleManager.getApplicationInfoSync('com.example.myapplication', 0, 100);
let tokenIDList: Array<number> = [appInfo.accessTokenId];
let permissionList: Array<Permissions> = ['ohos.permission.DISTRIBUTED_DATASYNC'];
try {
    atManager.on('permissionStateChange', tokenIDList, permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
        console.debug(`receive permission state change, data: ${data}`);
    });
} catch(err) {
    console.error(`catch errcode: ${err.code}, message: ${err.message}`);
}
```

## queryStatusByPermission

```TypeScript
queryStatusByPermission(
      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>
```

Queries all apps that have requested the specified permissions and their permission statuses based on the permission list. This API uses a promise to return the result. When the size of the queried data result exceeds 50000 entries, the API directly returns error code 12100015.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-queryStatusByPermission(      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>--><!--Device-AtManager-queryStatusByPermission(      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to query. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024 and cannot be empty. Value constraint: The permission name length cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[PermissionStatusInfo](arkts-ability-abilityaccessctrl-permissionstatusinfo-i-sys.md)&gt;&gt; | Promise used to return the list of queried permission status information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. Interface caller is not a system application. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionList is empty or exceeds the size limit. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| 12100015 | The queried data exceeds the upper limit. |

## queryStatusByTokenID

```TypeScript
queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>
```

Queries all permission statuses of an app based on its tokenID list. This API uses a promise to return the result. When the size of the queried data result exceeds 50000 entries, the API directly returns error code 12100015.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>--><!--Device-AtManager-queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | Array&lt;int&gt; | Yes | List of app token IDs to query. The app identity can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The maximum length is 1024 and cannot be empty. Value constraint: Each token ID in the list must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[PermissionStatusInfo](arkts-ability-abilityaccessctrl-permissionstatusinfo-i-sys.md)&gt;&gt; | Promise used to return the list of queried permission status information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. Interface caller is not a system application. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenIDList is empty or exceeds the size limit. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| 12100015 | The queried data exceeds the upper limit. |

## requestPermissionOnApplicationSetting

```TypeScript
requestPermissionOnApplicationSetting(tokenID: int): Promise<void>
```

Starts the permission settings page for an application. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-requestPermissionOnApplicationSetting(tokenID: int): Promise<void>--><!--Device-AtManager-requestPermissionOnApplicationSetting(tokenID: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
atManager.requestPermissionOnApplicationSetting(tokenID).then(() => {
  console.info('requestPermissionOnApplicationSetting success');
}).catch((err: BusinessError) => {
  console.error(`requestPermissionOnApplicationSetting fail, code: ${err.code}, message: ${err.message}`);
});
```

## requestPermissionsFromUserWithWindowId

```TypeScript
requestPermissionsFromUserWithWindowId(
        context: Context,
        windowId: int,
        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

Pops up a dialog based on the window ID to request user authorization. After the call is successful, the permission request result object is returned. Developers can continue the business process after window-level authorization based on the permission request result. This API uses a promise to return the result.

This is applicable to scenarios where a system app needs to explicitly attach the permission request dialog to a specified window.

If the user denies authorization, the dialog cannot be pulled up again. Permission can be re-obtained in the following ways: 1. Manually authorize in the system settings. 2. Call [requestPermissionOnSetting](arkts-ability-abilityaccessctrl-atmanager-i.md#requestpermissiononsetting) to pull up the permission settings dialog to guide the user to authorize.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-requestPermissionsFromUserWithWindowId(        context: Context,        windowId: int,        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>--><!--Device-AtManager-requestPermissionsFromUserWithWindowId(        context: Context,        windowId: int,        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes | Context of the UIAbility or UIExtensionAbility requesting the permission. If the context of another app, an invalid page, or a non-stage model is passed in, the API may report an error or fail to display the dialog box. |
| windowId | int | Yes | ID of the app window. It can be obtained through [window.findWindow](../../apis-arkui/arkts-apis/arkts-arkui-window-findwindow-f.md)(window name). [getWindowProperties()](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#getwindowproperties).id. This parameter must correspond to the current valid window. If a destroyed, invisible, or invalid window ID is passed in, 12100001 will be returned. <br>The value should be an integer. |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names. It is recommended that you pass in only the sensitive permissions that are actually required in the current window scenario. <br>The minimum length is 1. Value constraint: The length of a permission name in array cannot exceed 256 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; | Promise used to return the result of this permission request, including the permission array, grant result, whether to show a dialog box, and failure reason. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. windowId is invalid. |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) | Common inner error. An error occurs when creating the popup window or obtaining the user operation result. |

**Examples**

For details about how to obtain the context in the example, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).For details about the process and example of applying for user authorization, see [Requesting User Authorization](../../../security/AccessToken/request-user-authorization.md).

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let context: Context = this.getUIContext().getHostContext() as Context;
let windowId = 0; // *Obtaining method* let windowId = window.findWindow(*window name*).getWindowProperties().id;
atManager.requestPermissionsFromUserWithWindowId(context, windowId, ['ohos.permission.CAMERA']).then((data: PermissionRequestResult) => {
  console.info(`requestPermissionsFromUserWithWindowId success, result: ${data}`);
  console.info('requestPermissionsFromUserWithWindowId data permissions:' + data.permissions);
  console.info('requestPermissionsFromUserWithWindowId data authResults:' + data.authResults);
  console.info('requestPermissionsFromUserWithWindowId data dialogShownResults:' + data.dialogShownResults);
  console.info('requestPermissionsFromUserWithWindowId data errorReasons:' + data.errorReasons);
}).catch((err: BusinessError) => {
  console.error(`requestPermissionsFromUserWithWindowId fail, code: ${err.code}, message: ${err.message}`);
});
```

## revokePermission

```TypeScript
revokePermission(
      tokenID: int,
      permissionName: Permissions,
      permissionFlags: int,
      killProcess?: boolean): Promise<void>
```

Revokes an app permission. After the call is successful, the app loses the permission and cannot access the corresponding protected resources. Whether to terminate the app process is determined by the value of the killProcess parameter. This API uses a promise to return the result.

When the killProcess parameter is true and the permission status changes from "authorized" to "unauthorized", the app process will be terminated.

**Since:** 23

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokePermission(      tokenID: int,      permissionName: Permissions,      permissionFlags: int,      killProcess?: boolean): Promise<void>--><!--Device-AtManager-revokePermission(      tokenID: int,      permissionName: Permissions,      permissionFlags: int,      killProcess?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to be revoked. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in the permission management of system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this session. The authorization is revoked when the app switches to the background or exits. |
| killProcess | boolean | No | Whether to terminate the app process. <br>- **true**: Terminate the app process. <br>- **false**: Do not terminate the app process. <br>- Default value: **true**.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. The interface invoker does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not a system application. The interface invoker is not a system application. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The token ID is 0, the permission name exceeds 256 characters or is not declared in the module.json file, or the value of flags is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The specified permission is not allowed to be revoked from the application specified by the tokenID. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) | Unexpected permission. The specified permission is not a user_grant or manual_settings permission. |

## revokeUserGrantedPermission

```TypeScript
revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

Revokes a user_grant permission from an app. After the call is successful, the app loses the user_grant permission and cannot access the corresponding protected resources. This API uses a promise to return the result.

This API only supports revoking permissions of the user_grant type and does not support controlling whether to terminate the app process. If you need to revoke permissions of the user_grant or manual_settings type, or need to control whether to terminate the app process after revoking the permission, you are advised to use [revokePermission](#revokepermission).

When the permission status changes from "authorized" to "unauthorized", the app process will be terminated.

**Since:** 23

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to be revoked. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in the permission management page of system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this session. The authorization is revoked when the app switches to the background or exits. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The application specified by the tokenID is not allowed to be revoked with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
let permissionFlags: number = 1;
atManager.revokeUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('revokeUserGrantedPermission success');
}).catch((err: BusinessError) => {
  console.error(`revokeUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## revokeUserGrantedPermission

```TypeScript
revokeUserGrantedPermission(
        tokenID: int,
        permissionName: Permissions,
        permissionFlags: int,
        callback: AsyncCallback<void>
    ): void
```

Revokes a user_grant permission from an app. This API uses an asynchronous callback to return the result. After the call is successful, the app loses the user_grant permission and cannot access the corresponding protected resources.

**Since:** 23

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokeUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void--><!--Device-AtManager-revokeUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | int | Yes | Identity identifier of the target application. It can be obtained through the [accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid) field in ApplicationInfo of BundleInfo. Passing an invalid value returns error code 12100001. <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. <br>For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md). |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission to be revoked. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| permissionFlags | int | Yes | Authorization options. <br>The value should be an integer. <br>- 1: If the user denies the permission this time, the permission dialog box can still be displayed the next time to request user authorization. <br>- 2: If the user denies the permission this time, the permission dialog box will not be displayed again. The user needs to grant the permission in the permission management page of system settings. <br>- 64: If the user selects to allow only this time, the permission is granted only for this session. The permission is revoked after the app switches to the background or exits. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the permission revocation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) | The specified tokenID does not exist. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist or is not a user_grant permission. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | The application specified by the tokenID is not allowed to be revoked with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

**Examples**

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // Use bundleManager.getApplicationInfo() to obtain the token ID for a system application, and use bundleManager.getBundleInfoForSelf() to obtain the token ID for a non-system application.
let permissionFlags: number = 1;
atManager.revokeUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`revokeUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('revokeUserGrantedPermission success');
  }
});
```

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>
```

Sets the dialog toggle status for a specified permission of the current user. After the call is successful, the dialog toggle status of the permission will be set to the specified value. When the status is CLOSED, no permission dialog will pop up when the app requests the permission. When the status is OPEN, the permission dialog will pop up normally when the app requests the permission. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

<!--Device-AtManager-setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>--><!--Device-AtManager-setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission for which the dialog box switch status is to be set. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes | Toggle state to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission specified below. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, or the status value is invalid. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionRequestToggleStatus](#setpermissionrequesttogglestatus).<br>**Applicable version:** 26.1.0 and later |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |

**Examples**

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager = abilityAccessCtrl.createAtManager();
let permission: Permissions = 'ohos.permission.CAMERA';

atManager.setPermissionRequestToggleStatus(permission, abilityAccessCtrl.PermissionRequestToggleStatus.CLOSED).then((err) => {
  console.info('setPermissionRequestToggleStatus: set closed successful');
}).catch((err: BusinessError) => {
  console.error(`setPermissionRequestToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(
      permissionName: Permissions,
      status: PermissionRequestToggleStatus,
      subProfileId: int): Promise<void>
```

Sets the dialog toggle status for a specified permission under a specified sub-profile. After the call is successful, the dialog toggle status of the permission will be set to the specified value. When the status is CLOSED, no permission dialog will pop up when the app requests the permission. When the status is OPEN, the permission dialog will pop up normally when the app requests the permission. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-setPermissionRequestToggleStatus(      permissionName: Permissions,      status: PermissionRequestToggleStatus,      subProfileId: int): Promise<void>--><!--Device-AtManager-setPermissionRequestToggleStatus(      permissionName: Permissions,      status: PermissionRequestToggleStatus,      subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | Name of the permission for which the dialog box switch status is to be set. Passing an invalid value returns error code 12100001. <br>Value constraint: The permission name length cannot exceed 256 characters. |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes | Toggle state to set. |
| subProfileId | int | Yes | ID of the sub-profile. It can be obtained from [OsAccountSubProfile.id](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id). <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission specified below. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, the status value is invalid, or the specified subProfileId does not exist for the current user. |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) | The specified permission does not exist. |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionRequestToggleStatus](#setpermissionrequesttogglestatus). |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) | Common inner error. A database error occurs. |

