# DateTimeFormat

Provides the API for formatting date strings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export class DateTimeFormat--><!--Device-intl-export class DateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a DateTimeOptions object for the specified locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeFormat-constructor()--><!--Device-DateTimeFormat-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: DateTimeOptions)
```

Creates a DateTimeOptions object for the specified locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeFormat-constructor(locale: string | Array<string>, options?: DateTimeOptions)--><!--Device-DateTimeFormat-constructor(locale: string | Array<string>, options?: DateTimeOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) | No | Options for creating the DateTimeOptions object.&lt;br&gt;If no options are set, the default values of year, month, and day are numeric. |

## format

```TypeScript
format(date: Date): string
```

Formats the date and time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeFormat-format(date: Date): string--><!--Device-DateTimeFormat-format(date: Date): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from 0. For example, 0 indicates January. |

**Return value:**

| Type | Description |
| --- | --- |
| string | A string containing the formatted date and time. |

## formatRange

```TypeScript
formatRange(startDate: Date, endDate: Date): string
```

Formats date and time ranges.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeFormat-formatRange(startDate: Date, endDate: Date): string--><!--Device-DateTimeFormat-formatRange(startDate: Date, endDate: Date): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| startDate | Date | Yes | Start date and time. Note: The month starts from 0. For example, 0 indicates January. |
| endDate | Date | Yes | End date and time. Note: The month starts from 0. For example, 0 indicates January. |

**Return value:**

| Type | Description |
| --- | --- |
| string | a date string formatted based on the specified locale. |

## resolvedOptions

```TypeScript
resolvedOptions(): DateTimeOptions
```

Obtains the options for creating a DateTimeOptions object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DateTimeFormat-resolvedOptions(): DateTimeOptions--><!--Device-DateTimeFormat-resolvedOptions(): DateTimeOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) | Options for the DateTimeOptions object. |

