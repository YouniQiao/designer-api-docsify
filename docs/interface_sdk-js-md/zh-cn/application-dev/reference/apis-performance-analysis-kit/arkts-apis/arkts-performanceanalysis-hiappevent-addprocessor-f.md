# addProcessor

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addProcessor

```TypeScript
function addProcessor(processor: Processor): number
```

添加数据处理者配置信息，用于配置处理者接收的事件名等信息。事件发生后处理者可以接收事件。该接口为同步接口，包含耗时操作。为了确保性能，建议使用[addProcessorFromConfig](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md)异步接口或者交由子线程执行。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| processor | [Processor](arkts-performanceanalysis-hiappevent-processor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
