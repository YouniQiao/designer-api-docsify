# StyledDateTimeFormat

提供富文本时间日期格式化的能力。

**起始版本：** 23

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,
        options?: StyledDateTimeFormatOptions)
```

创建需要富文本显示的时间日期格式化的对象。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dateTimeFormat](../../apis-media-kit/arkts-apis/arkts-media-media-avmetadata-i.md) | Intl.DateTimeFormat \| [SimpleDateTimeFormat](arkts-localization-i18n-simpledatetimeformat-c.md) | 是 |
| options | [StyledDateTimeFormatOptions](arkts-localization-i18n-styleddatetimeformatoptions-i.md) | 否 |

## format

```TypeScript
format(date: Date): StyledString
```

对时间日期进行格式化，返回富文本对象。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) |
