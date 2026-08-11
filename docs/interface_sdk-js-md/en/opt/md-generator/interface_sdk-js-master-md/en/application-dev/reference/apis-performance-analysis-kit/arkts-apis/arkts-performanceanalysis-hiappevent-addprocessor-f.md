# addProcessor

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addProcessor

```TypeScript
function addProcessor(processor: Processor): number
```

Adds the configuration information of the data processor, such as the event name received by it.

This is a synchronous API and involves time-consuming operations. To ensure performance, you are advised to use the asynchronous API [addProcessorFromConfig](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md#addprocessorfromconfig) or use a child thread.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function addProcessor(processor: Processor): long--><!--Device-hiAppEvent-function addProcessor(processor: Processor): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| processor | [Processor](arkts-performanceanalysis-hiappevent-processor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let processor: hiAppEvent.Processor = {
    name: 'analytics_demo'
  };
  let id: number = hiAppEvent.addProcessor(processor);
  hilog.info(0x0000, 'hiAppEvent', `addProcessor event was successful, id=${id}`);
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to addProcessor event, code=${error.code}`);
}
```
