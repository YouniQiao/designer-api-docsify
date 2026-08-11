# DataProgressListener

```TypeScript
type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void
```

Defines the callback used to return the data retrieval progress information and data obtained.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unifiedDataChannel-type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void--><!--Device-unifiedDataChannel-type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| progressInfo | [ProgressInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-progressinfo-i.md) | Yes |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) \| null | Yes |
