# Transliterator

提供文本音译相关的能力，包括音译支持范围获取和文本音译等。

**起始版本：** 9

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getAvailableIDs

```TypeScript
static getAvailableIDs(): string[]
```

获取音译支持的转换ID列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string[] |

## getInstance

```TypeScript
static getInstance(id: string): Transliterator
```

创建指定转换ID的音译对象。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Transliterator](arkts-localization-i18n-transliterator-c.md) |

## transform

```TypeScript
transform(text: string): string
```

将输入文本从源格式转换为目标格式。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |
