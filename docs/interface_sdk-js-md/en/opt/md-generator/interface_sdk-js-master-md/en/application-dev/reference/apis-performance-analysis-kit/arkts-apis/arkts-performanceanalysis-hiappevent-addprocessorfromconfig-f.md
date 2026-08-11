# addProcessorFromConfig

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addProcessorFromConfig

```TypeScript
function addProcessorFromConfig(processorName: string, configName?: string): Promise<number>
```

Adds the configuration information of the data processor. The configuration file contains information such as the name of the event received by the data processor. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>--><!--Device-hiAppEvent-function addProcessorFromConfig(processorName: string, configName?: string): Promise<long>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| processorName | string | Yes |
| configName | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11105001](../errorcode-hiappevent.md#11105001-invalid-parameter-value) |

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
