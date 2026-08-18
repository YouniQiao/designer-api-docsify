# @ohos.app.ability.sendableContextManager

The sendableContextManager module provides APIs for converting between Context and [SendableContext](arkts-ability-sendablecontext-i.md#sendablecontext) objects.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace sendableContextManager--><!--Device-unnamed-declare namespace sendableContextManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { sendableContextManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [convertFromContext](arkts-ability-sendablecontextmanager-convertfromcontext-f.md#convertfromcontext) | Converts a Context object to a SendableContext object. |
| [convertToAbilityStageContext](arkts-ability-sendablecontextmanager-converttoabilitystagecontext-f.md#converttoabilitystagecontext) | Converts a SendableContext object to an AbilityStageContext object. |
| [convertToApplicationContext](arkts-ability-sendablecontextmanager-converttoapplicationcontext-f.md#converttoapplicationcontext) | Converts a SendableContext object to an ApplicationContext object. |
| [convertToContext](arkts-ability-sendablecontextmanager-converttocontext-f.md#converttocontext) | Converts a SendableContext object to a Context object. |
| [convertToUIAbilityContext](arkts-ability-sendablecontextmanager-converttouiabilitycontext-f.md#converttouiabilitycontext) | Converts a SendableContext object to a UIAbilityContext object. |
| [setEventHubMultithreadingEnabled](arkts-ability-sendablecontextmanager-seteventhubmultithreadingenabled-f.md#seteventhubmultithreadingenabled) | Enables the cross-thread data transfer feature of [EventHub](arkts-ability-eventhub-c.md#eventhub) in Context. > **NOTE：**> > - When multiple Context objects communicate, you need to call this API to set each Context object to support > EventHub cross-thread data transfer. |

### Types

| Name | Description |
| --- | --- |
| [SendableContext](arkts-ability-sendablecontextmanager-sendablecontext-t.md) | Level-2 module SendableContext. |

