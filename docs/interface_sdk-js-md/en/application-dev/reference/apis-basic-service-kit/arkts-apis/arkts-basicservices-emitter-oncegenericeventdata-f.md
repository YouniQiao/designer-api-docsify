# onceGenericEventData

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## onceGenericEventData

```TypeScript
function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in one-shot manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;GenericEventData&lt;T&gt;&gt; | Yes | Callback to be executed when the event is received. |

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  let storage: Sample = eventData.data! as Sample;
  storage.printCount();
}

// Execute the callback after receiving the event whose ID is eventId.
emitter.onceGenericEventData("eventId", callback);
```

