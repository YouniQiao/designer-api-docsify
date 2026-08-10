# BasicPrefetcher

一种IPrefetcher的基础实现。此prefetcher提供了一种智能预加载算法，可以根据显示区域的实时变化以及预加载耗时的变化来确定预加载范围并加载数据项，并且可以根据用户的滚动操作来取消相应数据项的预加载请求。

**Inheritance/Implementation:** BasicPrefetcher implements [IPrefetcher<T>](IPrefetcher<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BasicPrefetcher<T> implements IPrefetcher<T>--><!--Device-unnamed-export declare class BasicPrefetcher<T> implements IPrefetcher<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(dataSource?: IDataSourcePrefetching<T>)
```

构建一个基础的prefetcher，并在构建时可以按需设置数据源。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)--><!--Device-BasicPrefetcher-constructor(dataSource?: IDataSourcePrefetching<T>)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md)&lt;T&gt; | No | 支持预加载的数据源。 |

## setDataSource

```TypeScript
setDataSource(dataSource: IDataSourcePrefetching<T>): void
```

设置prefetcher对象的数据源。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void--><!--Device-BasicPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md)&lt;T&gt; | Yes | 支持预加载的数据源。 |

## visibleAreaChanged

```TypeScript
visibleAreaChanged(minVisible: int, maxVisible: int): void
```

通知prefetcher屏幕显示范围发生变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void--><!--Device-BasicPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minVisible | int | Yes | 显示范围内第一个元素的序号。 |
| maxVisible | int | Yes | 显示范围内最后一个元素的序号。 |

