# setEventConfig

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setEventConfig

```TypeScript
function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>
```

事件相关的配置参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件名称，设置事件相关的配置参数。不同的事件有不同的配置项，目前仅支持以下事件：  
- MAIN_THREAD_JANK（参数配置详见  
[主线程超时事件检测](../../../dfx/hiappevent-watcher-mainthreadjank-events.md#seteventconfig接口参数设置说明)）  
- APP_CRASH（参数配置详见[崩溃日志配置参数设置介绍](../../../dfx/hiappevent-watcher-crash-events.md#自定义规格设置)）  
- RESOURCE_OVERLIMIT（参数配置详见[资源泄漏事件检测](../../../dfx/hiappevent-watcher-resourceleak-events.md#自定义规格设置)）

> **说明：**&gt;
> 从API版本26.0.0开始，configEventPolicy已支持本接口所有设置，推荐使用[configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md)。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| config | Record&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
