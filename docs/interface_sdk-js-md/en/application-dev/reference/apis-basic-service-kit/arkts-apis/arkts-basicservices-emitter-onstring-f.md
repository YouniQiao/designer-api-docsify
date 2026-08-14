# on_string

## Modules to Import

```TypeScript
import { emitter } from 'emitter';
```

## on_string

```TypeScript
function on(eventId: string, callback: Callback<EventData>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function on(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function on(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes | Callback to be invoked when the event is received. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.on(`eventId`, callback);
```


## on_string

```TypeScript
function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-emitter-function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event ID, which cannot be empty or exceed 10,240 bytes. Excess content will be truncated. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes | Callback to be invoked when the event is received. |

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
}
// Execute the callback after receiving the event whose event ID is eventId.
emitter.on("eventId", callback);
```

