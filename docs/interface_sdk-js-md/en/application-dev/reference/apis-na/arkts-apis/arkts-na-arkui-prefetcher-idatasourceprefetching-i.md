# IDataSourcePrefetching

Implement this interface to provide data prefetching for the LazyForEach component.

**Inheritance/Implementation:** IDataSourcePrefetching extends IDataSource<T>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IDataSourcePrefetching--><!--Device-unnamed-export declare interface IDataSourcePrefetching-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## cancel

```TypeScript
cancel(index: int): Promise<void> | undefined
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-IDataSourcePrefetching-cancel(index: int): Promise<void> | undefined--><!--Device-IDataSourcePrefetching-cancel(index: int): Promise<void> | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

## prefetch

```TypeScript
prefetch(index: int): Promise<void> | undefined
```

Prefetches data for the specified element in the data collection. This method can be either synchronous or asynchronous.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSourcePrefetching-prefetch(index: int): Promise<void> | undefined--><!--Device-IDataSourcePrefetching-prefetch(index: int): Promise<void> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the item in the collection. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; |  |

## default

```TypeScript
default
```

Cancels prefetching data for the specified element in the data collection. This method can be either synchronous or asynchronous.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDataSourcePrefetching-default--><!--Device-IDataSourcePrefetching-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

