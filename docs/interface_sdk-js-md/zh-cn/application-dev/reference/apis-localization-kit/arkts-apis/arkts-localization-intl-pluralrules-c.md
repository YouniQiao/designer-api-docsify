# PluralRules

提供获取单复数类型的能力。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { intl } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

创建单复数对象来计算数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: PluralRulesOptions)
```

创建单复数对象来计算数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string \| Array & lt;string & gt; | 是 |
| options | [PluralRulesOptions](arkts-localization-intl-pluralrulesoptions-i.md) | 否 |

## select

```TypeScript
select(n: number): string
```

获取数字的单复数类别。

**起始版本：** 8

**废弃版本：** 20

**替代接口：** [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| n | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |
