# Transliterator

Provides the API for transliterate text from one format to another.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-i18n-export class Transliterator--><!--Device-i18n-export class Transliterator-End-->

**System capability:** SystemCapability.Global.I18n

## getAvailableIDs

```TypeScript
static getAvailableIDs(): string[]
```

Obtains a list of IDs supported by the Transliterator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Transliterator-static getAvailableIDs(): string[]--><!--Device-Transliterator-static getAvailableIDs(): string[]-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string[] | List of IDs supported by the Transliterator object. |

## getInstance

```TypeScript
static getInstance(id: string): Transliterator
```

Creates a Transliterator object based on the specified ID.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Transliterator-static getInstance(id: string): Transliterator--><!--Device-Transliterator-static getInstance(id: string): Transliterator-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID supported by the Transliterator object. |

**Return value:**

| Type | Description |
| --- | --- |
| [Transliterator](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-transliterator-c.md) | Transliterator object. |

## transform

```TypeScript
transform(text: string): string
```

Converts the input text from the source format to the target format.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

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

