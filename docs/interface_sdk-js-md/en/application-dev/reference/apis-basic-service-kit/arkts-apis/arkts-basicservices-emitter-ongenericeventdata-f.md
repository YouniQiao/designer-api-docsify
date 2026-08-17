# onGenericEventData

## Modules to Import

```TypeScript
import { emitter } from 'emitter';
```

## onGenericEventData

```TypeScript
function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in persistent manner and executes a callback after the event is received.

**Since:** 23

<!--Device-emitter-function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function onGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | Event to subscribe to in persistent manner. The value cannot be an empty string and exceed 10240 bytes. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes | Callback to be executed when the event is received. |

**Examples**

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
emitter.onGenericEventData("eventId", callback);
```

