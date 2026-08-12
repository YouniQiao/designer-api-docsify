# errnoToString

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## errnoToString

```TypeScript
function errnoToString(errno: number): string
```

Obtains detailed information about a system error code.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-util-function errnoToString(errno: number): string--><!--Device-util-function errnoToString(errno: number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errno](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let errnum = -1; // -1 is a system error code.
let result = util.errnoToString(errnum);
console.info("result = " + result);
// Output: result = operation not permitted
```
