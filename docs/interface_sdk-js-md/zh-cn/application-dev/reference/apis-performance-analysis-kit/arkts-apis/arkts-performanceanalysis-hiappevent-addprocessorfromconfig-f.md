# addProcessorFromConfig

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addProcessorFromConfig

```TypeScript
function addProcessorFromConfig(processorName: string, configName?: string): Promise<number>
```

添加数据处理者配置信息，通过配置文件配置处理者接收的事件名等信息，事件发生后处理者可以接收事件，使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| processorName | string | 是 |
| [configName](arkts-performanceanalysis-hiappevent-processor-i.md) | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [11105001](../errorcode-hiappevent.md#11105001-非法的参数值) |
