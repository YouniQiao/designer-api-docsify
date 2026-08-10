# getErrorString

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## getErrorString

```TypeScript
function getErrorString(errno: number): string
```

获取系统错误码的详细信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [util.errnoToString](arkts-arkts-util-errnotostring-f.md#errnotostring)

<!--Device-util-function getErrorString(errno: number): string--><!--Device-util-function getErrorString(errno: number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errno | number | Yes | 生成的错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 错误码的详细信息。 |

## Examples

```TypeScript
let errnum = -1; // -1 is a system error code.
let result = util.getErrorString(errnum);
console.info("result = " + result);
// Output: result = operation not permitted
```

