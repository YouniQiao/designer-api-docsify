# StyledDateTimeFormat

Provide a DateTime formatting interface which could format DateTime to StyleString.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-i18n-export class StyledDateTimeFormat--><!--Device-i18n-export class StyledDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,
        options?: StyledDateTimeFormatOptions)
```

A constructor used to create a StyledDateTimeFormat object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledDateTimeFormat-constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,        options?: StyledDateTimeFormatOptions)--><!--Device-StyledDateTimeFormat-constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,        options?: StyledDateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dateTimeFormat | Intl.DateTimeFormat \| [SimpleDateTimeFormat](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-simpledatetimeformat-c.md) | Yes | Indicates the date and time format object that used to format date. |
| options | [StyledDateTimeFormatOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-styleddatetimeformatoptions-i.md) | No | Indicates the options used to format the date. |

## format

```TypeScript
format(date: Date): StyledString
```

Formats a date as a rich text object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledDateTimeFormat-format(date: Date): StyledString--><!--Device-StyledDateTimeFormat-format(date: Date): StyledString-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | date to be formatted. |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-styledstring-c.md) | Rich text object after formatting. |

