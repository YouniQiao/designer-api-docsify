# AsyncCallback

异步回调接口

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.base:AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md)

<!--Device-resourceManager-export interface AsyncCallback<T>--><!--Device-resourceManager-export interface AsyncCallback<T>-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## [[Call]]

```TypeScript
(err: Error, data: T): void
```

异步回调函数，携带错误参数和异步返回值。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.base:AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | Error | Yes | 接口调用失败的错误信息。 |
| data | T | Yes | 接口调用时的回调信息。 |

