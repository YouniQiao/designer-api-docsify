# addProcessorFromConfig

## addProcessorFromConfig

```TypeScript
function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>
```

Adds the configuration information of the data processor. The configuration file contains information such as the name of the event received by the data processor. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>--><!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| processorName | string | Yes | Name of a data processor. It can contain only letters, digits,underscores (\_\_\_ESCAPED\_UNDERSCORE\_\_\_), and dollar signs (\_\_\_ESCAPED\_DOLLAR\_\_\_). It cannot start with a digit and cannot exceed 256 characters. |
| configName | string | No | Name of the data processor configuration. The corresponding configuration can be loaded from the configuration file. The default value is **SDK\_\_\_ESCAPED\_UNDERSCORE\_\_\_OCG**. It can contain only letters, digits, underscores (\_\_\_ESCAPED\_UNDERSCORE\_\_\_), and dollar signs (\_\_\_ESCAPED\_DOLLAR\_\_\_). It cannot start with a digit and cannot exceed 256characters. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;long&gt; | Promise that returns the unique ID of the added event data processor, which can be used |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [11105001](../errorcode-hiappevent.md#11105001-invalid-parameter-value) | Invalid parameter value. Possible causes: 1. Incorrect parameter length;2. Incorrect parameter format. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addProcessorFromConfig("test_name").then((processorId) => {
  hilog.info(0x0000, 'hiAppEvent', `Succeeded in adding processor from config, processorId=${processorId}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to add processor from config, code: ${err.code}, message: ${err.message}`);
});
```

