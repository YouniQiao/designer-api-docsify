# off

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## off

```TypeScript
function off(eventId: long): void
```

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long): void--><!--Device-emitter-function off(eventId: long): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 事件ID，由开发者定义，用于辨别事件。 |

## Examples

```TypeScript
// Unregister all callbacks for events whose event ID is 1.
emitter.off(1);
```


## off

```TypeScript
function off(eventId: string): void
```

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string): void--><!--Device-emitter-function off(eventId: string): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |

## Examples

```TypeScript
// Unregister all callbacks for events whose event ID is eventId1.
emitter.off('eventId1');
```


## off

```TypeScript
function off(eventId: long, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](emitter.on(event: InnerEvent, callback: Callback&lt;EventData&gt;))或  
[once](emitter.once(event: InnerEvent, callback: Callback&lt;EventData&gt;))接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: long, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 事件ID，由开发者定义，用于辨别事件。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的 callback一致。 |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// Unregister all callbacks for events whose event ID is 1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off(1, callback);
```


## off

```TypeScript
function off(eventId: string, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](emitter.on(eventId: string, callback: Callback&lt;EventData&gt;))或  
[once](emitter.once(eventId: string, callback: Callback&lt;EventData&gt;))接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function off(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的 callback一致。 |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// Unregister all callbacks for events whose event ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```


## off

```TypeScript
function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用  
[on](emitter.on&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>))或  
[once](emitter.once&lt;T&gt;(eventId: string, callback: Callback&lt;GenericEventData<T>&gt;&lt;T&gt;>))接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 事件ID。 不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的 callback一致。 |

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};
// Unregister all callbacks for events whose event ID is eventId1. The callback object must be the object used during registration.
// If the callback has not been registered, no processing is performed.
emitter.off('eventId1', callback);
```

