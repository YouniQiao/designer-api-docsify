# isSendable

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## isSendable

```TypeScript
function isSendable(value: Object | null | undefined): boolean
```

检查ArkTS值是否为Sendable。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-utils-function isSendable(value: Object | null | undefined): boolean--><!--Device-utils-function isSendable(value: Object | null | undefined): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object \| null \| undefined | Yes | 要检查的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果值为Sendable则返回true，否则返回false。 |

