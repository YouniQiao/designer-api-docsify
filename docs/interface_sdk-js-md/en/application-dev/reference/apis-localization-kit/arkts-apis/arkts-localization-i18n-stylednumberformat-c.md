# StyledNumberFormat

Provide a number formatting interface which could format number to StyleString.

**Since:** 18

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

Creates a **NumberFormat** object for rich text display.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| numberFormat | Intl.NumberFormat \| [SimpleNumberFormat](arkts-localization-i18n-simplenumberformat-c.md) | Yes |
| options | [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) | No |

## constructor

```TypeScript
constructor(numberFormat: intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

Creates a **NumberFormat** object for rich text display.

**Since:** 18

**Deprecated since:** 20

**Substitutes:** [constructor](#constructor)(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| numberFormat | intl.NumberFormat \| [SimpleNumberFormat](arkts-localization-i18n-simplenumberformat-c.md) | Yes |
| options | [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) | No |

## format

```TypeScript
format(value: number): StyledString
```

Formats a number as a rich text object.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) |
