# finishTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'hiTraceMeter';
```

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: int): void
```

Stops an asynchronous trace. To stop a trace, the values of name and task ID in **finishTrace** must be the same as those in [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#startTrace). Since API version 19, you are advised to use [finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishAsyncTrace), which must be used together with [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startAsyncTrace).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function finishTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function finishTrace(name: string, taskId: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the trace to start. |
| taskId | int | Yes | Task ID. |

## Examples

```TypeScript
hiTraceMeter.finishTrace("myTestFunc", 1);
```

```TypeScript
// Start trace tasks with the same name concurrently.
hiTraceMeter.startTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.startTrace("myTestFunc", 2);  // Start the second trace with the same name while the first task is still running. The tasks are running concurrently and therefore their taskId must be different.
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 2);
```

```TypeScript
// Start trace tasks with the same name in serial mode.
hiTraceMeter.startTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);  // End the first trace task.
// Service flow...
hiTraceMeter.startTrace("myTestFunc", 1);   // Start the second trace task with the same name in serial mode.
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);
```

