# ContinueCallbackInfo (System API)

当前任务流转状态监听的回调信息，包含流转状态和流转信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-distributedMissionManager-interface ContinueCallbackInfo--><!--Device-distributedMissionManager-interface ContinueCallbackInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## info

```TypeScript
info: ContinuableInfo
```

表示当前任务的流转信息。

**Type:** [ContinuableInfo](arkts-ability-distributedmissionmanager-continuableinfo-t-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueCallbackInfo-info: ContinuableInfo--><!--Device-ContinueCallbackInfo-info: ContinuableInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## state

```TypeScript
state: ContinueState
```

表示当前任务的流转状态。

**Type:** [ContinueState](arkts-ability-abilityconstant-continuestate-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueCallbackInfo-state: ContinueState--><!--Device-ContinueCallbackInfo-state: ContinueState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

