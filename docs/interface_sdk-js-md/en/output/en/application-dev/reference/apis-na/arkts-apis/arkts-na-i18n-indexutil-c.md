# IndexUtil

Sequence text can be grouped under the specified area, and grouping index with different lengths can be specified.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class IndexUtil--><!--Device-i18n-export class IndexUtil-End-->

**System capability:** SystemCapability.Global.I18n

## addLocale

```TypeScript
addLocale(locale: string): void
```

Adds the index list of a new locale to the index list of the current locale to form a composite list.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-addLocale(locale: string): void--><!--Device-IndexUtil-addLocale(locale: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |

## getIndex

```TypeScript
getIndex(text: string): string
```

Obtains the index of the text object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-getIndex(text: string): string--><!--Device-IndexUtil-getIndex(text: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text object. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Index of the text object. If no proper index is found, an empty string is returned. |

## getIndexList

```TypeScript
getIndexList(): Array<string>
```

Obtains the index list of the current locale.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-getIndexList(): Array<string>--><!--Device-IndexUtil-getIndexList(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Index list of the current locale. The first and last elements are "...". |

