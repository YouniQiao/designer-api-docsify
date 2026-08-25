# Emitter

This module provides the capabilities of sending and processing inter- or intra-thread events in a process of the same **Emitter** instance. You can use the following APIs to subscribe to an event in persistent or one-shot manner, cancel the subscription, or emit an event to the event queue. This module is applicable when inter-thread communication and event management are required based on independent instances. Different **Emitter** instances are isolated from each other.

**Since:** 22

**System capability:** SystemCapability.Notification.Emitter

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

Defines a constructor.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

## emit

```TypeScript
emit(eventId: string, data?: EventData): void
```

Emits a specified event to the Emitter class instance.This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

## emit

```TypeScript
emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event to the Emitter class instance.This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

## emit

```TypeScript
emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority to the Emitter instance.This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

## emit

```TypeScript
emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority to the Emitter instance.This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No |

## getListenerCount

```TypeScript
getListenerCount(eventId: string): number
```

Obtains the number of subscriptions to a specified event of the Emitter instance.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## off

```TypeScript
off(eventId: string): void
```

Unsubscribes from all events with the specified event ID of the Emitter instance.After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |

## off

```TypeScript
off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the on or once API is used to subscribe to the event with specified event ID and a callback is used to process the event.After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## off

```TypeScript
off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the [on](#on) or [once](#once) API is used to subscribe to the event with specified event ID and a callback is used to process the event.After this API is used to unsubscribe from an event, the event that has been published through the emit API but has not been executed will be unsubscribed.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

## on

```TypeScript
on(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## on

```TypeScript
on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |

## once

```TypeScript
once(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |

## once

```TypeScript
once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |
