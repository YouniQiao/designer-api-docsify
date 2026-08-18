# LastExitDetailInfo

Describes the key runtime information of the process where the ability last exited.

**Since:** 23

<!--Device-AbilityConstant-export interface LastExitDetailInfo--><!--Device-AbilityConstant-export interface LastExitDetailInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
```

## exitMsg

```TypeScript
exitMsg: string
```

Reason why the process was killed.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-exitMsg: string--><!--Device-LastExitDetailInfo-exitMsg: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## exitSubReason

```TypeScript
exitSubReason: number
```

Specific reason for the last exit of the ability.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-exitSubReason: int--><!--Device-LastExitDetailInfo-exitSubReason: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## killReason

```TypeScript
killReason?: string
```

Indecates kill reason message.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-LastExitDetailInfo-killReason?: string--><!--Device-LastExitDetailInfo-killReason?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: number
```

ID of the process where the ability last exited.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-pid: int--><!--Device-LastExitDetailInfo-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

Name of the process.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-processName: string--><!--Device-LastExitDetailInfo-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processState

```TypeScript
processState?: appManager.ProcessState
```

Process status of the ability when it last exited.

**Type:** appManager.ProcessState

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-processState?: appManager.ProcessState--><!--Device-LastExitDetailInfo-processState?: appManager.ProcessState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pss

```TypeScript
pss: number
```

Actual physical memory usage of the process, in KB.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-pss: int--><!--Device-LastExitDetailInfo-pss: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## rss

```TypeScript
rss: number
```

Actual memory usage of the process, in KB.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-rss: int--><!--Device-LastExitDetailInfo-rss: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## timestamp

```TypeScript
timestamp: number
```

Exact time when the ability last exited.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-timestamp: long--><!--Device-LastExitDetailInfo-timestamp: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: number
```

UID of the application.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LastExitDetailInfo-uid: int--><!--Device-LastExitDetailInfo-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
