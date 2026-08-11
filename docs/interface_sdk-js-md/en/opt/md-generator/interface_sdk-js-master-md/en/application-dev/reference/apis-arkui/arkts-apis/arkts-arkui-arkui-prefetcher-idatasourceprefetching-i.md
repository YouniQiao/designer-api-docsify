# IDataSourcePrefetching

Extends the [IDataSource](../arkts-components/arkts-arkui-idatasource-i.md/arkts-arkui-idatasource-i.md) API to provide a data source that can be prefetched.

**Inheritance/Implementation:** IDataSourcePrefetching extends [IDataSource](../arkts-components/arkts-arkui-idatasource-i.md/arkts-arkui-idatasource-i.md)

**Since:** 12

<!--Device-unnamed-export interface IDataSourcePrefetching extends IDataSource--><!--Device-unnamed-export interface IDataSourcePrefetching extends IDataSource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel?(index: number): Promise<void> | void
```

Cancels the prefetching of a specified data item from the dataset. This API can be either synchronous or asynchronous. This API is optional. If the data source does not implement this API, the prefetching cancellation operation will not be performed.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IDataSourcePrefetching-cancel?(index: number): Promise<void> | void--><!--Device-IDataSourcePrefetching-cancel?(index: number): Promise<void> | void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## prefetch

```TypeScript
prefetch(index: number): Promise<void> | void
```

Prefetches a specified data item from the dataset. This API can be either synchronous or asynchronous. When the visible area changes, the prefetching algorithm calls this API if it determines that the data item about to enter the visible area needs to be prefetched.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IDataSourcePrefetching-prefetch(index: number): Promise<void> | void--><!--Device-IDataSourcePrefetching-prefetch(index: number): Promise<void> | void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
