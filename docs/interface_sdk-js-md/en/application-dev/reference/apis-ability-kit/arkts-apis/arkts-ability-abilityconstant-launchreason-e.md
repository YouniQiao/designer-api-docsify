# LaunchReason

Ability启动原因，该类型为枚举，可配合UIAbility的[onCreate(want, launchParam)](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)方法根据launchParam.launchReason的不同类型执行相应操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export enum LaunchReason--><!--Device-AbilityConstant-export enum LaunchReason-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

未知原因。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-UNKNOWN = 0--><!--Device-LaunchReason-UNKNOWN = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## START_ABILITY

```TypeScript
START_ABILITY = 1
```

通过  
[startAbility](arkts-ability-uiabilitycontext-c.md#startability)接口启动Ability。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-START_ABILITY = 1--><!--Device-LaunchReason-START_ABILITY = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CALL

```TypeScript
CALL = 2
```

通过[startAbilityByCall](arkts-ability-uiabilitycontext-c.md#startabilitybycall)接口启动Ability。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-CALL = 2--><!--Device-LaunchReason-CALL = 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CONTINUATION

```TypeScript
CONTINUATION = 3
```

跨端迁移启动Ability。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-CONTINUATION = 3--><!--Device-LaunchReason-CONTINUATION = 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## APP_RECOVERY

```TypeScript
APP_RECOVERY = 4
```

设置应用恢复后，应用故障时自动恢复启动Ability。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-APP_RECOVERY = 4--><!--Device-LaunchReason-APP_RECOVERY = 4-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## SHARE

```TypeScript
SHARE = 5
```

通过原子化服务分享启动Ability。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-SHARE = 5--><!--Device-LaunchReason-SHARE = 5-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## AUTO_STARTUP

```TypeScript
AUTO_STARTUP = 8
```

通过设置开机自启动来启动Ability。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LaunchReason-AUTO_STARTUP = 8--><!--Device-LaunchReason-AUTO_STARTUP = 8-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## INSIGHT_INTENT

```TypeScript
INSIGHT_INTENT = 9
```

通过洞察意图来启动Ability。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchReason-INSIGHT_INTENT = 9--><!--Device-LaunchReason-INSIGHT_INTENT = 9-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## PREPARE_CONTINUATION

```TypeScript
PREPARE_CONTINUATION = 10
```

跨端迁移提前启动Ability。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LaunchReason-PREPARE_CONTINUATION = 10--><!--Device-LaunchReason-PREPARE_CONTINUATION = 10-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## PRELOAD

```TypeScript
PRELOAD = 11
```

表明该UIAbility是通过预加载机制启动的。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LaunchReason-PRELOAD = 11--><!--Device-LaunchReason-PRELOAD = 11-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

