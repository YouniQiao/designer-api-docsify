# ListFormat

用于按区域设置格式化列表的ListFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 否 |
| options | [ListFormatOptions](arkts-arkts-intl-listformatoptions-i.md) | 否 |

## format

```TypeScript
public format(list: Iterable<string>): string
```

格式化列表。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| list | Iterable & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatToParts

```TypeScript
public formatToParts(list: Iterable<string>): Array<FormatToPartsResult>
```

将列表格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| list | Iterable & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[FormatToPartsResult](arkts-arkts-intl-formattopartsresult-i.md)&gt; |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: ListFormatLocaleMatcher): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 是 |
| options | [ListFormatLocaleMatcher](arkts-arkts-intl-listformatlocalematcher-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
