# AsyncCallback

Asynchronous callback interface.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

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

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | Error | Yes | Error message returned when the API fails to be called. |
| data | T | Yes | Callback invoked when the API is called. |

