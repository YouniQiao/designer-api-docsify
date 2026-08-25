# DateTimeFormat

提供日期格式化的能力。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建时间日期格式化对象。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: DateTimeOptions)
```

创建时间日期格式化对象。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) | 否 |

## format

```TypeScript
format(date: Date): string
```

对时间日期进行格式化，返回格式化后的时间日期字符串。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRange

```TypeScript
formatRange(startDate: Date, endDate: Date): string
```

对时间日期段进行格式化，返回格式化后的时间日期段字符串。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startDate | Date | 是 |
| endDate | Date | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## resolvedOptions

```TypeScript
resolvedOptions(): DateTimeOptions
```

获取创建时间日期格式化对象时设置的配置项。

**起始版本：** 6

**废弃版本：** 20

**替代接口：** [Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) |
