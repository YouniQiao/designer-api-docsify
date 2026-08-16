# printf

## Modules to Import

```TypeScript
import { util } from 'util';
```

## printf

```TypeScript
function printf(format: string, ...args: Object[]): string
```

Formats a string by replacing the placeholders in it.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [format](../../apis-na/arkts-apis/arkts-na-util-format-f.md#format)

<!--Device-util-function printf(format: string, ...args: Object[]): string--><!--Device-util-function printf(format: string, ...args: Object[]): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | Format string. |
| args | Object[] | Yes | Data used to replace the placeholders in **format**. If **null** is passed in, the first argument is returned by default. |

**Return value:**

| Type | Description |
| --- | --- |
| string | String containing the formatted values. |

## Examples

```TypeScript
let res = util.printf("%s", "hello world!");
console.info(res);
// Output: hello world!
```

