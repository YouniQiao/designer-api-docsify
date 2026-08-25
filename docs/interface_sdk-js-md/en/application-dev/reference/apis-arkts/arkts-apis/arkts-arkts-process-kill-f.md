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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [kill](arkts-arkts-process-processmanager-c.md#kill)

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

**Examples**

```TypeScript
let pres = process.pid;
let result = process.kill(28, pres);
```

```TypeScript
let pro = new process.ProcessManager();
let pres = process.pid;
let result = pro.kill(28, pres);
```
