# addProcessorFromConfig

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addProcessorFromConfig

```TypeScript
function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>
```

添加数据处理者配置信息，通过配置文件配置处理者接收的事件名等信息，事件发生后处理者可以接收事件，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>--><!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processorName | string | Yes | 数据处理者的名称。名称只能包含大小写字母、数字、下划线和\\$，不能以数字开头，长度非空且不超过256个字符。 |
| configName | string | No | 数据处理者的配置名称，支持从配置文件中加载对应配置，默认为“SDK_OCG”。只能包含大小写字母、数字、下划线和\\$，不能以数字开头，长度非空且不 超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | Promise对象。返回添加的事件数据处理者的唯一ID，可用于移除该数据处理者。 添加失败返回11105001错误码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11105001 | Invalid parameter value. Possible causes: 1. Incorrect parameter length; 2. Incorrect parameter format. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addProcessorFromConfig("test_name").then((processorId) => {
  hilog.info(0x0000, 'hiAppEvent', `Succeeded in adding processor from config, processorId=${processorId}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to add processor from config, code: ${err.code}, message: ${err.message}`);
});
```

