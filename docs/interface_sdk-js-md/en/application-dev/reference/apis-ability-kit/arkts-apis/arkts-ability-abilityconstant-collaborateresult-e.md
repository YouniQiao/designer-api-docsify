# CollaborateResult

应用协同状态，该类型为枚举。用于多设备场景下，调用方应用拉起协同方应用时，协同方应用是否接受协同。需要配合UIAbility的  
[onCollaborate()](arkts-ability-app-ability-uiability-uiability-c.md#oncollaborate)方法进行设置。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum CollaborateResult--><!--Device-AbilityConstant-export enum CollaborateResult-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ACCEPT

```TypeScript
ACCEPT = 0
```

接受协同。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CollaborateResult-ACCEPT = 0--><!--Device-CollaborateResult-ACCEPT = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## REJECT

```TypeScript
REJECT = 1
```

拒绝协同。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CollaborateResult-REJECT = 1--><!--Device-CollaborateResult-REJECT = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

