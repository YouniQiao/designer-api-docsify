# TaskInfo

Describes the internal information about a task.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-class TaskInfo--><!--Device-taskpool-class TaskInfo-End-->

**System capability:** SystemCapability.Utils.Lang

## duration

```TypeScript
duration?: number
```

Duration that the task has been executed, in ms. The default value is **0**. If the return value is **0**, the task is not running. If the return value is empty, no task is running. You are advised not to change the value.&lt; br&gt; This API can be used in atomic services since API version 11.

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskInfo-duration?: number--><!--Device-TaskInfo-duration?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## name

```TypeScript
name: string
```

Task name. You are advised not to change the value.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ This API can be used in atomic services since API version 12.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TaskInfo-name: string--><!--Device-TaskInfo-name: string-End-->

**System capability:** SystemCapability.Utils.Lang

## state

```TypeScript
state: State
```

Task state. You are advised not to change the value.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ This API can be used in atomic services since API version 11.

**Type:** State

**Default:** State::WAITING

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskInfo-state: State--><!--Device-TaskInfo-state: State-End-->

**System capability:** SystemCapability.Utils.Lang

## taskId

```TypeScript
taskId: number
```

Task ID, which is globally unique by default. You are advised not to change the value.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ This API can be used in atomic services since API version 11.

**Type:** number

**Default:** 0

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskInfo-taskId: number--><!--Device-TaskInfo-taskId: number-End-->

**System capability:** SystemCapability.Utils.Lang

