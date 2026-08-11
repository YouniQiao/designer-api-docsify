# getUidForName

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getUidForName

```TypeScript
function getUidForName(v: string): number
```

Obtains the UID of a user from the user database of the system based on the specified user name.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getUidForName](arkts-arkts-process-processmanager-c.md#getuidforname)

<!--Device-process-function getUidForName(v: string): number--><!--Device-process-function getUidForName(v: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pres = process.getUidForName("tool");
```
