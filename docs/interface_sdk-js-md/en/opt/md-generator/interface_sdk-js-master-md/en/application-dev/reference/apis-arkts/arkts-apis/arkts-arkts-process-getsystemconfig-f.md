# getSystemConfig

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## getSystemConfig

```TypeScript
function getSystemConfig(name: number): number
```

Obtains the system configuration.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSystemConfig](arkts-arkts-process-processmanager-c.md#getSystemConfig)

<!--Device-process-function getSystemConfig(name: number): number--><!--Device-process-function getSystemConfig(name: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```
