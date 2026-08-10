# GetDelayData

```TypeScript
type GetDelayData = (type: string) => UnifiedData
```

对UnifiedData的延迟封装，支持延迟获取数据。当数据接收方请求特定类型数据时，系统会触发此回调函数，数据发送方可在回调中动态生成数据，而非提前准备所有数据。当前只支持同设备剪贴板场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unifiedDataChannel-type GetDelayData = (type: string) => UnifiedData--><!--Device-unifiedDataChannel-type GetDelayData = (type: string) => UnifiedData-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 作为延迟数据类型的标识，用于区分不同类型的数据。取值见 [UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)， 如'general.plain-text'表示纯文本类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UnifiedData](../../apis-arkui/arkts-components/arkts-arkui-unifieddata-t.md) | 当延迟回调触发时，返回包含相应类型数据的UnifiedData对象，可用于跨应用数据共享和传输。 |

