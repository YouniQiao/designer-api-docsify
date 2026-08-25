# StyledDateTimeFormat

Provide a DateTime formatting interface which could format DateTime to StyleString.

**Since:** 23

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,
        options?: StyledDateTimeFormatOptions)
```

Creates an object for formatting the time and date that need to be displayed in rich text.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dateTimeFormat](../../apis-media-kit/arkts-apis/arkts-media-media-avmetadata-i.md) | Intl.DateTimeFormat \| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) | Yes |
| options | [StyledDateTimeFormatOptions](arkts-localization-i18n-styleddatetimeformatoptions-i.md) | No |

## format

```TypeScript
format(date: Date): StyledString
```

Formats the date and time as a rich text object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| date | Date | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) |
