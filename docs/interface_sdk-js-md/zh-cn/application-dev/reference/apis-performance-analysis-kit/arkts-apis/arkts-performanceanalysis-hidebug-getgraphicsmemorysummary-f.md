# getGraphicsMemorySummary

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGraphicsMemorySummary

```TypeScript
function getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>
```

获取应用显存数据，使用Promise进行异步回调。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interval | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[GraphicsMemorySummary](arkts-performanceanalysis-hidebug-graphicsmemorysummary-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-cpuusage统计异常) |
