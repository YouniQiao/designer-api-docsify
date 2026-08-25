# printf

## Modules to Import

```TypeScript
import { util } from '@kit.ArkTS';
```

## printf

```TypeScript
function printf(format: string, ...args: Object[]): string
```

Formats a string by replacing the placeholders in it.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [format](arkts-arkts-util-format-f.md)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| format | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let res = util.printf("%s", "hello world!");
console.info(res);
// Output: hello world!
```
