# onceGenericEventData

## Modules to Import

```TypeScript
import { emitter } from '@kit.BasicServicesKit';
```

## onceGenericEventData

```TypeScript
function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void
```

Subscribes to an event in one-shot manner and unsubscribes from it after the event callback is executed.

**Since:** 23

**Deprecated since:** -1

<!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void--><!--Device-emitter-function onceGenericEventData<T>(eventId: string, callback: Callback<GenericEventData<T>>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventId | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[GenericEventData](arkts-basicservices-emitter-genericeventdata-i.md)&lt;T&gt;&gt; | Yes |
