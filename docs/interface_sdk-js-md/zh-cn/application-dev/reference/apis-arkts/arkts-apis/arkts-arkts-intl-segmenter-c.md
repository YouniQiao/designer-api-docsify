# Segmenter

Segmenter class for locale-sensitive text segmentation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class Segmenter--><!--Device-Intl-export class Segmenter-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)
```

Creates a new Segmenter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)--><!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| BCP47LanguageTag[] | 否 | the locales. |
| options | [SegmenterOptions](arkts-arkts-intl-segmenteroptions-i.md) | 否 | the options. |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSegmenterOptions
```

Returns resolved options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions--><!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedSegmenterOptions](arkts-arkts-intl-resolvedsegmenteroptions-i.md) | the resolved options. |

## segment

```TypeScript
public segment(doc: string): Segments
```

Segments a document.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public segment(doc: string): Segments--><!--Device-Segmenter-public segment(doc: string): Segments-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doc | string | 是 | the text to segment. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Segments](arkts-arkts-intl-segments-c.md) | the segments. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], 
            options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]--><!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| BCP47LanguageTag[] | 是 | the locales. |
| options | [PickLocaleMatchSegmenterOptions](arkts-arkts-intl-picklocalematchsegmenteroptions-i.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | supported locales. |

