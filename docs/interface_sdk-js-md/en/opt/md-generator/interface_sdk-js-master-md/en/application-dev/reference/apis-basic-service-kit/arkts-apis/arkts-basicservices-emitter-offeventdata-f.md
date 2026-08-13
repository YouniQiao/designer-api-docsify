# offEventData

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## offEventData

```TypeScript
function offEventData(eventId: string, callback: Callback<EventData>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when Callback&lt;EventData&gt; has been registered through the on or once API. Otherwise, no processing is performed.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[EventData](arkts-basicservices-emitter-eventdata-i.md)&gt; | Yes |
