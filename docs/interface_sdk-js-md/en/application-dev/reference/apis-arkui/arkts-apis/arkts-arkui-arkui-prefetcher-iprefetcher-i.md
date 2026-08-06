# IPrefetcher

Implement this interface to provide prefetcher logic.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface IPrefetcher<T>--><!--Device-unnamed-export interface IPrefetcher<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setDataSource

```TypeScript
setDataSource(dataSource: IDataSourcePrefetching<T>): void
```

Sets the data source to bind to this prefetcher.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void--><!--Device-IPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Data source that supports prefetching. |

## visibleAreaChanged

```TypeScript
visibleAreaChanged(minVisible: int, maxVisible: int): void
```

Call this method when the visible area boundaries were changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void--><!--Device-IPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minVisible | int | Yes | Index of the first visible data item. |
| maxVisible | int | Yes | Index of the last visible data item. |

