# ListFormat

用于按区域设置格式化列表的ListFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class ListFormat--><!--Device-Intl-export class ListFormat-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: ListFormatOptions)
```

创建新的ListFormat。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)--><!--Device-ListFormat-public constructor(locales?: string | string[], options?: ListFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | 区域设置。 |
| options | [ListFormatOptions](arkts-arkts-intl-listformatoptions-i.md) | 否 | 选项。 |

## format

```TypeScript
public format(list: Iterable<string>): string
```

格式化列表。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public format(list: Iterable<string>): string--><!--Device-ListFormat-public format(list: Iterable<string>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 | 待格式化的列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

## formatToParts

```TypeScript
public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>
```

将列表格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>--><!--Device-ListFormat-public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 | 待格式化的列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[FormatToPartsResult](arkts-arkts-intl-formattopartsresult-i.md)&gt; | 格式化后的各个片段。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]--><!--Device-ListFormat-public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | 区域设置。 |
| options | [ListFormatLocaleMatcher](arkts-arkts-intl-listformatlocalematcher-t.md) | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

