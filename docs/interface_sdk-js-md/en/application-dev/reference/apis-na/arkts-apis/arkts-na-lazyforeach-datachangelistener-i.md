# DataChangeListener

Data Change Listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface DataChangeListener--><!--Device-unnamed-export interface DataChangeListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDataAdd

```TypeScript
onDataAdd(index: int): void
```

Data added.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDataAdd(index: int): void--><!--Device-DataChangeListener-onDataAdd(index: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## onDataChange

```TypeScript
onDataChange(index: int): void
```

Called when there is a data change.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDataChange(index: int): void--><!--Device-DataChangeListener-onDataChange(index: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## onDataDelete

```TypeScript
onDataDelete(index: int): void
```

Data deleted.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDataDelete(index: int): void--><!--Device-DataChangeListener-onDataDelete(index: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

## onDataMove

```TypeScript
onDataMove(from: int, to: int): void
```

Data moved.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDataMove(from: int, to: int): void--><!--Device-DataChangeListener-onDataMove(from: int, to: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | int | Yes |  |
| to | int | Yes |  |

## onDataReloaded

```TypeScript
onDataReloaded(): void
```

Data ready.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDataReloaded(): void--><!--Device-DataChangeListener-onDataReloaded(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDatasetChange

```TypeScript
onDatasetChange(dataOperations: Array<DataOperation>): void
```

Called when multiple data changes occur.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeListener-onDatasetChange(dataOperations: Array<DataOperation>): void--><!--Device-DataChangeListener-onDatasetChange(dataOperations: Array<DataOperation>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataOperations | Array&lt;[DataOperation](arkts-na-dataoperation-t.md)&gt; | Yes |  |

