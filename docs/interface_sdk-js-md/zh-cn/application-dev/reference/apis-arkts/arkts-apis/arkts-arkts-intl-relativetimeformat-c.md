# RelativeTimeFormat

用于按区域设置格式化相对时间的RelativeTimeFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)
```

创建新的RelativeTimeFormat。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 否 |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 |

## format

```TypeScript
public format(value: double, unit: RelativeTimeFormatUnit): string
```

格式化相对时间。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |
| unit | [RelativeTimeFormatUnit](arkts-arkts-intl-relativetimeformatunit-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatToParts

```TypeScript
public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

将相对时间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |
| unit | [RelativeTimeFormatUnit](arkts-arkts-intl-relativetimeformatunit-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RelativeTimeFormatPart](arkts-arkts-intl-relativetimeformatpart-i.md)[] |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedRelativeTimeFormatOptions](arkts-arkts-intl-resolvedrelativetimeformatoptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]
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
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
