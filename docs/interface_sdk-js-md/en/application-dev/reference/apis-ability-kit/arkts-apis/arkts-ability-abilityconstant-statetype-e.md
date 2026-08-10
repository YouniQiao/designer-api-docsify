# StateType

保存应用数据场景原因，该类型为枚举。配合UIAbility的  
[onSaveState()](arkts-ability-app-ability-uiability-uiability-c.md#onsavestate)方法使用，可以实现[UIAbility备份恢复](../../../application-models/ability-recover-guideline.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum StateType--><!--Device-AbilityConstant-export enum StateType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CONTINUATION

```TypeScript
CONTINUATION = 0
```

应用迁移场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-StateType-CONTINUATION = 0--><!--Device-StateType-CONTINUATION = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## APP_RECOVERY

```TypeScript
APP_RECOVERY = 1
```

应用故障恢复场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-StateType-APP_RECOVERY = 1--><!--Device-StateType-APP_RECOVERY = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

