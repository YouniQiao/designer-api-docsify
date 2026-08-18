# startAsyncTrace

## 导入模块

```TypeScript
```

## startAsyncTrace

```TypeScript
function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string,
      customArgs?: string): void
```

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。 如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startAsyncTrace传入的taskId需不同。 如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace) 中的示例。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: int, customCategory: string,      customArgs?: string): void--><!--Device-hiTraceMeter-function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: int, customCategory: string,      customArgs?: string): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | 是 |
| name | string | 是 |
| taskId | number | 是 |
| customCategory | string | 是 |
| customArgs | string | 否 |

**示例**

```TypeScript
// 不需要customCategory参数时，可传入空字符串
// 不需要customArgs参数时，可不传入该参数或传入空字符串
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "", "");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 2, "");
// 多个键值对用逗号分隔
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 3, "categoryTest", "key1=value");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 4, "categoryTest", "key1=value1,key2=value2");
```
