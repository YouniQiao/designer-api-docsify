# printf

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## printf

```TypeScript
function printf(format: string, ...args: Object[]): string
```

通过式样化字符串对输入的内容按特定格式输出。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [util.format](arkts-arkts-util-format-f.md#format)

<!--Device-util-function printf(format: string, ...args: Object[]): string--><!--Device-util-function printf(format: string, ...args: Object[]): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | 式样化字符串。 |
| args | Object[] | Yes | 替换式样化字符串通配符的数据，此参数缺失时，默认返回第一个参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 按特定格式式样化后的字符串，包含根据格式说明符处理后的参数值。 |

## Examples

```TypeScript
let res = util.printf("%s", "hello world!");
console.info(res);
// Output: hello world!
```

