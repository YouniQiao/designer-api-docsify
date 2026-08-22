# Transliterator

Provides text transliteration capabilities, such as obtaining the supported language IDs and transliterating text.

**Since:** 23

<!--Device-i18n-export class Transliterator--><!--Device-i18n-export class Transliterator-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getAvailableIDs

```TypeScript
static getAvailableIDs(): string[]
```

Obtains a list of IDs supported by the **Transliterator** object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Transliterator-static getAvailableIDs(): string[]--><!--Device-Transliterator-static getAvailableIDs(): string[]-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string[] | List of IDs supported by the **Transliterator** object. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// ids = ['America/Adak', 'America/Anchorage', 'America/Bogota', 'America/Denver', 'America/Los_Angeles', 'America/Montevideo', 'America/Santiago', 'America/Sao_Paulo', 'Asia/Ashgabat', 'Asia/Hovd', 'Asia/Jerusalem', 'Asia/Magadan', 'Asia/Omsk', 'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Yerevan', 'Atlantic/Cape_Verde', 'Australia/Lord_Howe', 'Europe/Dublin', 'Europe/London', 'Europe/Moscow', 'Pacific/Auckland', 'Pacific/Easter', 'Pacific/Pago-Pago']
let ids: Array<string> = i18n.TimeZone.getAvailableIDs();
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// A total of 742 IDs are supported. One ID is comprised of two parts separated by a hyphen (-) in the format of source-destination. For example, in **ids = ["Han-Latin","Latin-ASCII", "Amharic-Latin/BGN","Accents-Any", ...]**, **Han-Latin** indicates conversion from Chinese to Latin, and **Amharic-Latin** indicates conversion from Amharic to Latin.
// For more information, see ISO-15924.
let ids: string[] = i18n.Transliterator.getAvailableIDs();
```

## getInstance

```TypeScript
static getInstance(id: string): Transliterator
```

Creates a **Transliterator** object based on the specified ID.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Transliterator-static getInstance(id: string): Transliterator--><!--Device-Transliterator-static getInstance(id: string): Transliterator-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID supported by the **Transliterator** object. |

**Return value:**

| Type | Description |
| --- | --- |
| [Transliterator](arkts-localization-i18n-transliterator-c.md) | Transliterator** object. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## transform

```TypeScript
transform(text: string): string
```

Converts the input text from the source format to the target format.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Transliterator-transform(text: string): string--><!--Device-Transliterator-transform(text: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Input text. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Text after conversion. |

**Examples**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
let wordArray: string[] = ['China', 'Germany', 'US', 'France"]
for (let i = 0; i < wordArray.length; i++) {
  let transliterateLatn: string =
    transliterator.transform(wordArray[i]); // transliterateLatn: 'zhōng guó', 'dé guó', 'měi guó', 'fǎ guó'
}

// Chinese transliteration and tone removal
transliterator = i18n.Transliterator.getInstance('Any-Latn;Latin-Ascii');
let transliterateAscii: string = transliterator.transform ('China'); // transliterateAscii = 'zhong guo'

// Chinese surname pronunciation
transliterator = i18n.Transliterator.getInstance('Han-Latin/Names');
let transliterateNames: string = transliterator.transform('Teacher Shan'); // transliterateNames = 'shàn lǎo shī'
transliterateNames = transliterator.transform('Long Sun No Taboo'); // transliterateNames = 'zhǎng sūn wú jì'
```

