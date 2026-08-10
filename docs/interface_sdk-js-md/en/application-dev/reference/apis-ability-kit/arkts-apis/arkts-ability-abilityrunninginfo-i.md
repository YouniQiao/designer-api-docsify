# AbilityRunningInfo

AbilityRunningInfo是记录Ability运行信息和状态的数据结构，通过  
[getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md#getabilityrunninginfos)方法获取。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityRunningInfo--><!--Device-unnamed-export interface AbilityRunningInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ability

```TypeScript
ability: ElementName
```

Ability的ElementName信息。

**Type:** [ElementName](arkts-ability-elementname-i.md)

**Default:** the ohos.bundleManager.ElementName object of the ability.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-ability: ElementName--><!--Device-AbilityRunningInfo-ability: ElementName-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityState

```TypeScript
abilityState: abilityManager.AbilityState
```

Ability的状态。

**Type:** abilityManager.AbilityState

**Default:** Enumerates state of the ability state info

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-abilityState: abilityManager.AbilityState--><!--Device-AbilityRunningInfo-abilityState: abilityManager.AbilityState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

进程ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** process id

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-pid: int--><!--Device-AbilityRunningInfo-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

进程的名称。

**Type:** string

**Default:** the name of the process

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-processName: string--><!--Device-AbilityRunningInfo-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## startTime

```TypeScript
startTime: long
```

Ability的启动时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Default:** ability start time

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-startTime: long--><!--Device-AbilityRunningInfo-startTime: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

所属应用程序的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** user id

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityRunningInfo-uid: int--><!--Device-AbilityRunningInfo-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

