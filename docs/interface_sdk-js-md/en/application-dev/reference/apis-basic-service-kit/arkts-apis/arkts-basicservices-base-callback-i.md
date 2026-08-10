# Callback

通用回调函数，用于在异步操作完成时回传处理结果。类型由开发者自定义。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface Callback<T>--><!--Device-unnamed-export interface Callback<T>-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from 'kits/@kit.BasicServicesKit';
```

## [[Call]]

```TypeScript
(data: T): void
```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Callback-(data: T): void--><!--Device-Callback-(data: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | 接口调用时的公共回调信息。类型由开发者自定义，回调成功时将返回对应类型的数据。失败则不返回数据。 |

