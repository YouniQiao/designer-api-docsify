# Segmenter

Segmenter class for locale-sensitive text segmentation.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)
```

Creates a new Segmenter.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | BCP47LanguageTag \| [BCP47LanguageTag[]](arkts-arkts-intl-bcp47languagetag-t.md) | No |
| options | [SegmenterOptions](arkts-arkts-intl-segmenteroptions-i.md) | No |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSegmenterOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedSegmenterOptions](arkts-arkts-intl-resolvedsegmenteroptions-i.md) |

## segment

```TypeScript
public segment(doc: string): Segments
```

Segments a document.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| doc | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Segments](arkts-arkts-intl-segments-c.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], 
            options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | BCP47LanguageTag \| [BCP47LanguageTag[]](arkts-arkts-intl-bcp47languagetag-t.md) | Yes |
| options | [PickLocaleMatchSegmenterOptions](arkts-arkts-intl-picklocalematchsegmenteroptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [BCP47LanguageTag[]](arkts-arkts-intl-bcp47languagetag-t.md) |
