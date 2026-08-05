# BasicPrefetcher

Basic implementation of \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. It provides an intelligent data prefetching algorithm to make decisions about which data items should be prefetched in response to the real-time changes of visible on-screen area and changes in the duration of the prefetching. It also determines which prefetch requests should be canceled based on user scrolling actions.

**Inheritance/Implementation:** BasicPrefetcher implements [IPrefetcher<T>](IPrefetcher<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BasicPrefetcher<T> implements IPrefetcher<T>--><!--Device-unnamed-export declare class BasicPrefetcher<T> implements IPrefetcher<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(dataSource?: IDataSourcePrefetching<T>)
```

Constructs a basic prefetcher instance and optionally sets the data source.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)--><!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | No | Data source that supports prefetching. |

## setDataSource

```TypeScript
setDataSource(dataSource: IDataSourcePrefetching<T>): void
```

Sets the data source to bind to this prefetcher.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void--><!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Data source that supports prefetching. |

## visibleAreaChanged

```TypeScript
visibleAreaChanged(minVisible: int, maxVisible: int): void
```

Call this method when the visible area changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void--><!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minVisible | int | Yes | Index of the first visible data item. |
| maxVisible | int | Yes | Index of the last visible data item. |

