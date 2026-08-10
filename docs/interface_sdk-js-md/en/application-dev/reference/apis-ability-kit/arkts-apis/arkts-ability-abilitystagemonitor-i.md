# AbilityStageMonitor

本模块提供监听指定[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)对象的能力。开发者可以将AbilityStageMonitor作为  
[abilityDelegator.waitAbilityStageMonitor](arkts-ability-abilitydelegator-i.md#waitabilitystagemonitor)的入参来注册监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityStageMonitor--><!--Device-unnamed-export interface AbilityStageMonitor-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName: string
```

被监听的AbilityStage的模块名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStageMonitor-moduleName: string--><!--Device-AbilityStageMonitor-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## srcEntrance

```TypeScript
srcEntrance: string
```

被监听的AbilityStage的源路径。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStageMonitor-srcEntrance: string--><!--Device-AbilityStageMonitor-srcEntrance: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

