# subscribeToEvent

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## subscribeToEvent

```TypeScript
function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>
```

Subscribes to a common event. This API uses a promise to return the result, indicating subscription success or failure.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-commonEventManager-function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>--><!--Device-commonEventManager-function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;CommonEventData&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1500007](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) |
| [1500010](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500010-the-number-of-subscribers-exceeds-the-upper-limit) |
| [1500008](../../apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Define a subscriber to save the created subscriber object for subsequent subscription and unsubscription.
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// Subscriber information.
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['event']
};

// Create a subscriber.
try {
  commonEventManager.createSubscriber(subscribeInfo,
    (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
      if (err) {
        console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
      } else {
        console.info(`Succeeded in creating subscriber.`);
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        try {
          commonEventManager.subscribeToEvent(subscriber, (data: commonEventManager.CommonEventData) => {
            console.info(`Succeeded to receive common event, data is ${JSON.stringify(data)}`);
          }).then(() => {
            console.info(`Succeeded in subscribing.`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
          });
        } catch (error) {
          let err: BusinessError = error as BusinessError;
          console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
        }
      }
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```
