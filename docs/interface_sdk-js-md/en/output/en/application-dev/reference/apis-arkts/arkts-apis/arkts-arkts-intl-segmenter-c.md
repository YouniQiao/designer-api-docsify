# Segmenter

Segmenter class for locale-sensitive text segmentation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-Intl-export class Segmenter--><!--Device-Intl-export class Segmenter-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)
```

Creates a new Segmenter.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)--><!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| BCP47LanguageTag[] | No | the locales. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSegmenterOptions
```

Returns resolved options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions--><!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the resolved options. |

## segment

```TypeScript
public segment(doc: string): Segments
```

Segments a document.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segmenter-public segment(doc: string): Segments--><!--Device-Segmenter-public segment(doc: string): Segments-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| doc | string | Yes | the text to segment. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the segments. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], 
            options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]
```

Returns supported locales.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]--><!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| BCP47LanguageTag[] | Yes | the locales. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the options. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_[] | supported locales. |

