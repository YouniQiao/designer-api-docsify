# OnSaveResult

保存应用数据的结果，该类型为枚举。配合UIAbility的  
[onSaveState()](arkts-ability-app-ability-uiability-uiability-c.md#onsavestate)方法使用，可以实现[UIAbility备份恢复](../../../application-models/ability-recover-guideline.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum OnSaveResult--><!--Device-AbilityConstant-export enum OnSaveResult-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ALL_AGREE

```TypeScript
ALL_AGREE = 0
```

总是同意保存状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-ALL_AGREE = 0--><!--Device-OnSaveResult-ALL_AGREE = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CONTINUATION_REJECT

```TypeScript
CONTINUATION_REJECT = 1
```

拒绝迁移保存状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-CONTINUATION_REJECT = 1--><!--Device-OnSaveResult-CONTINUATION_REJECT = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CONTINUATION_MISMATCH

```TypeScript
CONTINUATION_MISMATCH = 2
```

迁移不匹配。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-CONTINUATION_MISMATCH = 2--><!--Device-OnSaveResult-CONTINUATION_MISMATCH = 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## RECOVERY_AGREE

```TypeScript
RECOVERY_AGREE = 3
```

同意恢复保存状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-RECOVERY_AGREE = 3--><!--Device-OnSaveResult-RECOVERY_AGREE = 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## RECOVERY_REJECT

```TypeScript
RECOVERY_REJECT = 4
```

拒绝恢复保存状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-RECOVERY_REJECT = 4--><!--Device-OnSaveResult-RECOVERY_REJECT = 4-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ALL_REJECT

```TypeScript
ALL_REJECT = 5
```

Always rejected to save the status.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OnSaveResult-ALL_REJECT = 5--><!--Device-OnSaveResult-ALL_REJECT = 5-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

