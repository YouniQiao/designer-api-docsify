# publishAsUser (System API)

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

Publishes a common event to a specified user. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1500003](../errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500006](../errorcode-CommonEventService.md#1500006-invalid-user-id) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |


## publishAsUser

```TypeScript
function publishAsUser(
    event: string,
    userId: number,
    options: CommonEventPublishData,
    callback: AsyncCallback<void>
  ): void
```

Publishes a common event to a specified user and specifies the information to be published. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| userId | number | Yes |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1500003](../errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500006](../errorcode-CommonEventService.md#1500006-invalid-user-id) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |
