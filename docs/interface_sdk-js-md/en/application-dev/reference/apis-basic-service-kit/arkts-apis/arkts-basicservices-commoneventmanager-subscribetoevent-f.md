# subscribeToEvent

## Modules to Import

```TypeScript
import { commonEventManager } from '@kit.BasicServicesKit';
```

## subscribeToEvent

```TypeScript
function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>
```

Subscribes to a common event. This API uses a promise to return the result, indicating subscription success or failure.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-commonEventManager-function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>--><!--Device-commonEventManager-function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriber | CommonEventSubscriber | Yes | Subscriber object. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;CommonEventData&gt; | Yes | Callback to be invoked when a common event is subscribed to. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [1500007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-CommonEventService.md#1500007-failed-to-send-a-request-through-ipc) | Failed to send the message to the common event service. |
| [1500010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-CommonEventService.md#1500010-the-number-of-subscribers-exceeds-the-upper-limit) | The count of subscriber exceeds system specification. |
| [1500008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-CommonEventService.md#1500008-failed-to-initialize-the-common-event-service) | Failed to initialize the common event service. |

## Examples

ArkTS-Dyn example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Define a subscriber to save the created subscriber object for subsequent subscription and unsubscription.
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// Subscriber information.
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ["event"]
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
            console.info(`Succeeded to receive common event, data is ` + JSON.stringify(data));
          }).then(() => {
            console.info(`Succeeded to subscribe.`);
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

ArkTS-Sta example:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Define a subscriber.
let subscriber: commonEventManager.CommonEventSubscriber | undefined | null = null;
// Subscriber information.
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ["event"]
};

// Create a subscriber.
try {
  commonEventManager.createSubscriber(
    subscribeInfo,
    (err: BusinessError | null, commonEventSubscriber: commonEventManager.CommonEventSubscriber | undefined) => {
      if (err) {
        console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
        return;
      }

      // Ensure the subscriber object is valid.
      if (!commonEventSubscriber) {
        console.error(`Failed to create subscriber: subscriber is undefined`);
        return;
      }

      console.info(`Succeeded in creating subscriber.`);
      subscriber = commonEventSubscriber;

      // Use type assertions to ensure the type is correct.
      const validSubscriber = commonEventSubscriber as commonEventManager.CommonEventSubscriber;

      // Subscribe to a common event.
      commonEventManager.subscribeToEvent(
        validSubscriber,
        (data: commonEventManager.CommonEventData) => {
          console.info(`Succeeded to receive common event, data is ${JSON.stringify(data)}`);
        }
      ).then(() => {
        console.info(`Succeeded to subscribe.`);
      }).catch((err: Error) => {
        const businessErr = err as BusinessError;
        console.error(`Failed to subscribe. Code is ${businessErr.code}, message is ${businessErr.message}`);
      });
    }
  );
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```

