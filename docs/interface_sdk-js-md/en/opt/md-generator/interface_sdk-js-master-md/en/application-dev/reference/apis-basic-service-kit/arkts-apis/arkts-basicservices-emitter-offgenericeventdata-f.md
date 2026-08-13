# offGenericEventData

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## offGenericEventData

```TypeScript
function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Unsubscribes from an event with the specified event ID and processed by the specified callback. This API takes effect only when Callback&lt;EventData&gt; has been registered through the on or once API. Otherwise, no processing is performed.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function offGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |
