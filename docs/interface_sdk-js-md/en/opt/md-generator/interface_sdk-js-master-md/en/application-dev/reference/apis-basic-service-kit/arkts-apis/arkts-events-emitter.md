# @ohos.events.emitter

This module provides APIs for sending and processing events between threads in a process or within a thread. You can use the APIs of this module to subscribe to events (continuous subscription or one-shot subscription), cancel event subscription, send events to the event queue, and query the number of subscribed events. In this way, event communication between different threads in the same process and within the same thread can be implemented. It is applicable to scenarios such as cross-thread communication, module decoupling, and the event-driven mode, helping developers implement a lightweight publish-subscribe pattern, reduce coupling between components, and improve code maintainability and scalability. Two event processing entries are provided. You can select one based on the isolation requirements: - **Namespace APIs** (**on**, **once**, **off**, **emit**, and **getListenerCount** in the **emitter** namespace): provide global event subscription and publishing capabilities within a process. This entry works based on the global event queue. Any thread in the same process can subscribe to and publish events. These APIs are suitable for cross-thread event communication. - **Instance APIs** (**Emitter** class): provide the event subscription and publishing capabilities within the same **Emitter** instance. Different **Emitter** instances are isolated from each other. You can create multiple independent event communication channels when events need to be isolated or grouped by instance. **APIs used in combination** The event communication of this module follows the calling sequence of subscription, publishing, processing, and unsubscription. For both namespace and instance APIs, you need to subscribe to an event first, and then another thread or the same thread publishes the event. The callback is executed after the event is received. When the event is no longer needed, unsubscribe from the event to release resources. In addition, event subscription has a lifecycle. Pay attention to resource management: - **Continuous subscription** (**on**): The subscription remains valid until **off** is called to cancel subscription. If the subscription is not canceled, it will be retained. - **One-shot subscription** (**once**): The subscription is automatically canceled after the event is received for the first time and the callback is executed. You do not need to manually call **off**. - **Time for unsubscription**: After the subscription is canceled by calling **off**, the events that have been published through **emit** but have not been executed are also canceled and no callback is triggered. Note that when canceling a specified callback, you need to pass the corresponding callback function. If no callback is specified, all subscriptions to the event are canceled.

**Since:** 23

<!--Device-unnamed-declare namespace emitter--><!--Device-unnamed-declare namespace emitter-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [emit_InnerEvent](arkts-basicservices-emitter-emitinnerevent-f.md#emitinnerevent) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-1) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-2) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-3) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-4) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-5) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-6) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-7) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-8) |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-9) |
| [getListenerCount](arkts-basicservices-emitter-getlistenercount-f.md#getlistenercount) |
| [offEventData](arkts-basicservices-emitter-offeventdata-f.md#offeventdata) |
| [offGenericEventData](arkts-basicservices-emitter-offgenericeventdata-f.md#offgenericeventdata) |
| [off_long](arkts-basicservices-emitter-offlong-f.md#offlong) |
| [off_long](arkts-basicservices-emitter-offlong-f.md#offlong) |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring) |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring-1) |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring-2) |
| [onEventData](arkts-basicservices-emitter-oneventdata-f.md#oneventdata) |
| [onGenericEventData](arkts-basicservices-emitter-ongenericeventdata-f.md#ongenericeventdata) |
| [on_InnerEvent](arkts-basicservices-emitter-oninnerevent-f.md#oninnerevent) |
| [on_string](arkts-basicservices-emitter-onstring-f.md#onstring) |
| [on_string](arkts-basicservices-emitter-onstring-f.md#onstring-1) |
| [onceEventData](arkts-basicservices-emitter-onceeventdata-f.md#onceeventdata) |
| [onceGenericEventData](arkts-basicservices-emitter-oncegenericeventdata-f.md#oncegenericeventdata) |
| [once_InnerEvent](arkts-basicservices-emitter-onceinnerevent-f.md#onceinnerevent) |
| [once_string](arkts-basicservices-emitter-oncestring-f.md#oncestring) |
| [once_string](arkts-basicservices-emitter-oncestring-f.md#oncestring-1) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Emitter](arkts-basicservices-emitter-emitter-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventData](arkts-basicservices-emitter-eventdata-i.md) |
| [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md) |
| [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) |
| [Options](arkts-basicservices-emitter-options-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventPriority](arkts-basicservices-emitter-eventpriority-e.md) |
