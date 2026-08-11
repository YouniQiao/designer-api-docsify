# setEventConfig

## setEventConfig

```TypeScript
function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>
```

事件相关的配置参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件名称，设置事件相关的配置参数。

不同的事件有不同的配置项，目前仅支持以下事件：

- MAIN_THREAD_JANK（参数配置详见  
[主线程超时事件检测](../../../dfx/hiappevent-watcher-mainthreadjank-events.md#seteventconfig接口参数设置说明)）  
- APP_CRASH（参数配置详见[崩溃日志配置参数设置介绍](../../../dfx/hiappevent-watcher-crash-events.md#自定义规格设置)）  
- RESOURCE_OVERLIMIT（参数配置详见[资源泄漏事件检测](../../../dfx/hiappevent-watcher-resourceleak-events.md#自定义规格设置)）

> **说明：**
> 
> 从API版本26.0.0开始，configEventPolicy已支持本接口所有设置，推荐使用[configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md#configeventpolicy)。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-hiAppEvent-function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>--><!--Device-hiAppEvent-function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| config | Record&lt;string, ParamType&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

以下示例用于模拟配置MAIN_THREAD_JANK事件的采集堆栈自定义参数：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "log_type": "1",
  "sample_interval": "100",
  "ignore_startup_time": "11",
  "sample_count": "21",
  "report_times_per_app": "3"
};
hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `Successfully set sampling stack parameters.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to set sample stack value. Code: ${err.code}, message: ${err.message}`);
});
```
