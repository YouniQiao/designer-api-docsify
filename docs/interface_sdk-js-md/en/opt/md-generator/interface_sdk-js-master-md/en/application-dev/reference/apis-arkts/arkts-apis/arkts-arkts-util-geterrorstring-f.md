# getErrorString

## Modules to Import

```TypeScript
```

## getErrorString

```TypeScript
function getErrorString(errno: number): string
```

Obtains detailed information about a system error code.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [errnoToString](arkts-arkts-util-errnotostring-f.md#errnotostring)

<!--Device-util-function getErrorString(errno: number): string--><!--Device-util-function getErrorString(errno: number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errno](../../apis-universal-keystore-kit/arkts-apis/arkts-universalkeystore-huksexternalcrypto-huksexternalerrorinfo-i.md) | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let errnum = -1; // -1 is a system error code.
let result = util.getErrorString(errnum);
console.info("result = " + result);
// Output: result = operation not permitted
```
