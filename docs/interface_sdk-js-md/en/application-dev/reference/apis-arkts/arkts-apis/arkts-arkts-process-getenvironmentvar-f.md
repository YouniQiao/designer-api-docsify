# getEnvironmentVar

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## getEnvironmentVar

```TypeScript
function getEnvironmentVar(name: string): string
```

Obtains the value of an environment variable.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getEnvironmentVar](arkts-arkts-process-processmanager-c.md#getenvironmentvar)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let pres = process.getEnvironmentVar("PATH");
```

```TypeScript
let pro = new process.ProcessManager();
let pres = pro.getEnvironmentVar("PATH");
```
