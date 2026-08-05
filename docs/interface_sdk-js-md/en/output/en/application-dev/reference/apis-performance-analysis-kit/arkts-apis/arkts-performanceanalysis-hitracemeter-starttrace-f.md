# startTrace

## startTrace

```TypeScript
function startTrace(name: string, taskId: int): void
```

Starts an asynchronous trace. If multiple trace tasks with the same name need to be performed at the same time or a trace needs to be performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks with the same name are not performed at the same time, the same taskId can be used. For a specific example, see [finishTrace()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Since API version 19, you are advised to use [startAsyncTrace()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, which must be used together with [finishAsyncTrace()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. In this way, you can specify the trace output level and category.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the trace to start.The maximum length of a trace record is 512 bytes. The excess part will be truncated. It is recommended that the length of this parameter be less than or equal to 420 bytes. |
| taskId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Task ID.It is used to distinguish multiple tasks with the same name. Ensure that the task IDs of concurrently executed tasks with the same name are unique. |

**Example**

```TypeScript
hiTraceMeter.startTrace("myTestFunc", 1);
```

