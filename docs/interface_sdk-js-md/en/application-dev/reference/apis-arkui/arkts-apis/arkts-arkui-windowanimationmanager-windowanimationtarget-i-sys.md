# WindowAnimationTarget (System API)

动画目标窗口，用来实现动画。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-windowAnimationManager-export interface WindowAnimationTarget--><!--Device-windowAnimationManager-export interface WindowAnimationTarget-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { windowAnimationManager } from 'kits/@kit.ArkUI';
```

## abilityName

```TypeScript
readonly abilityName: string
```

/* 动画目标窗口所对应的Ability名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WindowAnimationTarget-readonly abilityName: string--><!--Device-WindowAnimationTarget-readonly abilityName: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## bundleName

```TypeScript
readonly bundleName: string
```

动画目标窗口所对应的包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WindowAnimationTarget-readonly bundleName: string--><!--Device-WindowAnimationTarget-readonly bundleName: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## missionId

```TypeScript
readonly missionId: int
```

/* 任务ID，多任务中用于与ability进行匹配。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WindowAnimationTarget-readonly missionId: int--><!--Device-WindowAnimationTarget-readonly missionId: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## windowBounds

```TypeScript
readonly windowBounds: RRect
```

/* 动画目标窗口所对应的实际大小。

**Type:** [RRect](arkts-arkui-windowanimationmanager-rrect-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WindowAnimationTarget-readonly windowBounds: RRect--><!--Device-WindowAnimationTarget-readonly windowBounds: RRect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

