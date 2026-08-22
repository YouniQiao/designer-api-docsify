# SimpleDateTimeFormat

Provide a simple date time formatting interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-i18n-export class SimpleDateTimeFormat--><!--Device-i18n-export class SimpleDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## format

```TypeScript
format(date: Date): string
```

Formats the date and time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-SimpleDateTimeFormat-format(date: Date): string--><!--Device-SimpleDateTimeFormat-format(date: Date): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from 0. For example, 0 indicates January. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string containing the formatted date and time. |

