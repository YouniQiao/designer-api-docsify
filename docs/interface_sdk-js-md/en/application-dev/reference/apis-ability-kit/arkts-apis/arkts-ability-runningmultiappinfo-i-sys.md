# RunningMultiAppInfo (System API)

定义应用多开在运行态的结构信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RunningMultiAppInfo--><!--Device-unnamed-export interface RunningMultiAppInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用的包名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RunningMultiAppInfo-bundleName: string--><!--Device-RunningMultiAppInfo-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## mode

```TypeScript
mode: MultiAppMode
```

应用多开模式。

**Type:** [MultiAppMode](arkts-ability-multiappmode-e-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RunningMultiAppInfo-mode: MultiAppMode--><!--Device-RunningMultiAppInfo-mode: MultiAppMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## runningAppClones

```TypeScript
runningAppClones?: Array<RunningAppClone>
```

特定包名在运行态的分身应用信息。

**Type:** Array&lt;[RunningAppClone](arkts-ability-runningappclone-i-sys.md)&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RunningMultiAppInfo-runningAppClones?: Array<RunningAppClone>--><!--Device-RunningMultiAppInfo-runningAppClones?: Array<RunningAppClone>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## runningMultiInstances

```TypeScript
runningMultiInstances?: Array<RunningMultiInstanceInfo>
```

特定包名在运行态的多实例应用信息。

**Type:** Array&lt;[RunningMultiInstanceInfo](arkts-ability-runningmultiinstanceinfo-i-sys.md)&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-RunningMultiAppInfo-runningMultiInstances?: Array<RunningMultiInstanceInfo>--><!--Device-RunningMultiAppInfo-runningMultiInstances?: Array<RunningMultiInstanceInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

