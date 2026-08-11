# LoopObserver

The module defines an observer to listen for event processing timeout. It can be used as an input parameter in   
[ErrorManager.on](./../@ohos.app.ability.errorManager:errorManager.on(type: 'loopObserver', timeout: number, observer: LoopObserver))to listen for the event processing timeout of the current application's main thread.

**Since:** 12

<!--Device-unnamed-export interface LoopObserver--><!--Device-unnamed-export interface LoopObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onLoopTimeOut

```TypeScript
onLoopTimeOut?(timeout: number): void
```

Called when a timeout occurs for the main thread to process an event in the JS runtime.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LoopObserver-onLoopTimeOut?(timeout: int): void--><!--Device-LoopObserver-onLoopTimeOut?(timeout: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| timeout | number | Yes |
