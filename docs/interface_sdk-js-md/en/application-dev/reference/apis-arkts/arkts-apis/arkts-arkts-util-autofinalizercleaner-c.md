# AutoFinalizerCleaner

用于通过开发者自定义回调释放由开发者管理的资源的 cleaner。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-util-class AutoFinalizerCleaner<T>--><!--Device-util-class AutoFinalizerCleaner<T>-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## register

```TypeScript
static register<T>(obj: AutoFinalizer<T>, heldValue: T): void
```

注册释放由开发者管理的资源的对象。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AutoFinalizerCleaner-static register<T>(obj: AutoFinalizer<T>, heldValue: T): void--><!--Device-AutoFinalizerCleaner-static register<T>(obj: AutoFinalizer<T>, heldValue: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | [AutoFinalizer](arkts-arkts-util-autofinalizer-i.md)&lt;T&gt; | Yes | 注册到 cleaner 的对象。 |
| heldValue | T | Yes | 传递给 finalizer 的值。 |

