# Callback

Defines a common callback used to return the processing result when an asynchronous operation is successful. You need to define the callback type.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

<!--Device-unnamed-export interface Callback--><!--Device-unnamed-export interface Callback-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from '@kit.BasicServicesKit';
```

## constructor

```TypeScript
(data: T): void
```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Callback-(data: T): void--><!--Device-Callback-(data: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | Common callback information. The type is defined by the developer. The callback is used to return data of the corresponding type. No data is returned if the callback fails. |

