# DataLoadHandler

```TypeScript
type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null
```

Defines a handler for lazy data loading. The data sender can dynamically generate data based on the information passed by the data receiver to implement more flexible and precise data interaction policies.

This API is a synchronous function and is applicable to simple service logic. If the service logic is complex and the execution time lasts for more than 3s, you are advised to use the asynchronous handler   
[DelayedDataLoadHandler](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md#DelayedDataLoadHandler).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unifiedDataChannel-type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null--><!--Device-unifiedDataChannel-type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [acceptableInfo](arkts-arkdata-unifieddatachannel-getdataparams-i.md) | [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| UnifiedData \| null |
