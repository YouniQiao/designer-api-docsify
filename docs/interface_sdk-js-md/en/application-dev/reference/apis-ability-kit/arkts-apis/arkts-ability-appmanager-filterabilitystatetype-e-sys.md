# FilterAbilityStateType (System API)

表示要监听的Ability状态，该类型为枚举。可配合[AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md)过滤想要监听的Ability状态。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-appManager-export enum FilterAbilityStateType--><!--Device-appManager-export enum FilterAbilityStateType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## CREATE

```TypeScript
CREATE = 1 << 0
```

Ability正在创建中，对应  
[Ability状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability状态)中的ABILITY_STATE_CREATE。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-CREATE = 1 << 0--><!--Device-FilterAbilityStateType-CREATE = 1 << 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## FOREGROUND

```TypeScript
FOREGROUND = 1 << 1
```

Ability处于前台，对应  
[Ability状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability状态)中的ABILITY_STATE_FOREGROUND。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-FOREGROUND = 1 << 1--><!--Device-FilterAbilityStateType-FOREGROUND = 1 << 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## BACKGROUND

```TypeScript
BACKGROUND = 1 << 2
```

Ability处于后台，对应  
[Ability状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability状态)中的ABILITY_STATE_BACKGROUND。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-BACKGROUND = 1 << 2--><!--Device-FilterAbilityStateType-BACKGROUND = 1 << 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## DESTROY

```TypeScript
DESTROY = 1 << 3
```

Ability已经销毁，对应  
[Ability状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability状态)中的ABILITY_STATE_TERMINATED。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-DESTROY = 1 << 3--><!--Device-FilterAbilityStateType-DESTROY = 1 << 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

