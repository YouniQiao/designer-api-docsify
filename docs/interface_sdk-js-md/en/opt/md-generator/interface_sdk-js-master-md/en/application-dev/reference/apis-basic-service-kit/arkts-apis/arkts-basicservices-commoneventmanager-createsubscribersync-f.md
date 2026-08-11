# createSubscriberSync

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## createSubscriberSync

```TypeScript
function createSubscriberSync(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber
```

Creates a subscriber synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-commonEventManager-function createSubscriberSync(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber--><!--Device-commonEventManager-function createSubscriberSync(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](arkts-basicservices-commoneventmanager-commoneventsubscribeinfo-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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
  subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```
