# Emitter

This module provides the capabilities of sending and processing inter- or intra-thread events in a process of the same **Emitter** instance. You can use the following APIs to subscribe to an event in persistent or one-shot manner, cancel the subscription, or emit an event to the event queue. This module is applicable when inter-thread communication and event management are required based on independent instances. Different   
**Emitter** instances are isolated from each other.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-emitter-export class Emitter--><!--Device-emitter-export class Emitter-End-->

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

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-constructor()--><!--Device-Emitter-constructor()-End-->

**System capability:** SystemCapability.Notification.Emitter

## Examples

```TypeScript
let emitter1 = new emitter.Emitter();
```

## emit

```TypeScript
emit(eventId: string, data?: EventData): void
```

Emits a specified event to the Emitter class instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and   
[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-emit(eventId: string, data?: EventData): void--><!--Device-Emitter-emit(eventId: string, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | Data carried by the event. This parameter is left empty by default. |

## Examples

ArkTS-Dyn example:

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", eventData);
```

ArkTS-Sta example:

```TypeScript
import { RecordData } from '@ohos.base';

let emitter1 = new emitter.Emitter();
let record: Record<string, RecordData> = {
  "content": "content",
  "id": 1,
};

let eventData: emitter.EventData = {
  data: record // The types are now compatible.
};

emitter1.emit("eventId", eventData);
```

## emit

```TypeScript
emit<T>(eventId: string, data?: GenericEventData<T>): void
```

Emits a specified event to the Emitter class instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and   
[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-emit<T>(eventId: string, data?: GenericEventData<T>): void--><!--Device-Emitter-emit<T>(eventId: string, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

## Examples

```TypeScript
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", eventData);
```

## emit

```TypeScript
emit(eventId: string, options: Options, data?: EventData): void
```

Emits an event of a specified priority to the Emitter instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and   
[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-emit(eventId: string, options: Options, data?: EventData): void--><!--Device-Emitter-emit(eventId: string, options: Options, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | Event emit priority. |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No | Data carried by the event. This parameter is left empty by default. |

## Examples

ArkTS-Dyn example:

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.EventData = {
  data: {
  "content": "content",
  "id": 1,
  }
};

emitter1.emit("eventId", options, eventData);
```

ArkTS-Sta example:

```TypeScript
import { RecordData } from '@ohos.base';

let emitter1 = new emitter.Emitter();
let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let record: Record<string, RecordData> = {
  "content": "content",
  "id": 1,
};
let eventData: emitter.EventData = {
  data: record
};

emitter1.emit("eventId", options, eventData);
```

## emit

```TypeScript
emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void
```

Emits an event of a specified priority to the Emitter instance.

This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and   
[@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported.

After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void--><!--Device-Emitter-emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes | Event emit priority. |
| data | [GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt; | No | Data carried by the event. This parameter is left empty by default. |

## Examples

```TypeScript
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1 = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit("eventId", options, eventData);
```

## getListenerCount

ArkTS-Dyn:
```TypeScript
getListenerCount(eventId: string): number
```

ArkTS-Sta:
```TypeScript
getListenerCount(eventId: string): long
```

Obtains the number of subscriptions to a specified event of the Emitter instance.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-getListenerCount(eventId: string): long--><!--Device-Emitter-getListenerCount(eventId: string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Number of subscriptions to a specified event. |

## Examples

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();
let count = emitter1.getListenerCount("eventId");
```

## off

```TypeScript
off(eventId: string): void
```

Unsubscribes from all events with the specified event ID of the Emitter instance.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.Emitter#emit(eventId: string, data?: EventData)) API but has not been executed will be unsubscribed.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-off(eventId: string): void--><!--Device-Emitter-off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |

## Examples

```TypeScript
let emitter1: emitter.Emitter = new emitter.Emitter();

emitter1.off("eventId");
```

## off

```TypeScript
off(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the   
[on](emitter.Emitter#on(eventId: string, callback: Callback&lt;EventData&gt;)) or   
[once](emitter.Emitter#once(eventId: string, callback: Callback&lt;EventData&gt;)) API is used to subscribe to the event with specified event ID and a callback is used to process the event.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](emitter.Emitter#emit(eventId: string, data?: EventData)) API but has not been executed will be unsubscribed.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-off(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to unregister. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.off("eventId", callback);
```

## off

```TypeScript
off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event of the Emitter instance. This API takes effect only when the   
[on](emitter.Emitter#on&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>)) or   
[once](emitter.Emitter#once&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>)) API is used to subscribe to the event with specified event ID and a callback is used to process the event.

After this API is used to unsubscribe from an event, the event that has been published through the   
[emit](arkts-basicservices-emitter-emitter-c.md#emit) API but has not been executed will be unsubscribed.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to unregister. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.off("eventId", callback);
```

## offEventData

```TypeScript
offEventData(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to unregister. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1 = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.offEventData("eventId", callback);
```

## offGenericEventData

```TypeScript
offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to unregister. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let emitter1 = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    const sampleData = eventData.data as Sample;
    sampleData.printCount();
  }
}

emitter1.offGenericEventData("eventId", callback);
```

## on

```TypeScript
on(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-on(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-on(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to be invoked when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.on(`eventId`, callback);
```

## on

```TypeScript
on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in persistent manner and executes a callback after the event is received.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to be invoked when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.on("eventId", callback);
```

## onEventData

```TypeScript
onEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-onEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-onEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in persistent manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to be executed when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1 = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.onEventData(`eventId`, callback);
```

## onGenericEventData

```TypeScript
onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in persistent manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to be executed when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1 = new emitter.Emitter();

class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    const sampleData = eventData.data as Sample;
    sampleData.printCount();
  }
}

emitter1.onGenericEventData("eventId", callback);
```

## once

```TypeScript
once(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-once(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-once(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to be invoked when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.once("eventId", callback);
```

## once

```TypeScript
once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event specified by the Emitter instance in one-shot manner and unsubscribes from it after the event callback is executed. This API uses an asynchronous callback to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Emitter-once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to be invoked when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
}

emitter1.once("eventId", callback);
```

## onceEventData

```TypeScript
onceEventData(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-onceEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-Emitter-onceEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in one-shot manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | Callback to be executed when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1 = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}

emitter1.onceEventData("eventId", callback);
```

## onceGenericEventData

```TypeScript
onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Emitter-onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-Emitter-onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in one-shot manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to be executed when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let emitter1 = new emitter.Emitter();

class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    const sampleData = eventData.data as Sample;
    sampleData.printCount();
  }
}

emitter1.onceGenericEventData("eventId", callback);
```

