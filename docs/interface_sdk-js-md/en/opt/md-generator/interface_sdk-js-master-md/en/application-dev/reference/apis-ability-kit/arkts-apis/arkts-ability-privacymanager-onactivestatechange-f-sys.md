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

Subscribes to permission usage status change events for a specified permission list. Permission usage status changes are triggered by calls to [startUsingPermission](arkts-ability-privacymanager-startusingpermission-f-sys.md#startUsingPermission-(System-API)) and [stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopUsingPermission-(System-API)). After a successful subscription, when the permission usage status changes, the callback function is triggered, returning an [ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md#ActiveChangeResponse-(System-API)) object containing details of the permission usage status change. This API uses an asynchronous callback to return the result. Multiple callback functions are allowed to be subscribed for the same permissionList. > **NOTE：**> It is not allowed to subscribe the same callback function using two permissionLists that have an intersection. > That is, if two permissionLists contain the same permission name, the same callback function cannot be used for subscription. > This API is typically used in conjunction with offActiveStateChange. When listening is no longer needed, offActiveStateChange should be called to unsubscribe.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function onActiveStateChange(    permissionList: Array<Permissions>,    callback: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100005](../errorcode-access-token.md#12100005-listener-overflows) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
