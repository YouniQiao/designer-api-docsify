# Collator

提供字符串排序的能力。

**起始版本：** 8

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## compare

```TypeScript
compare(first: string, second: string): number
```

根据配置项的排序规则，比较两个字符串。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| first | string | 是 |
| second | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## constructor

```TypeScript
constructor()
```

使用当前系统区域创建排序对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: CollatorOptions)
```

根据指定的区域和配置项创建排序对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) | 否 |

## resolvedOptions

```TypeScript
resolvedOptions(): CollatorOptions
```

获取创建排序对象时设置的配置项。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) |
