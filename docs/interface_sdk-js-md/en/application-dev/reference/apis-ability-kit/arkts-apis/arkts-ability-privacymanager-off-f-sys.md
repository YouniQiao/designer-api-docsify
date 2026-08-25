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

Unsubscribes from permission usage status change events for a specified permission list. After a successful unsubscription, status change notifications for the specified permission list will no longer be received.When unsubscribing, if no callback function is passed in, all callback functions under the permissionList are deleted in batch.

> **NOTE：**
> This API is typically used in conjunction with [on](arkts-ability-privacymanager-on-f-sys.md) to cancel the listening relationship created by on.

**Since:** 9

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activeStateChange' | Yes |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ActiveChangeResponse](arkts-ability-privacymanager-activechangeresponse-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100004](../errorcode-access-token.md#12100004-listener-apis-not-used-in-pairs) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
