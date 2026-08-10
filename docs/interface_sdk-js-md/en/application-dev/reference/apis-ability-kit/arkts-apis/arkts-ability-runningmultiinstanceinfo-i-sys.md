# RunningMultiInstanceInfo (System API)

定义多实例应用在运行态的结构信息，通过appManager的  
[getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md#getrunningmultiappinfo)来获取。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RunningMultiInstanceInfo--><!--Device-unnamed-export interface RunningMultiInstanceInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## instanceKey

```TypeScript
instanceKey: string
```

多实例应用的唯一实例标识。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-RunningMultiInstanceInfo-instanceKey: string--><!--Device-RunningMultiInstanceInfo-instanceKey: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## pids

```TypeScript
pids: Array<int>
```

应用的进程ID集合。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-RunningMultiInstanceInfo-pids: Array<int>--><!--Device-RunningMultiInstanceInfo-pids: Array<int>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

表示应用程序的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-RunningMultiInstanceInfo-uid: int--><!--Device-RunningMultiInstanceInfo-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

