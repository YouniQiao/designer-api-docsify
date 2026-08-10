# ErrorCallback

通用回调函数，携带错误参数，用于在接口调用失败时回传错误信息。具体错误码值由各接口定义，请参考对应接口的错误码说明。

回调返回的信息为[BusinessError](arkts-basicservices-base-businesserror-i.md)类型的错误参数。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface ErrorCallback<T extends Error = BusinessError>--><!--Device-unnamed-export interface ErrorCallback<T extends Error = BusinessError>-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from 'kits/@kit.BasicServicesKit';
```

## [[Call]]

```TypeScript
(err: T): void
```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ErrorCallback-(err: T): void--><!--Device-ErrorCallback-(err: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | T | Yes | 接口调用失败的公共错误信息，类型默认为[BusinessError](arkts-basicservices-base-businesserror-i.md)，包含错误码（code）和可选附加数据（data）。 |

