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

<!--Device-commonEventManager-function publish(event: string, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publish(event: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Publish a common event.
try {
  commonEventManager.publish('event', (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

Publishes a common event. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-commonEventManager-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void-End-->

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
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500003](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500003-common-event-sending-frequency-is-too-high) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |
| [1500009](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500009-failed-to-obtain-system-parameters) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Common event information. The following uses an ordered common event as an example.
let options: commonEventManager.CommonEventPublishData = {
  code: 0,
  data: 'initial data',
  isOrdered: true // The common event is an ordered one.
};

// Publish a common event.
try {
  commonEventManager.publish('event', options, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in publishing common event.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```
