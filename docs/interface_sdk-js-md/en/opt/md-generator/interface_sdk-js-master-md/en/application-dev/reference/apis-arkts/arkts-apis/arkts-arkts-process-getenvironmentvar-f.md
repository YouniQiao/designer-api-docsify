# getEnvironmentVar

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## getEnvironmentVar

```TypeScript
function getEnvironmentVar(name: string): string
```

Obtains the value of an environment variable.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getEnvironmentVar](arkts-arkts-process-processmanager-c.md#getenvironmentvar)

<!--Device-process-function getEnvironmentVar(name: string): string--><!--Device-process-function getEnvironmentVar(name: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let pres = process.getEnvironmentVar("PATH");
```
