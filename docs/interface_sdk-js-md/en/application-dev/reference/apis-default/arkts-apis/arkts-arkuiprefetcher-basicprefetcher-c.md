# BasicPrefetcher

Basic implementation of [IPrefetcher](arkts-arkuiprefetcher-iprefetcher-i.md). It provides an intelligent data prefetching algorithm to make decisions about which data items should be prefetched in response to the real-time changes of visible on-screen area and changes in the duration of the prefetching. It also determines which prefetch requests should be canceled based on user scrolling actions.

**Inheritance/Implementation:** BasicPrefetcher implements IPrefetcher<T>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class BasicPrefetcher--><!--Device-unnamed-export declare class BasicPrefetcher-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(dataSource?: IDataSourcePrefetching<T>)
```

Constructs a basic prefetcher instance and optionally sets the data source.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)--><!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](arkts-arkuiprefetcher-idatasourceprefetching-i.md)&lt;T&gt; | No | Data source that supports prefetching. |

## setDataSource

```TypeScript
setDataSource(dataSource: IDataSourcePrefetching<T>): void
```

Sets the data source to bind to this prefetcher.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void--><!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](arkts-arkuiprefetcher-idatasourceprefetching-i.md)&lt;T&gt; | Yes | Data source that supports prefetching. |

## visibleAreaChanged

```TypeScript
visibleAreaChanged(minVisible: int, maxVisible: int): void
```

Call this method when the visible area changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void--><!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minVisible | int | Yes | Index of the first visible data item. |
| maxVisible | int | Yes | Index of the last visible data item. |

