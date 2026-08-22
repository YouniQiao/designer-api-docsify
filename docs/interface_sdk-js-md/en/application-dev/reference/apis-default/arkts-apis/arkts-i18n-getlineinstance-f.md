# getLineInstance

## Modules to Import

```TypeScript
```

## getLineInstance

```TypeScript
export function getLineInstance(locale: string): BreakIterator
```

Obtains a BreakIterator object. The BreakIterator object maintains an internal break iterator that can be used to access various line break points.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getLineInstance(locale: string): BreakIterator--><!--Device-i18n-export function getLineInstance(locale: string): BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. The generated BreakIterator object calculates the positions of line breaks based on the rules of the specified locale. |

**Return value:**

| Type | Description |
| --- | --- |
| [BreakIterator](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-breakiterator-c.md) | BreakIterator object. |

