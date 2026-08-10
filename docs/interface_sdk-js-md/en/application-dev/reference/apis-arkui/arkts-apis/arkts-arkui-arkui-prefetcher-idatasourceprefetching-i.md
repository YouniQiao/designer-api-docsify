# IDataSourcePrefetching

用于实现具有预加载能力的LazyForEach数据源。

**Inheritance/Implementation:** IDataSourcePrefetching extends [IDataSource<T>](IDataSource<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IDataSourcePrefetching<T> extends IDataSource<T>--><!--Device-unnamed-export declare interface IDataSourcePrefetching<T> extends IDataSource<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
default cancel(index: int): Promise<void> | undefined
```

取消指定数据项的预加载。该方法可以为同步，也可以为异步。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSourcePrefetching-default cancel(index: int): Promise<void> | undefined--><!--Device-IDataSourcePrefetching-default cancel(index: int): Promise<void> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 指定项的序号。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

## prefetch

```TypeScript
prefetch(index: int): Promise<void> | undefined
```

预加载数据源中的指定项。该方法可以为同步，也可以为异步。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSourcePrefetching-prefetch(index: int): Promise<void> | undefined--><!--Device-IDataSourcePrefetching-prefetch(index: int): Promise<void> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 指定项的序号。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

