# AutoFinalizerCleaner

A cleaner for releasing resources managed by developers through a developer-defined callback.

**Since:** 22

**Deprecated since:** -1

<!--Device-util-class AutoFinalizerCleaner--><!--Device-util-class AutoFinalizerCleaner-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## register

```TypeScript
static register<T>(obj: AutoFinalizer<T>, heldValue: T): void
```

Register objects that release resources managed by developers.

**Since:** 22

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AutoFinalizerCleaner-static register<T>(obj: AutoFinalizer<T>, heldValue: T): void--><!--Device-AutoFinalizerCleaner-static register<T>(obj: AutoFinalizer<T>, heldValue: T): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [AutoFinalizer](arkts-arkts-util-autofinalizer-i.md)&lt;T&gt; | Yes |
| heldValue | T | Yes |
