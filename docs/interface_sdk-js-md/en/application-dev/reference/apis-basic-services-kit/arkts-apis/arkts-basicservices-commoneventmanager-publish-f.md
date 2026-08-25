# publish

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## publish

```TypeScript
function publish(event: string, callback: AsyncCallback<void>): void
```

Publishes a common event. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1500003](../errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

Publishes a common event. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1500003](../errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500007](../errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500008](../errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |
