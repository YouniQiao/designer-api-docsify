# startTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startTrace

```TypeScript
function startTrace(name: string, taskId: number): void
```

Starts an asynchronous trace.

If multiple trace tasks with the same name need to be performed at the same time or a trace needs to be performed multiple times concurrently, different task IDs must be specified in **startTrace**.

If the trace tasks with the same name are not performed at the same time, the same taskId can be used. For a specific example, see [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace).

Since API version 19, you are advised to use [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace), which must be used together with [finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace). In this way, you can specify the trace output level and category.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| taskId | number | Yes |

## Examples

```TypeScript
hiTraceMeter.startTrace("myTestFunc", 1);
```
