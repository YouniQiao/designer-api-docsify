# LastExitDetailInfo

Describes the key runtime information of the process where the ability last exited.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export interface LastExitDetailInfo--><!--Device-AbilityConstant-export interface LastExitDetailInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AbilityConstant } from '@kit.AbilityKit';
```

## exitMsg

```TypeScript
exitMsg: string
```

Reason why the process was killed.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-exitMsg: string--><!--Device-LastExitDetailInfo-exitMsg: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## exitSubReason

```TypeScript
exitSubReason: int
```

Specific reason for the last exit of the ability.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-exitSubReason: int--><!--Device-LastExitDetailInfo-exitSubReason: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## killReason

```TypeScript
killReason?: string
```

Indecates kill reason message.

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-LastExitDetailInfo-killReason?: string--><!--Device-LastExitDetailInfo-killReason?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

ID of the process where the ability last exited.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-pid: int--><!--Device-LastExitDetailInfo-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

Name of the process.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-processName: string--><!--Device-LastExitDetailInfo-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processState

```TypeScript
processState?: appManager.ProcessState
```

Process status of the ability when it last exited.

**Type:** appManager.ProcessState

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LastExitDetailInfo-processState?: appManager.ProcessState--><!--Device-LastExitDetailInfo-processState?: appManager.ProcessState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pss

```TypeScript
pss: int
```

Actual physical memory usage of the process, in KB.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-pss: int--><!--Device-LastExitDetailInfo-pss: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## rss

```TypeScript
rss: int
```

Actual memory usage of the process, in KB.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-rss: int--><!--Device-LastExitDetailInfo-rss: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## timestamp

```TypeScript
timestamp: long
```

Exact time when the ability last exited.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-timestamp: long--><!--Device-LastExitDetailInfo-timestamp: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LastExitDetailInfo-uid: int--><!--Device-LastExitDetailInfo-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

