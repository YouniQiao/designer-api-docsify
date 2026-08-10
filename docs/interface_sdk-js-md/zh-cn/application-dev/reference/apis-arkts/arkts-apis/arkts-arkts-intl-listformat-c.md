# ListFormat

ListFormat class for locale-sensitive list formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class ListFormat--><!--Device-Intl-export class ListFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: ListFormatOptions)
```

Creates a new ListFormat.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)--><!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | the locales. |
| options | [ListFormatOptions](arkts-arkts-intl-listformatoptions-i.md) | 否 | the options. |

## format

```TypeScript
public format(list: Iterable<string>): string
```

Formats a list.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public format(list: Iterable<string>): string--><!--Device-ListFormat-public format(list: Iterable<string>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 | the list to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | formatted string. |

## formatToParts

```TypeScript
public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>
```

Formats a list to parts.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>--><!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 | the list to format. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;FormatToPartsResult&gt; | formatted parts. |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]
```

Returns supported locales.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]--><!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | the locales. |
| options | [ListFormatLocaleMatcher](arkts-arkts-intl-listformatlocalematcher-t.md) | 否 | the options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | supported locales. |

