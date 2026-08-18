# EventHub

EventHub is an event communication mechanism based on the publish-subscribe pattern. It decouples senders and subscribers through event names, supporting efficient data transfer and state synchronization between different service modules. It is primarily used for [data communication between UIAbility components and UI pages](../../../application-models/uiability-data-sync-with-ui.md) . Different Context objects have different EventHub objects, and different EventHub objects cannot communicate directly with each other. Event subscription, unsubscription, and triggering all take place on a specific EventHub object. Since Worker and TaskPool implement [multithreaded concurrency](../../../arkts-utils/multi-thread-concurrency-overview.md#multithreaded-concurrency-models) through the actor model, where different virtual machine instances have exclusive memory, EventHub objects cannot be used for inter-thread data communication.

**Since:** 23

<!--Device-unnamed-declare class EventHub--><!--Device-unnamed-declare class EventHub-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## emit_string

```TypeScript
emit(event: string, ...args: Object[]): void
```

Trigger the event callbacks.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventHub-emit(event: string, ...args: Object[]): void--><!--Device-EventHub-emit(event: string, ...args: Object[]): void-End-->

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

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    this.context.eventHub.on('myEvent', this.eventFunc);
  }

  onDestroy() {
    try {
      // Result
      // eventFunc is called,undefined,undefined
      this.context.eventHub.emit('myEvent');
      // Result
      // eventFunc is called,1,undefined
      this.context.eventHub.emit('myEvent', 1);
      // Result
      // eventFunc is called,1,2
      this.context.eventHub.emit('myEvent', 1, 2);
    } catch (e) {
      let code: number = (e as BusinessError).code;
      let msg: string = (e as BusinessError).message;
      console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
    }
  }

  eventFunc(argOne: number, argTwo: number) {
    console.info(`eventFunc is called, ${argOne}, ${argTwo}`);
  }
}
```

## emit_string

```TypeScript
emit(event: string, ...args: (Object|null|undefined)[]): void
```

Trigger the event callbacks.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventHub-emit(event: string, ...args: (Object|null|undefined)[]): void--><!--Device-EventHub-emit(event: string, ...args: (Object|null|undefined)[]): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | (Object \| null \| undefined)[] | Yes |

## off_string

```TypeScript
off(event: string, callback?: Function): void
```

Unsubscribes from an event. - If **callback** is specified, this API unsubscribes from the given event with the specified callback. - If **callback** is not specified, this API unsubscribes from the given event with all callbacks.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventHub-off(event: string, callback?: Function): void--><!--Device-EventHub-off(event: string, callback?: Function): void-End-->

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

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    try {
      this.context.eventHub.on('myEvent', this.eventFunc1);
      this.context.eventHub.off('myEvent', this.eventFunc1); // Unsubscribe from the myEvent event with the callback eventFunc1.
      this.context.eventHub.on('myEvent', this.eventFunc1);
      this.context.eventHub.on('myEvent', this.eventFunc2);
      this.context.eventHub.off('myEvent'); // Unsubscribe from the myEvent event with all the callbacks (eventFunc1 and eventFunc2).
    } catch (e) {
      let code: number = (e as BusinessError).code;
      let msg: string = (e as BusinessError).message;
      console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
    }
  }

  eventFunc1() {
    console.info('eventFunc1 is called');
  }

  eventFunc2() {
    console.info('eventFunc2 is called');
  }
}
```

## on_string

```TypeScript
on(event: string, callback: Function): void
```

Subscribes to an event. > **NOTE：**> > When the callback is triggered by **emit**, the invoker is the EventHub object. To change the direction of > **this** in **callback**, use an arrow function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EventHub-on(event: string, callback: Function): void--><!--Device-EventHub-on(event: string, callback: Function): void-End-->

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
