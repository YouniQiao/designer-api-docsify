# IndexUtil

提供索引相关的能力，包括区域索引列表和文本索引值获取。

**起始版本：** 8

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## addLocale

```TypeScript
addLocale(locale: string): void
```

在当前区域的索引列表中，添加新区域的索引列表，形成复合列表。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 是 |

## getIndex

```TypeScript
getIndex(text: string): string
```

获取输入文本对应的索引值。

**起始版本：** 8

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

## getIndexList

```TypeScript
getIndexList(): Array<string>
```

获取当前区域的索引列表。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |
