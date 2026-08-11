# getGraphicsMemorySummary

## getGraphicsMemorySummary

```TypeScript
function getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>
```

��ȡӦ���Դ����ݣ�ʹ��Promise�����첽�ص���

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>--><!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| interval | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;GraphicsMemorySummary&gt; |

**错误码：**

| 错误码ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-cpuusage统计异常) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemorySummary().then((ret: hidebug.GraphicsMemorySummary) => {
  console.info(`get graphicsMemory gl: ${ret.gl} graph: ${ret.graph}.`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}.`);
})
```
