# removeStickyCommonEvent (System API)

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string, callback: AsyncCallback<void>): void
```

Removes a sticky common event. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.COMMONEVENT_STICKY

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1500004](../errorcode-CommonEventService.md#1500004-failed-to-send-system-common-events) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |


## removeStickyCommonEvent

```TypeScript
function removeStickyCommonEvent(event: string): Promise<void>
```

Removes a sticky common event that has been published. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.COMMONEVENT_STICKY

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1500004](../errorcode-CommonEventService.md#1500004-failed-to-send-system-common-events) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
