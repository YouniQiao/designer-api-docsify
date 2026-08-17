# IDataSource

Developers need to implement this interface to provide data to LazyForEach component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface IDataSource--><!--Device-unnamed-export interface IDataSource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getData

```TypeScript
getData(index: int): T
```

Return the data of index.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-getData(index: int): T--><!--Device-IDataSource-getData(index: int): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## registerDataChangeListener

```TypeScript
registerDataChangeListener(listener: DataChangeListener): void
```

Register data change listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [DataChangeListener](arkts-na-lazyforeach-datachangelistener-i.md) | Yes |  |

## totalCount

```TypeScript
totalCount(): int
```

Total data count.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-totalCount(): int--><!--Device-IDataSource-totalCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int |  |

## unregisterDataChangeListener

```TypeScript
unregisterDataChangeListener(listener: DataChangeListener): void
```

Unregister data change listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [DataChangeListener](arkts-na-lazyforeach-datachangelistener-i.md) | Yes |  |

