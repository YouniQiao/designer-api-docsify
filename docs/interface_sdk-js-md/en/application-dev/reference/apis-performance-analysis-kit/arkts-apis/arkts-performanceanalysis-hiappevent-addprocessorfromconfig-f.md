# addProcessorFromConfig

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## addProcessorFromConfig

```TypeScript
function addProcessorFromConfig(processorName: string, configName?: string): Promise<number>
```

<!--RP1-->Add the configuration information of the data processor and configure the information such as the event name received by the processor through the configuration file. After the event occurs, the processor can receive the event and use Promise asynchronous callback. <!--RP1End-->

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>--><!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processorName | string | Yes | <!--RP2-->Name of the data processor. The name can contain only uppercase letters, lowercase letters, digits, underscores(_), and dollar sign($), and cannot start with a digit. The length cannot exceed 256 characters. <!--RP2End--> |
| configName | string | No | <!--RP3-->Configuration name of the data processor. The corresponding configuration can be loaded from the configuration file. The default value is SDK_OCG. The value can contain only uppercase letters, lowercase letters, digits, underscores(_), and dollar sign($), and cannot start with a digit. The value cannot be empty and cannot exceed 256 characters. <!--RP3End--> |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise that returns the unique ID of the added event data processor, which can be used to remove the data processor. If the adding fails, error code **11105001** is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [11105001](../errorcode-hiappevent.md#11105001-invalid-parameter-value) | Invalid parameter value. Possible causes: 1. Incorrect parameter length;         2. Incorrect parameter format. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addProcessorFromConfig("test_name").then((processorId) => {
  hilog.info(0x0000, 'hiAppEvent', `Succeeded in adding processor from config, processorId=${processorId}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to add processor from config, code: ${err.code}, message: ${err.message}`);
});
```
