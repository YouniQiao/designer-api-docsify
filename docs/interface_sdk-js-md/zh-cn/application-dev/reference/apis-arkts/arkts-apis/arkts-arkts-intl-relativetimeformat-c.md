# RelativeTimeFormat

用于按区域设置格式化相对时间的RelativeTimeFormat类。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-Intl-export class RelativeTimeFormat--><!--Device-Intl-export class RelativeTimeFormat-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)--><!--Device-RelativeTimeFormat-constructor(locales?: string | string[], options?: RelativeTimeFormatOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 | 区域设置。 |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 | 选项。 |

## format

```TypeScript
public format(value: double, unit: RelativeTimeFormatUnit): string
```

格式化相对时间。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string--><!--Device-RelativeTimeFormat-public format(value: double, unit: RelativeTimeFormatUnit): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 值。 |
| unit | [RelativeTimeFormatUnit](arkts-arkts-intl-relativetimeformatunit-t.md) | 是 | 单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

## formatToParts

```TypeScript
public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

将相对时间格式化为多个片段。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]--><!--Device-RelativeTimeFormat-public formatToParts(value: double, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 值。 |
| unit | [RelativeTimeFormatUnit](arkts-arkts-intl-relativetimeformatunit-t.md) | 是 | 单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeTimeFormatPart](arkts-arkts-intl-relativetimeformatpart-i.md)[] | 格式化后的各个片段。 |

## resolvedOptions

```TypeScript
public resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

返回解析后的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions--><!--Device-RelativeTimeFormat-public resolvedOptions(): ResolvedRelativeTimeFormatOptions-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedRelativeTimeFormatOptions](arkts-arkts-intl-resolvedrelativetimeformatoptions-i.md) | 解析后的选项。 |

## supportedLocalesOf

```TypeScript
public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]
```

返回支持的区域设置。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]--><!--Device-RelativeTimeFormat-public static supportedLocalesOf(locales: string | string[], options?: RelativeTimeFormatOptions): string[]-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 是 | 区域设置。 |
| options | [RelativeTimeFormatOptions](arkts-arkts-intl-relativetimeformatoptions-i.md) | 否 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 支持的区域设置。 |

