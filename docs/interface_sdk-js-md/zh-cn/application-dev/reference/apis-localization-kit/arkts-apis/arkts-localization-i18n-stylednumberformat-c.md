# StyledNumberFormat

提供富文本数字格式化的能力。

**起始版本：** 18

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

创建需要富文本显示的数字格式化的对象。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numberFormat | Intl.NumberFormat \| [SimpleNumberFormat](arkts-localization-i18n-simplenumberformat-c.md) | 是 |
| options | [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) | 否 |

## constructor

```TypeScript
constructor(numberFormat: intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
```

创建需要富文本显示的数字格式化的对象。

**起始版本：** 18

**废弃版本：** 20

**替代接口：** [constructor](#constructor)(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| numberFormat | intl.NumberFormat \| [SimpleNumberFormat](arkts-localization-i18n-simplenumberformat-c.md) | 是 |
| options | [StyledNumberFormatOptions](arkts-localization-i18n-stylednumberformatoptions-i.md) | 否 |

## format

```TypeScript
format(value: number): StyledString
```

使用数字格式化对象对数字进行格式化，返回富文本对象。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) |
