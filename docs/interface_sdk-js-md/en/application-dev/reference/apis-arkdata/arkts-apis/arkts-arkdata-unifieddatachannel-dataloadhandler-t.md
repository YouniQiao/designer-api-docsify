# DataLoadHandler

```TypeScript
type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null
```

用于延迟加载数据的处理函数。支持数据发送方根据接收方传入的信息，动态生成数据，实现更灵活、精准的数据交互策略。

该处理函数为同步函数，适用于处理简单业务逻辑，若函数业务逻辑较复杂、执行时间较长（3s以上），推荐使用异步处理函数  
[DelayedDataLoadHandler](arkts-arkdata-unifieddatachannel-delayeddataloadhandler-t.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unifiedDataChannel-type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null--><!--Device-unifiedDataChannel-type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| acceptableInfo | [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md) | No | 表示数据接收方可以接收的数据类型和数量，默认为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) \| null | 当延迟处理函数触发时，返回根据接收方信息生成的UnifiedData对象，用于数据传输。若无法生成数据或生成失败则返回null。 |

