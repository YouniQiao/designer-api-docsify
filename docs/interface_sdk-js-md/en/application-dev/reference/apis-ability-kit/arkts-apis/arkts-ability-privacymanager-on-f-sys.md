# on (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## on('activeStateChange')

```TypeScript
function on(type: 'activeStateChange',
    permissionList: Array<Permissions>,
    callback: Callback<ActiveChangeResponse>): void
```

Subscribes to permission usage status change events for a specified permission list. Permission usage status changes are triggered by calls to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission) and  
[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission). After a successful subscription, when the permission usage status changes, the callback function is triggered, returning an  
[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md#ActiveChangeResponse) object containing details of the permission usage status change. This API uses an asynchronous callback to return the result.

Multiple callback functions are allowed to be subscribed for the same permissionList.

> **NOTE：**
> It is not allowed to subscribe the same callback function using two permissionLists that have an intersection.
> That is, if two permissionLists contain the same permission name, the same callback function cannot be used for
subscription.  
> This API is typically used in conjunction with [off](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off).
> When listening is no longer needed, off should be called to unsubscribe.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function on(type: 'activeStateChange',    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function on(type: 'activeStateChange',    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'activeStateChange' | Yes | Event type. The value is **'activeStateChange'**, which indicates the permission usage change. |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of subscribed permission names. An empty value indicates subscription to the usage status changes of all permissions. Passing an invalid value returns error code 12100001. &lt;br&gt;Value constraint: The array length cannot exceed 1024. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | Yes | Callback used to return the object of subscribing to state changes of the specified permission. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12100008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [12100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionList exceeds the size limit, or the permissionNames in the list are all invalid. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is used repeatedly with the same input. |
| [12100005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100005-listener-overflows) | The registration time has exceeded the limit. |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

## Examples

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let permissionList: Array<Permissions> = [];
try {
    privacyManager.on('activeStateChange', permissionList, (data: privacyManager.ActiveChangeResponse) => {
        console.debug(`receive permission state change, data: + ${data}`);
    });
} catch(err) {
    console.error(`Catch errcode: ${err.code}, message: ${err.message}`);
}
```

