# IPrefetcher

该接口用于提供预加载操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface IPrefetcher<T>--><!--Device-unnamed-export interface IPrefetcher<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from 'kits/@kit.ArkUI';
```

## setDataSource

```TypeScript
setDataSource(dataSource: IDataSourcePrefetching<T>): void
```

设置prefetcher对象的数据源。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void--><!--Device-IPrefetcher-setDataSource(dataSource: IDataSourcePrefetching<T>): void-End-->

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

<!--Device-IPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void--><!--Device-IPrefetcher-visibleAreaChanged(minVisible: int, maxVisible: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| minVisible | int | Yes | 显示范围内第一个元素的序号。 |
| maxVisible | int | Yes | 显示范围内最后一个元素的序号。 |

