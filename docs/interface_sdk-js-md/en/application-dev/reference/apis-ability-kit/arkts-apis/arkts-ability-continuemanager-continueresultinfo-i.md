# ContinueResultInfo

注册或注销回调函数返回的快速拉起的结果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-continueManager-interface ContinueResultInfo--><!--Device-continueManager-interface ContinueResultInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## Modules to Import

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## resultInfo

```TypeScript
resultInfo?: string
```

操作结果的说明。

此接口仅可在Stage模型下使用。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueResultInfo-resultInfo?: string--><!--Device-ContinueResultInfo-resultInfo?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## resultState

```TypeScript
resultState: ContinueStateCode
```

操作结果状态码。

**Type:** [ContinueStateCode](arkts-ability-continuemanager-continuestatecode-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinueResultInfo-resultState: ContinueStateCode--><!--Device-ContinueResultInfo-resultState: ContinueStateCode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

