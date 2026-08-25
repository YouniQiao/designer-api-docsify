# NumberFormat

提供标准的数字格式化的能力。

**起始版本：** 6

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

使用当前系统区域创建数字格式化对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: NumberOptions)
```

根据指定的区域和配置项创建数字格式化对象。

**起始版本：** 6

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [NumberOptions](arkts-localization-intl-numberoptions-i.md) | 否 |

## format

```TypeScript
format(num: number): string
```

对数字进行格式化，返回格式化后的数字字符串。

**起始版本：** 6

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| num | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## formatRange

```TypeScript
formatRange(startRange: number, endRange: number): string
```

对数字范围进行格式化，返回格式化后的数字范围字符串。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| startRange | number | 是 |
| endRange | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## resolvedOptions

```TypeScript
resolvedOptions(): NumberOptions
```

获取创建数字格式化对象时设置的配置项。

**起始版本：** 6

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [NumberOptions](arkts-localization-intl-numberoptions-i.md) |
