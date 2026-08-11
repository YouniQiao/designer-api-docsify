# AsyncCallback

Asynchronous callback interface.

**Since:** 6

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

Defines an asynchronous callback that carries an error parameter and asynchronous return value.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.base:AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | Error | Yes |
| data | T | Yes |
