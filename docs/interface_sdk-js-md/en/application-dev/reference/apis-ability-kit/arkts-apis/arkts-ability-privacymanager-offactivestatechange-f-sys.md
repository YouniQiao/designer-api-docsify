# offActiveStateChange (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## offActiveStateChange

```TypeScript
function offActiveStateChange(
    permissionList: Array<Permissions>,
    callback?: Callback<ActiveChangeResponse>): void
```

Unsubscribes from permission usage status change events for a specified permission list. After a successful unsubscription, status change notifications for the specified permission list will no longer be received.

When unsubscribing, if no callback function is passed in, all callback functions under the permissionList are deleted in batch.

> **NOTE：**
> This API is typically used in conjunction with [onActiveStateChange](arkts-ability-privacymanager-onactivestatechange-f-sys.md) to cancel the listening relationship created by onActiveStateChange.

**Since:** 23

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function offActiveStateChange(    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function offActiveStateChange(    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | List of permission names to unsubscribe from. If empty, unsubscribes from all permission status changes. Must be consistent with the input of on. <br>Value constraint: The array length cannot exceed 1024. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | No | Callback used to return the object for unsubscribing from the status change event of the specified tokenId and permission names. Must be consistent with the callback passed to onActiveStateChange. If this parameter is not provided, all callback functions under permissionList will be deleted in batch. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The permissionList is not in the listening list. |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) | The API is not used in pair with 'on'. |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) | Out of memory. |

