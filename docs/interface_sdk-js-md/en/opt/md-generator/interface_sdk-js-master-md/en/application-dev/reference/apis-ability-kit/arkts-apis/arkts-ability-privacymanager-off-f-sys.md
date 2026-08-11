# off (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## off('activeStateChange')

```TypeScript
function off(
    type: 'activeStateChange',
    permissionList: Array<Permissions>,
    callback?: Callback<ActiveChangeResponse>): void
```

Unsubscribes from permission usage status change events for a specified permission list. After a successful unsubscription, status change notifications for the specified permission list will no longer be received.

When unsubscribing, if no callback function is passed in, all callback functions under the permissionList are deleted in batch.

> **NOTE：**
> This API is typically used in conjunction with [on](privacyManager.on) to cancel the listening relationship
 created by on.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function off(    type: 'activeStateChange',    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void--><!--Device-privacyManager-function off(    type: 'activeStateChange',    permissionList: Array<Permissions>,    callback?: Callback<ActiveChangeResponse>): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeStateChange' | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ActiveChangeResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## Examples

```TypeScript
import { privacyManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let permissionList: Array<Permissions> = [];
try {
    // Unsubscribe from permission usage status change events
    privacyManager.off('activeStateChange', permissionList);
} catch (err) {
    let error = err as BusinessError;
    console.error(`Catch errcode: ${error.code}, message: ${error.message}`);
}
```
