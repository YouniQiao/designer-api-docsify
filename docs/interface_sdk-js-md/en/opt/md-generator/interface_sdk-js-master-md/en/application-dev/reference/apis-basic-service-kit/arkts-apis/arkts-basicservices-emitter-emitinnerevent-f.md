# emit_InnerEvent

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## emit_InnerEvent

```TypeScript
function emit(event: InnerEvent, data?: EventData): void
```

Emits a specified event. This API can be used to emit data objects across threads. The data objects must meet the specifications specified in [Overview of Inter-Thread Communication Objects](../../../arkts-utils/serializable-overview.md). Currently, complex data decorated by decorators such as [@State](../../../ui/state-management/arkts-state.md) and [@Observed](../../../ui/state-management/arkts-observed-and-objectlink.md) is not supported. After an event is published using this API, the event may not be executed immediately. When the execution starts depends on the number of events in the event queue and the execution efficiency of each event.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void--><!--Device-emitter-function emit(event: InnerEvent, data?: EventData): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [InnerEvent](arkts-basicservices-emitter-innerevent-i.md) | Yes |
| data | [EventData](arkts-basicservices-emitter-eventdata-i.md) | No |

## Examples

```TypeScript
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);
```
