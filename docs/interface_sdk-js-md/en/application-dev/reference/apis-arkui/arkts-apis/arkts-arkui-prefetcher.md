# @ohos.arkui.Prefetcher(Prefetching)

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, IPrefetcher, BasicPrefetcher } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BasicPrefetcher(Prefetching)](arkts-arkui-arkui-prefetcher-basicprefetcher-c.md) | **BasicPrefetcher** is a fundamental implementation of **IPrefetcher**. It offers an intelligent data prefetching algorithm that decides the data items to prefetch based on real-time changes in the visible area on the screen and variations in the prefetch duration. It can also determine the prefetch requests to be canceled based on the user's scrolling actions.  **BasicPrefetcher** objects do not support JSON serialization. |

### Interfaces

| Name | Description |
| --- | --- |
| [IDataSourcePrefetching(Prefetching)](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md) | Extends the IDataSource API to provide a data source that can be prefetched. |
| [IPrefetcher(Prefetching)](arkts-arkui-arkui-prefetcher-iprefetcher-i.md) | Provides the prefetching capability. It works with **LazyForEach** to prefetch data items when users swipe through container components such as **List** and **Grid**, improving user browsing experience. |

