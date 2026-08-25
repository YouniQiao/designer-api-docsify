# Segmenter

用于按区域设置进行文本分段的Segmenter类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 否 |
| options | [SegmenterOptions](arkts-arkts-intl-segmenteroptions-i.md) | 否 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedSegmenterOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedSegmenterOptions](arkts-arkts-intl-resolvedsegmenteroptions-i.md) |

## segment

```TypeScript
public segment(doc: string): Segments
```

对文档进行分段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| doc | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Segments](arkts-arkts-intl-segments-c.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: BCP47LanguageTag | BCP47LanguageTag[], 
            options?: PickLocaleMatchSegmenterOptions): BCP47LanguageTag[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md) \| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] | 是 |
| options | [PickLocaleMatchSegmenterOptions](arkts-arkts-intl-picklocalematchsegmenteroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [BCP47LanguageTag](arkts-arkts-intl-bcp47languagetag-t.md)[] |
