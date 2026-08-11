# startTrace

## startTrace

```TypeScript
function startTrace(name: string, taskId: number): void
```

标记一个异步跟踪耗时任务的开始。调用成功后，创建一条异步跟踪记录。

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startTrace传入的taskId需不同。

如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace)中的示例。

从API version 19开始，建议使用[startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace)接口（需与  
[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace)接口配套使用），以便分级控制跟踪输出与跟踪聚类。

**起始版本：** 8

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| taskId | number | 是 |

## 示例

```TypeScript
hiTraceMeter.startTrace("myTestFunc", 1);  // 开始异步跟踪任务
```
