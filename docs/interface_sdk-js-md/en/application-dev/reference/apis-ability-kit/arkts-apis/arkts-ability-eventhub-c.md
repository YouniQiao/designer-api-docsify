# EventHub

EventHub is an event communication mechanism based on the publish-subscribe pattern. It decouples senders and subscribers through event names, supporting efficient data transfer and state synchronization between different service modules. It is primarily used for [data communication between UIAbility components and UI pages](../../../application-models/uiability-data-sync-with-ui.md). Different Context objects have different EventHub objects, and different EventHub objects cannot communicate directly with each other. Event subscription, unsubscription, and triggering all take place on a specific EventHub object. Since Worker and TaskPool implement [multithreaded concurrency](../../../arkts-utils/multi-thread-concurrency-overview.md#multithreaded-concurrency-models) through the actor model, where different virtual machine instances have exclusive memory, EventHub objects cannot be used for inter-thread data communication.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## emit

```TypeScript
emit(event: string, ...args: Object[]): void
```

Trigger the event callbacks.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off

```TypeScript
off(event: string, callback?: Function): void
```

Unsubscribes from an event.  
- If **callback** is specified, this API unsubscribes from the given event with the specified callback.  
- If **callback** is not specified, this API unsubscribes from the given event with all callbacks.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | Function | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on

```TypeScript
on(event: string, callback: Function): void
```

Subscribes to an event.

> **NOTE：**&gt;
> When the callback is triggered by **emit**, the invoker is the EventHub object. To change the direction of
> **this** in **callback**, use an arrow function.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| callback | Function | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
