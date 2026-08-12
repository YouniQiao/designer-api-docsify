# @ohos.commonEventManager

This module provides APIs to publish, subscribe to, and unsubscribe from common events. This module provides a system-level event notification mechanism that allows an app to send notifications to other apps that have subscribed to the event when the system status changes (such as power-on completion, battery level change, and screen on/off) or a custom service event occurs. This mechanism enables transferring information across components and apps.

The key concepts involved in this module are as follows:  
- Unordered common events: common events that CES forwards regardless of whether subscribers receive the events and  
when they subscribe to the events.  
- Ordered common events: common events that CES forwards based on the subscriber priority. CES preferentially  
forwards an ordered common event to the subscriber with higher priority, waits until the subscriber receives the event, and then forwards the events to the subscriber with lower priority. Subscribers with the same priority receive common events in a random order.  
- Sticky common events: common events that can be sent to a subscriber before or after they initiate a  
subscription. Only system apps or services can send sticky common events.

**APIs used in combination**

The event communication of this module involves three processes: subscription, publishing, and ordered event. The subscription process and publishing process are associated through the event name. The publisher and subscriber do not need to be aware of each other.

**Subscription process: Create a subscriber, subscribe to an event, receive the event, and cancel the subscription.**

1. Configure the subscriber information, declare the name of the event to be subscribed to, and set the subscription priority, publisher permission, and package name as required.2. Create a subscriber object using **commonEventManager.createSubscriberSync**.3. Subscribe to an event using **commonEventManager.subscribe**. When an event is published, use a callback to receive **CommonEventData**, and process the event data in the callback.4. Unsubscribe from the event using **commonEventManager.unsubscribe** when it is no longer needed.

**Publishing process: Publish an event (carrying data and attributes as required).**

1. Simple publishing: Publish an event by specifying only the event name using **commonEventManager.publish**.2. Publishing with data and attributes: Configure attributes such as code, data, parameters, and **isOrdered**using **CommonEventPublishData**, and then call **publish** to publish the event.

**Ordered event process: Deliver the event by priority by collaborating with the subscriber.**

1. Set **isOrdered** to **true** using **CommonEventPublishData** and call **publish** to publish ordered events.Events are delivered in sequence based on the subscriber priority.2. The subscriber with a higher priority receives the event first, who can modify the code and data in the callback using methods such as **setCodeAndData** for subsequent subscribers to receive.3. After the processing is complete, call **finishCommonEvent** to deliver the event to the subscriber with the next highest priority. To stop delivering the event, call **abortCommonEvent** to mark the event as aborted.

**Since:** 9

<!--Device-unnamed-declare namespace commonEventManager--><!--Device-unnamed-declare namespace commonEventManager-End-->

**System capability:** SystemCapability.Notification.CommonEvent

## Modules to Import

```TypeScript
import { commonEventManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createSubscriber](arkts-basicservices-commoneventmanager-createsubscriber-f.md#createsubscriber) |
| [createSubscriber](arkts-basicservices-commoneventmanager-createsubscriber-f.md#createsubscriber-1) |
| [createSubscriberSync](arkts-basicservices-commoneventmanager-createsubscribersync-f.md#createsubscribersync) |
| [publish](arkts-basicservices-commoneventmanager-publish-f.md#publish) |
| [publish](arkts-basicservices-commoneventmanager-publish-f.md#publish-1) |
| [subscribe](arkts-basicservices-commoneventmanager-subscribe-f.md#subscribe) |
| [subscribeToEvent](arkts-basicservices-commoneventmanager-subscribetoevent-f.md#subscribetoevent) |
| [unsubscribe](arkts-basicservices-commoneventmanager-unsubscribe-f.md#unsubscribe) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser) |
| [publishAsUser](arkts-basicservices-commoneventmanager-publishasuser-f-sys.md#publishasuser-1) |
| [removeStickyCommonEvent](arkts-basicservices-commoneventmanager-removestickycommonevent-f-sys.md#removestickycommonevent) |
| [removeStickyCommonEvent](arkts-basicservices-commoneventmanager-removestickycommonevent-f-sys.md#removestickycommonevent-1) |
| [setStaticSubscriberState](arkts-basicservices-commoneventmanager-setstaticsubscriberstate-f-sys.md#setstaticsubscriberstate) |
| [setStaticSubscriberState](arkts-basicservices-commoneventmanager-setstaticsubscriberstate-f-sys.md#setstaticsubscriberstate-1) |
| [setStaticSubscriberState](arkts-basicservices-commoneventmanager-setstaticsubscriberstate-f-sys.md#setstaticsubscriberstate-2) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Support](arkts-basicservices-commoneventmanager-support-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Support](arkts-basicservices-commoneventmanager-support-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CommonEventData](arkts-basicservices-commoneventmanager-commoneventdata-t.md) |
| [CommonEventPublishData](arkts-basicservices-commoneventmanager-commoneventpublishdata-t.md) |
| [CommonEventSubscribeInfo](arkts-basicservices-commoneventmanager-commoneventsubscribeinfo-t.md) |
| [CommonEventSubscriber](arkts-basicservices-commoneventmanager-commoneventsubscriber-t.md) |
