# Segmenter

用于按区域设置进行文本分段的Segmenter类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-Intl-export class Segmenter--><!--Device-Intl-export class Segmenter-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)
```

创建新的Segmenter。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)--><!--Device-Segmenter-public constructor(locales?: BCP47LanguageTag | BCP47LanguageTag[], options?: SegmenterOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 | 区域设置。 |
| options | [SegmenterOptions](arkts-arkts-intl-segmenteroptions-i.md) | 否 | 选项。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSegmenterOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions--><!--Device-Segmenter-public resolvedOptions(): ResolvedSegmenterOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedSegmenterOptions](arkts-arkts-intl-resolvedsegmenteroptions-i.md) | 解析后的选项。 |

## segment

```TypeScript
public segment(doc: string): Segments
```

对文档进行分段。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public segment(doc: string): Segments--><!--Device-Segmenter-public segment(doc: string): Segments-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| doc | string | 是 | 待分段的文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Segments](arkts-arkts-intl-segments-c.md) | 分段结果。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], 
            options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]--><!--Device-Segmenter-public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[],             options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 是 | 区域设置。 |
| options | [PickLocaleMatchSegmenterOptions](arkts-arkts-intl-picklocalematchsegmenteroptions-i.md) | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 支持的区域设置。 |

