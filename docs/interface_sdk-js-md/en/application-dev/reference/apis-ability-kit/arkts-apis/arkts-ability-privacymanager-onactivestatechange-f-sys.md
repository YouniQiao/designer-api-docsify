# onActiveStateChange (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## onActiveStateChange

```TypeScript
function onActiveStateChange(
    permissionList: Array<Permissions>,
    callback: Callback<ActiveChangeResponse>): void
```

Subscribes to permission usage status change events for a specified permission list. Permission usage status changes are triggered by calls to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md) and [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md). After a successful subscription, when the permission usage status changes, the callback function is triggered, returning an [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md) object containing details of the permission usage status change. This API uses an asynchronous callback to return the result.

Multiple callback functions are allowed to be subscribed for the same permissionList.

> **NOTE：**
> It is not allowed to subscribe the same callback function using two permissionLists that have an intersection.
> That is, if two permissionLists contain the same permission name, the same callback function cannot be used for subscription.
> This API is typically used in conjunction with [offActiveStateChange](arkts-ability-privacymanager-offactivestatechange-f-sys.md). When listening is no longer needed, offActiveStateChange should be called to unsubscribe.

**Since:** 23

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of subscribed permission names. An empty value indicates subscription to the usage status changes of all permissions. Passing an invalid value returns error code 12100001. <br>Value constraint: The array length cannot exceed 1024. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | Yes | Callback used to return the event object for the subscribed permission state change. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionList exceeds the size limit, or the permissionNames in the list are all invalid. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is used repeatedly with the same input. |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) | The registration time has exceeded the limit. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |

