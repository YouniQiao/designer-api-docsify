# DataProgressListener

```TypeScript
type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void
```

定义获取进度信息和数据的监听回调函数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unifiedDataChannel-type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void--><!--Device-unifiedDataChannel-type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progressInfo | [ProgressInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-progressinfo-i.md) | Yes | 定义进度上报的进度信息，用于接收拖拽任务的进度状态和进度百分比。包含progress（进度百分比，取值范围[-1-100]）和status（任务状态码） 两个字段，其中progress为-1表示获取数据失败，100表示获取数据完成。 |
| data | [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) \| null | Yes | 进度达到100时获取的数据，进度未到100时返回null。 |

