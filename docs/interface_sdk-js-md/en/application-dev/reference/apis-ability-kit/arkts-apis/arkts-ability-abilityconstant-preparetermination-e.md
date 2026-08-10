# PrepareTermination

应用准备关闭时返回的动作，该类型为枚举。需要配合[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)的  
[onPrepareTermination](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onpreparetermination)或者  
[onPrepareTerminationAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onprepareterminationasync)方法使用。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum PrepareTermination--><!--Device-AbilityConstant-export enum PrepareTermination-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## TERMINATE_IMMEDIATELY

```TypeScript
TERMINATE_IMMEDIATELY = 0
```

表示立即执行结束动作，默认值。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PrepareTermination-TERMINATE_IMMEDIATELY = 0--><!--Device-PrepareTermination-TERMINATE_IMMEDIATELY = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CANCEL

```TypeScript
CANCEL = 1
```

表示取消结束动作。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PrepareTermination-CANCEL = 1--><!--Device-PrepareTermination-CANCEL = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

