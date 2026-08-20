# intlBestFitLocales

## Modules to Import

```TypeScript
```

## intlBestFitLocales

```TypeScript
export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]
```

Gets the best fit locales from the given language tags.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Intl-export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]--><!--Device-Intl-export function intlBestFitLocales(locale: Intl.BCP47LanguageTag | Intl.BCP47LanguageTag[]): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [Intl.BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | Yes | the locales. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | the best fit locales. |

