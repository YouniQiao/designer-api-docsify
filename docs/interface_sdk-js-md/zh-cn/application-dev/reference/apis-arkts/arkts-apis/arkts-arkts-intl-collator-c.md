# Collator

用于按区域设置比较字符串的Collator类。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-Intl-export class Collator--><!--Device-Intl-export class Collator-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public compare(x: string, y: string): double--><!--Device-Collator-public compare(x: string, y: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | string | 是 | 参与比较的第一个字符串。 |
| y | string | 是 | 参与比较的第二个字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | 比较结果。 |

## constructor

```TypeScript
public constructor(locales?: string | string[], options?: CollatorOptions)
```

创建新的Collator。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)--><!--Device-Collator-public constructor(locales?: string | string[], options?: CollatorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | 区域设置。 |
| options | CollatorOptions | 否 | 选项。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedCollatorOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions--><!--Device-Collator-public resolvedOptions(): ResolvedCollatorOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedCollatorOptions](arkts-arkts-intl-resolvedcollatoroptions-i.md) | 解析后的选项。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]--><!--Device-Collator-public static supportedLocalesOf(locales: string | string[], options?: CollatorOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | 区域设置。 |
| options | CollatorOptions | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

