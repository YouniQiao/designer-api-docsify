# SimpleNumberFormat

Provide a simple number formatting interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class SimpleNumberFormat--><!--Device-i18n-export class SimpleNumberFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## format

```TypeScript
format(value: double): string
```

Formats a number.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SimpleNumberFormat-format(value: double): string--><!--Device-SimpleNumberFormat-format(value: double): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | Number to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Formatted number. |

