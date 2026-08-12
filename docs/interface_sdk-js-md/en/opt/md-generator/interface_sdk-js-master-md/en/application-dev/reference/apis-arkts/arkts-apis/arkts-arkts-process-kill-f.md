# kill

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## kill

```TypeScript
function kill(signal: number, pid: number): boolean
```

Sends a signal to a specified process to terminate it.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [kill](arkts-arkts-process-processmanager-c.md#kill)

<!--Device-process-function kill(signal: number, pid: number): boolean--><!--Device-process-function kill(signal: number, pid: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [signal](arkts-arkts-locks-asynclockoptions-c.md) | number | Yes |
| pid | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let pres = process.pid;
let result = process.kill(28, pres);
```
