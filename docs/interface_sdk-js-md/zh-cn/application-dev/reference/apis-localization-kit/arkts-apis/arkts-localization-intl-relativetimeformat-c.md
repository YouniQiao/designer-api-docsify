# RelativeTimeFormat

提供相对时间格式化的能力。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建相对时间格式化对象。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)
```

创建相对时间格式化对象。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) | 否 |

## format

```TypeScript
format(value: number, unit: string): string
```

对相对时间进行格式化，返回相对时间字符串。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| unit | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatToParts

```TypeScript
formatToParts(value: number, unit: string): Array<object>
```

对相对时间进行格式化，获取格式化结果中各个部分的对象数组。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| unit | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;object & gt; |

## resolvedOptions

```TypeScript
resolvedOptions(): RelativeTimeFormatResolvedOptions
```

获取相对时间格式化对象的格式化配置项。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) |
