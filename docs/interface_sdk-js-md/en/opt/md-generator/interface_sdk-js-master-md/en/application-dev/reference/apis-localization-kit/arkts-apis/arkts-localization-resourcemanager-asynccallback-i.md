# AsyncCallback

Asynchronous callback interface.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback)

<!--Device-resourceManager-export interface AsyncCallback--><!--Device-resourceManager-export interface AsyncCallback-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
(err: Error, data: T): void
```

Defines an asynchronous callback that carries an error parameter and asynchronous return value.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | Error | Yes |
| data | T | Yes |
