# @ohos.events.emitter

This module provides APIs for sending and processing events between threads in a process or within a thread. You can use the APIs of this module to subscribe to events (continuous subscription or one-shot subscription), cancel event subscription, send events to the event queue, and query the number of subscribed events. In this way, event communication between different threads in the same process and within the same thread can be implemented. It is applicable to scenarios such as cross-thread communication, module decoupling, and the event-driven mode, helping developers implement a lightweight publish-subscribe pattern, reduce coupling between components, and improve code maintainability and scalability. Two event processing entries are provided. You can select one based on the isolation requirements: - **Namespace APIs** (**on**, **once**, **off**, **emit**, and **getListenerCount** in the **emitter** namespace): provide global event subscription and publishing capabilities within a process. This entry works based on the global event queue. Any thread in the same process can subscribe to and publish events. These APIs are suitable for cross-thread event communication. - **Instance APIs** (**Emitter** class): provide the event subscription and publishing capabilities within the same **Emitter** instance. Different **Emitter** instances are isolated from each other. You can create multiple independent event communication channels when events need to be isolated or grouped by instance. **APIs used in combination** The event communication of this module follows the calling sequence of subscription, publishing, processing, and unsubscription. For both namespace and instance APIs, you need to subscribe to an event first, and then another thread or the same thread publishes the event. The callback is executed after the event is received. When the event is no longer needed, unsubscribe from the event to release resources. In addition, event subscription has a lifecycle. Pay attention to resource management: - **Continuous subscription** (**on**): The subscription remains valid until **off** is called to cancel subscription. If the subscription is not canceled, it will be retained. - **One-shot subscription** (**once**): The subscription is automatically canceled after the event is received for the first time and the callback is executed. You do not need to manually call **off**. - **Time for unsubscription**: After the subscription is canceled by calling **off**, the events that have been published through **emit** but have not been executed are also canceled and no callback is triggered. Note that when canceling a specified callback, you need to pass the corresponding callback function. If no callback is specified, all subscriptions to the event are canceled.

**Since:** 23

<!--Device-unnamed-declare namespace emitter--><!--Device-unnamed-declare namespace emitter-End-->

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
import { emitter } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [emit_InnerEvent](arkts-basicservices-emitter-emitinnerevent-f.md#emitinnerevent) | Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring) | Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-1) | Emits the specified event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-2) | Emits the specified event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-3) | Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-4) | Emits the specified event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-5) | Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-6) | Emits an event of a specified priority. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-7) | Emits an event of a specified priority. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-8) | Emits an event of a specified priority. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event. |
| [emit_string](arkts-basicservices-emitter-emitstring-f.md#emitstring-9) | Emits an event of a specified priority. |
| [getListenerCount](arkts-basicservices-emitter-getlistenercount-f.md#getlistenercount) | Obtains the number of subscriptions to a specified event. |
| [offEventData](arkts-basicservices-emitter-offeventdata-f.md#offeventdata) | Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when Callback&lt;EventData&gt; has been registered through the on or once API. Otherwise, no processing is performed. |
| [offGenericEventData](arkts-basicservices-emitter-offgenericeventdata-f.md#offgenericeventdata) | Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when Callback&lt;EventData&gt; has been registered through the on or once API. Otherwise, no processing is performed. |
| [off_long](arkts-basicservices-emitter-offlong-f.md#offlong) | Unsubscribes from all events with the specified event ID. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed. |
| [off_long](arkts-basicservices-emitter-offlong-f.md#offlong-1) | Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the [on](arkts-basicservices-emitter-oninnerevent-f.md#oninnerevent) or once API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed. |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring) | Unsubscribes from all events with the specified event ID. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed. |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring-1) | Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the [on](arkts-basicservices-emitter-oninnerevent-f.md#oninnerevent) or once API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed. |
| [off_string](arkts-basicservices-emitter-offstring-f.md#offstring-2) | Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when **Callback\&lt;EventData&gt;** has been registered through the on or once API. Otherwise, no processing is performed. After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed. |
| [onEventData](arkts-basicservices-emitter-oneventdata-f.md#oneventdata) | Subscribes to an event in persistent manner and executes a callback after the event is received. |
| [onGenericEventData](arkts-basicservices-emitter-ongenericeventdata-f.md#ongenericeventdata) | Subscribes to an event in persistent manner and executes a callback after the event is received. |
| [on_InnerEvent](arkts-basicservices-emitter-oninnerevent-f.md#oninnerevent) | Subscribes to an event in persistent manner and executes a callback after the event is received. |
| [on_string](arkts-basicservices-emitter-onstring-f.md#onstring) | Subscribes to an event in persistent manner and executes a callback after the event is received. |
| [on_string](arkts-basicservices-emitter-onstring-f.md#onstring-1) | Subscribes to an event in persistent manner and executes a callback after the event is received. |
| [onceEventData](arkts-basicservices-emitter-onceeventdata-f.md#onceeventdata) | Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed. |
| [onceGenericEventData](arkts-basicservices-emitter-oncegenericeventdata-f.md#oncegenericeventdata) | Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed. |
| [once_InnerEvent](arkts-basicservices-emitter-onceinnerevent-f.md#onceinnerevent) | Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed. |
| [once_string](arkts-basicservices-emitter-oncestring-f.md#oncestring) | Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed. |
| [once_string](arkts-basicservices-emitter-oncestring-f.md#oncestring-1) | Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed. |

### Classes

| Name | Description |
| --- | --- |
| [Emitter](arkts-basicservices-emitter-emitter-c.md) | This module provides the capabilities of sending and processing inter- or intra-thread events in a process of the same **Emitter** instance. You can use the following APIs to subscribe to an event in persistent or one-shot manner, cancel the subscription, or emit an event to the event queue. This module is applicable when inter-thread communication and event management are required based on independent instances. Different **Emitter** instances are isolated from each other. |

### Interfaces

| Name | Description |
| --- | --- |
| [EventData](arkts-basicservices-emitter-eventdata-i.md) | Describes data carried by the emitted event. |
| [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md) | Describes the generic data carried by the emitted event. |
| [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | Describes an event to subscribe to or emit. The **EventPriority** settings do not take effect under event subscription. |
| [Options](arkts-basicservices-emitter-options-i.md) | Describes the event emit priority. |

### Enums

| Name | Description |
| --- | --- |
| [EventPriority](arkts-basicservices-emitter-eventpriority-e.md) | Enumerates the event priorities. |

