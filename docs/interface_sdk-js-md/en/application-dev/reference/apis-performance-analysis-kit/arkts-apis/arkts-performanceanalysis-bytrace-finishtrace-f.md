# finishTrace

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: number): void
```

标记一个时间片跟踪事件的结束。

> **说明：**
> 
> finishTrace的name和taskId必须与流程开始的startTrace对应参数值一致。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.hiTraceMeter.finishTrace

<!--Device-bytrace-function finishTrace(name: string, taskId: number): void--><!--Device-bytrace-function finishTrace(name: string, taskId: number): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 时间片跟踪任务名称，必须与startTrace调用时的name参数值一致。 |
| taskId | number | Yes | 时间片跟踪任务id，必须与startTrace调用时的taskId参数值一致。 |

## Examples

```TypeScript
bytrace.finishTrace("myTestFunc", 1);
```

```TypeScript
// Start trace tasks with the same name concurrently.
bytrace.startTrace("myTestFunc", 1);
// Service flow...
bytrace.startTrace("myTestFunc", 2);  // The second trace task starts while the first task is still running. The first and second tasks have the same name but different task IDs.
// Service flow...
bytrace.finishTrace("myTestFunc", 1);
// Service flow...
bytrace.finishTrace("myTestFunc", 2);
```

```TypeScript
// Start trace tasks with the same name in serial mode.
bytrace.startTrace("myTestFunc", 1);
// Service flow...
bytrace.finishTrace("myTestFunc", 1);  // The first trace task ends.
// Service flow...
bytrace.startTrace("myTestFunc", 1);   // The second trace task starts after the first task ends. The two tasks have the same name and task ID.
// Service flow...
bytrace.finishTrace("myTestFunc", 1);
```

