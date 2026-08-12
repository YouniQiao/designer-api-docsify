# @ohos.arkui.Prefetcher

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BasicPrefetcher](arkts-arkui-arkui-prefetcher-basicprefetcher-c.md) | Basic implementation of [IPrefetcher](arkts-arkui-arkui-prefetcher-iprefetcher-i.md#IPrefetcher).It provides an intelligent data prefetching algorithm to make decisions about which data items should be prefetched in response to the real-time changes of visible on-screen area and changes in the duration of the prefetching. It also determines which prefetch requests should be canceled based on user scrolling actions. |

### Interfaces

| Name | Description |
| --- | --- |
| [IDataSourcePrefetching](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md) | Implement this interface to provide data prefetching for the LazyForEach component. |
| [IPrefetcher](arkts-arkui-arkui-prefetcher-iprefetcher-i.md) | Implement this interface to provide prefetcher logic. |

