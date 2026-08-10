# TaskInfo

任务的内部信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-class TaskInfo--><!--Device-taskpool-class TaskInfo-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## duration

```TypeScript
duration?: number
```

任务执行至当前所用的时间，默认为0，单位为ms。当返回为0时，表示任务未执行；返回为空时，表示没有任务执行。不建议修改此值。&lt;br/&gt;从API version 11开始，该接口支持在原子化服务中使用。

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

任务的名字，不建议修改此值。&lt;br/&gt;从API version 12开始，该接口支持在原子化服务中使用。

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

任务的状态。state标识任务的当前状态，不建议修改此值。&lt;br/&gt;从API version 11开始，该接口支持在原子化服务中使用。

**Type:** [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md)

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

任务的ID。任务的标识符，系统默认提供全局唯一值，不建议修改此值。&lt;br/&gt;从API version 11开始，该接口支持在原子化服务中使用。

**Type:** number

**Default:** 0

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskInfo-taskId: number--><!--Device-TaskInfo-taskId: number-End-->

**System capability:** SystemCapability.Utils.Lang

