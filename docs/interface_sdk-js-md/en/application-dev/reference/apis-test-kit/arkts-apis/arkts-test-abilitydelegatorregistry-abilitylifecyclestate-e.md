# AbilityLifecycleState

Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](arkts-test-abilitydelegatorregistry-abilitydelegator-t.md)的  
[getAbilityState(ability)](../../apis-ability-kit/arkts-apis/arkts-ability-abilitydelegator-i.md/arkts-ability-abilitydelegator-i.md#getabilitystate)方法返回不同ability生命周期。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-abilityDelegatorRegistry-export enum AbilityLifecycleState--><!--Device-abilityDelegatorRegistry-export enum AbilityLifecycleState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## UNINITIALIZED

```TypeScript
UNINITIALIZED = 0
```

表示Ability处于无效状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleState-UNINITIALIZED = 0--><!--Device-AbilityLifecycleState-UNINITIALIZED = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CREATE

```TypeScript
CREATE = 1
```

表示Ability处于已创建状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleState-CREATE = 1--><!--Device-AbilityLifecycleState-CREATE = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## FOREGROUND

```TypeScript
FOREGROUND = 2
```

表示Ability处于前台状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleState-FOREGROUND = 2--><!--Device-AbilityLifecycleState-FOREGROUND = 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## BACKGROUND

```TypeScript
BACKGROUND = 3
```

表示Ability处于后台状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleState-BACKGROUND = 3--><!--Device-AbilityLifecycleState-BACKGROUND = 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## DESTROY

```TypeScript
DESTROY = 4
```

表示Ability处于已销毁状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleState-DESTROY = 4--><!--Device-AbilityLifecycleState-DESTROY = 4-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

