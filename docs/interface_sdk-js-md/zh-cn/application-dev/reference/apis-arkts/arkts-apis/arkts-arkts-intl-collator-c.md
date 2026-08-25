# Collator

用于按区域设置比较字符串的Collator类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## compare

```TypeScript
public compare(x: string, y: string): double
```

比较两个字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | string | 是 |
| y | string | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: CollatorOptions)
```

创建新的Collator。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locales | string \| string[] | 否 |
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | 否 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedCollatorOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ResolvedCollatorOptions](arkts-arkts-intl-resolvedcollatoroptions-i.md) |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]
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
| options | [CollatorOptions](arkts-arkts-intl-collatoroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |
