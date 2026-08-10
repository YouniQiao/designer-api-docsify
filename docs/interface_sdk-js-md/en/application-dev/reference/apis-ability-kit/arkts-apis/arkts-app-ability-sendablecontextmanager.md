# @ohos.app.ability.sendableContextManager

sendableContextManager模块提供Context与[SendableContext](arkts-ability-sendablecontext-i.md)相互转换的能力。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace sendableContextManager--><!--Device-unnamed-declare namespace sendableContextManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { sendableContextManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [convertFromContext](arkts-ability-sendablecontextmanager-convertfromcontext-f.md#convertfromcontext) | 将Context转换为SendableContext对象。 |
| [convertToAbilityStageContext](arkts-ability-sendablecontextmanager-converttoabilitystagecontext-f.md#converttoabilitystagecontext) | 将SendableContext对象转换为AbilityStageContext。 |
| [convertToApplicationContext](arkts-ability-sendablecontextmanager-converttoapplicationcontext-f.md#converttoapplicationcontext) | 将SendableContext对象转换为ApplicationContext。 |
| [convertToContext](arkts-ability-sendablecontextmanager-converttocontext-f.md#converttocontext) | 将SendableContext对象转换为Context。 |
| [convertToUIAbilityContext](arkts-ability-sendablecontextmanager-converttouiabilitycontext-f.md#converttouiabilitycontext) | 将SendableContext对象转换为UIAbilityContext。 |
| [setEventHubMultithreadingEnabled](arkts-ability-sendablecontextmanager-seteventhubmultithreadingenabled-f.md#seteventhubmultithreadingenabled) | 设置[Context](arkts-ability-context-t.md)中的[EventHub](arkts-ability-eventhub-c.md)是否启用跨线程通信能力。 |

### Types

| Name | Description |
| --- | --- |
| [SendableContext](arkts-ability-sendablecontextmanager-sendablecontext-t.md) | SendableContext二级模块 |

