# setEventConfig

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

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

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-hiAppEvent-function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>--><!--Device-hiAppEvent-function setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 事件名称。 |
| config | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ParamType&gt; | Yes | 事件自定义参数对象。参数名和参数值规格定义如下： &lt;br&gt;- 参数名为string类型，要求非空，且参数名长度需在1024个字符以内。 &lt;br&gt;- 参数值为ParamType类型，参数值长度需在1024个字符以内。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3.Parameter verification failed. |

## Examples

The following example sets the collection stack parameters of the MAIN_THREAD_JANK event:

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

