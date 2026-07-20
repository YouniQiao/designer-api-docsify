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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progressInfo | [ProgressInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-progressinfo-i.md) | Yes | Progress information to report.  |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) \| null | Yes | Data obtained when the progress reaches 100. If the progress does not reach 10 0, **null** is returned.  |

