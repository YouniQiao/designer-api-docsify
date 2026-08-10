# @ohos.arkui.Prefetcher

## Modules to Import

```TypeScript
import { IDataSourcePrefetching, BasicPrefetcher, IPrefetcher } from 'kits/@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BasicPrefetcher](arkts-arkui-arkui-prefetcher-basicprefetcher-c.md) | 一种IPrefetcher的基础实现。此prefetcher提供了一种智能预加载算法，可以根据显示区域的实时变化以及预加载耗时的变化来确定预加载范围并加载数据项，并且可以根据用户的滚动操作来取消相应数据项的预加载请求。 |

### Interfaces

| Name | Description |
| --- | --- |
| [IDataSourcePrefetching](arkts-arkui-arkui-prefetcher-idatasourceprefetching-i.md) | 用于实现具有预加载能力的LazyForEach数据源。 |
| [IPrefetcher](arkts-arkui-arkui-prefetcher-iprefetcher-i.md) | 该接口用于提供预加载操作。 |

