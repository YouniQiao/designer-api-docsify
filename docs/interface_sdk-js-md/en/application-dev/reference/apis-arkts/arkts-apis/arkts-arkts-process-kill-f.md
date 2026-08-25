# kill

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## kill

```TypeScript
function kill(signal: number, pid: number): boolean
```

Sends a signal to a specified process to terminate it.

**Since:** 7

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
