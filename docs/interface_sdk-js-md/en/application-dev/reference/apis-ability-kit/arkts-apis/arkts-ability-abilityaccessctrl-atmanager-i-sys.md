# AtManager

Program access control management class, providing capabilities such as permission verification, runtime permission dialog box request, settings page authorization guidance, global switch request, and permission status monitoring. Obtain an instance through [createAtManager](arkts-ability-abilityaccessctrl-createatmanager-f.md).

**Since:** 8

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult, Permissions } from 'kits/@kit.AbilityKit';
```

## getPermissionFlags

```TypeScript
getPermissionFlags(tokenID: number, permissionName: Permissions): Promise<number>
```

Obtains the flags of a specified permission for a specified app. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS or ohos.permission.GRANT_SENSITIVE_PERMISSIONS or ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>
```

Obtains the toggle state of a permission. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(
      permissionName: Permissions,
      subProfileId: number): Promise<PermissionRequestToggleStatus>
```

Obtains the permission dialog toggle status for a specified permission under a specified sub-profile. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| [subProfileId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |

## getPermissionsStatus

```TypeScript
getPermissionsStatus(tokenID: number, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>
```

Obtains the status of the specified permissions. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PermissionStatus](arkts-ability-abilityaccessctrl-permissionstatus-e.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## getVersion

```TypeScript
getVersion(): Promise<number>
```

Obtains the data version number of the current permission management. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## grantPermission

```TypeScript
grantPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

Grants an app permission. After the call is successful, the specified app obtains the permission and can access the corresponding protected resources. Unlike [grantUserGrantedPermission](#grantusergrantedpermission), which only supports permissions of the user_grant type, this API supports granting permissions of both the user_grant and manual_settings types. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) |

## grantUserGrantedPermission

```TypeScript
grantUserGrantedPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

Grants a user_grant permission to an app. After the call is successful, the app obtains the user_grant permission and can access the corresponding protected resources. This API uses a promise to return the result.This API only supports granting permissions of the user_grant type. If you need to grant permissions of the user_grant or manual_settings type, you are advised to use [grantPermission](#grantpermission).

**Since:** 8

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## grantUserGrantedPermission

```TypeScript
grantUserGrantedPermission(
        tokenID: number,
        permissionName: Permissions,
        permissionFlags: number,
        callback: AsyncCallback<void>
    ): void
```

Grants a user_grant permission to an app. This API uses an asynchronous callback to return the result. After the call is successful, the app obtains the user_grant permission and can access the corresponding protected resources.

**Since:** 8

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## off('permissionStateChange')

```TypeScript
off(
      type: 'permissionStateChange',
      tokenIDList: Array<number>,
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

Unsubscribes from changes in the state of the specified permissions for the token ID list and permission list. This API uses an asynchronous callback to return the result.When unsubscribing, if no callback is passed in, all listening callbacks that completely match the tokenIDList and permissionList will be unsubscribed in batches.This API is usually used together with [on](#onpermissionstatechange) to cancel the listening relationship created by on.

**Since:** 9

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'permissionStateChange' | Yes |
| tokenIDList | Array & lt;number & gt; | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## on('permissionStateChange')

```TypeScript
on(
      type: 'permissionStateChange',
      tokenIDList: Array<number>,
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

Subscribes to changes in the state of specified permissions for the given applications. This API uses an asynchronous callback to return the result.Multiple callbacks can be registered for the specified **tokenIDList** and **permissionList**.If a new subscription overlaps with an existing subscription in terms of the tokenID list and permission list, the same callback cannot be used for subscription.This API is usually used together with [off](#offpermissionstatechange). When listening is no longer needed, off should be called to unsubscribe.

**Since:** 9

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'permissionStateChange' | Yes |
| tokenIDList | Array & lt;number & gt; | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PermissionStateChangeInfo](arkts-ability-abilityaccessctrl-permissionstatechangeinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |

## queryStatusByPermission

```TypeScript
queryStatusByPermission(
      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>
```

Queries all apps that have requested the specified permissions and their permission statuses based on the permission list. This API uses a promise to return the result. When the size of the queried data result exceeds 50000 entries, the API directly returns error code 12100015.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PermissionStatusInfo](arkts-ability-abilityaccessctrl-permissionstatusinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| 12100015 |

## queryStatusByTokenID

```TypeScript
queryStatusByTokenID(tokenIDList: Array<number>): Promise<Array<PermissionStatusInfo>>
```

Queries all permission statuses of an app based on its tokenID list. This API uses a promise to return the result. When the size of the queried data result exceeds 50000 entries, the API directly returns error code 12100015.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenIDList | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PermissionStatusInfo](arkts-ability-abilityaccessctrl-permissionstatusinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| 12100015 |

## requestPermissionOnApplicationSetting

```TypeScript
requestPermissionOnApplicationSetting(tokenID: number): Promise<void>
```

Starts the permission settings page for an application. This API uses a promise to return the result.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## requestPermissionsFromUserWithWindowId

```TypeScript
requestPermissionsFromUserWithWindowId(
        context: Context,
        windowId: number,
        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

Pops up a dialog based on the window ID to request user authorization. After the call is successful, the permission request result object is returned. Developers can continue the business process after window-level authorization based on the permission request result. This API uses a promise to return the result.This is applicable to scenarios where a system app needs to explicitly attach the permission request dialog to a specified window.If the user denies authorization, the dialog cannot be pulled up again. Permission can be re-obtained in the following ways: 1. Manually authorize in the system settings. 2. Call [requestPermissionOnSetting](arkts-ability-abilityaccessctrl-atmanager-i.md#requestpermissiononsetting) to pull up the permission settings dialog to guide the user to authorize.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-t.md) | Yes |
| windowId | number | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-permissionrequestresult-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |

## revokePermission

```TypeScript
revokePermission(
      tokenID: number,
      permissionName: Permissions,
      permissionFlags: number,
      killProcess?: boolean): Promise<void>
```

Revokes an app permission. After the call is successful, the app loses the permission and cannot access the corresponding protected resources. Whether to terminate the app process is determined by the value of the killProcess parameter. This API uses a promise to return the result.When the killProcess parameter is true and the permission status changes from "authorized" to "unauthorized", the app process will be terminated.

**Since:** 21

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |
| killProcess | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100014](../errorcode-access-token.md#12100014-unexpected-permission) |

## revokeUserGrantedPermission

```TypeScript
revokeUserGrantedPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

Revokes a user_grant permission from an app. After the call is successful, the app loses the user_grant permission and cannot access the corresponding protected resources. This API uses a promise to return the result.This API only supports revoking permissions of the user_grant type and does not support controlling whether to terminate the app process. If you need to revoke permissions of the user_grant or manual_settings type, or need to control whether to terminate the app process after revoking the permission, you are advised to use [revokePermission](#revokepermission).When the permission status changes from "authorized" to "unauthorized", the app process will be terminated.

**Since:** 8

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## revokeUserGrantedPermission

```TypeScript
revokeUserGrantedPermission(
        tokenID: number,
        permissionName: Permissions,
        permissionFlags: number,
        callback: AsyncCallback<void>
    ): void
```

Revokes a user_grant permission from an app. This API uses an asynchronous callback to return the result. After the call is successful, the app loses the user_grant permission and cannot access the corresponding protected resources.

**Since:** 8

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| permissionFlags | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>
```

Sets the dialog toggle status for a specified permission of the current user. After the call is successful, the dialog toggle status of the permission will be set to the specified value. When the status is CLOSED, no permission dialog will pop up when the app requests the permission. When the status is OPEN, the permission dialog will pop up normally when the app requests the permission. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(
      permissionName: Permissions,
      status: PermissionRequestToggleStatus,
      subProfileId: number): Promise<void>
```

Sets the dialog toggle status for a specified permission under a specified sub-profile. After the call is successful, the dialog toggle status of the permission will be set to the specified value. When the status is CLOSED, no permission dialog will pop up when the app requests the permission. When the status is OPEN, the permission dialog will pop up normally when the app requests the permission. This API uses a promise to return the result.

**Since:** 26.1.0

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes |
| [subProfileId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
