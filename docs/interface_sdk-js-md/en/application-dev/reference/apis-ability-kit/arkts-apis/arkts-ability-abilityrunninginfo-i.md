# AbilityRunningInfo

AbilityRunningInfo is a struct that records the running information and state of an ability. It is obtained through [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md#getAbilityRunningInfos).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface AbilityRunningInfo--><!--Device-unnamed-export interface AbilityRunningInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ability

```TypeScript
ability: ElementName
```

Element name of the ability.

**Type:** [ElementName](arkts-ability-elementname-i.md)

**Default:** the ohos.bundleManager.ElementName object of the ability.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-ability: ElementName--><!--Device-AbilityRunningInfo-ability: ElementName-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityState

```TypeScript
abilityState: abilityManager.AbilityState
```

Ability state.

**Type:** abilityManager.AbilityState

**Default:** Enumerates state of the ability state info

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-abilityState: abilityManager.AbilityState--><!--Device-AbilityRunningInfo-abilityState: abilityManager.AbilityState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

Process ID.

**Type:** int

**Default:** process id

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-pid: int--><!--Device-AbilityRunningInfo-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

Process name.

**Type:** string

**Default:** the name of the process

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-processName: string--><!--Device-AbilityRunningInfo-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## startTime

```TypeScript
startTime: long
```

Ability start time.

**Type:** long

**Default:** ability start time

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-startTime: long--><!--Device-AbilityRunningInfo-startTime: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** int

**Default:** user id

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityRunningInfo-uid: int--><!--Device-AbilityRunningInfo-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

