# NumberFormat

Provides the API for formatting number strings.

**Since:** 6

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a **NumberFormat** object for the current system locale.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: NumberOptions)
```

Creates a **NumberFormat** object based on the specified locale and options.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | Yes |
| options | [NumberOptions](arkts-localization-intl-numberoptions-i.md) | No |

## format

```TypeScript
format(num: number): string
```

Formats a number.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| num | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatRange

```TypeScript
formatRange(startRange: number, endRange: number): string
```

Formats a number range.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startRange | number | Yes |
| endRange | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## resolvedOptions

```TypeScript
resolvedOptions(): NumberOptions
```

Obtains the options for creating a **NumberFormat** object.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Global.I18n

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NumberOptions](arkts-localization-intl-numberoptions-i.md) |
