# IDataSource

LazyForEach的数据源。ArkTS-Sta中IDataSource强制要求声明`&lt;T&gt;`类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface IDataSource<T>--><!--Device-unnamed-export interface IDataSource<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getData

```TypeScript
getData(index: int): T
```

获取索引值index对应的数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-getData(index: int): T--><!--Device-IDataSource-getData(index: int): T-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T | 获取索引值index对应的数据，由数据源决定具体类型。 |

## registerDataChangeListener

```TypeScript
registerDataChangeListener(listener: DataChangeListener): void
```

注册数据改变的监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [DataChangeListener](../arkts-components/arkts-arkui-datachangelistener-i.md) | Yes |  |

## totalCount

```TypeScript
totalCount(): int
```

获得数据总数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-totalCount(): int--><!--Device-IDataSource-totalCount(): int-End-->

**Return value:**

| Type | Description |
| --- | --- |
| int | 获得数据总数，由数据源决定实际大小。 |

## unregisterDataChangeListener

```TypeScript
unregisterDataChangeListener(listener: DataChangeListener): void
```

注销数据改变的监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [DataChangeListener](../arkts-components/arkts-arkui-datachangelistener-i.md) | Yes |  |

