# ISO8601DateTimeFormat

符合ISO 8601标准的日期格式化对象。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(options?: ISO8601DateTimeFormatOptions)
```

创建符合ISO 8601标准的日期格式化对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ISO8601DateTimeFormatOptions](arkts-localization-i18n-iso8601datetimeformatoptions-i.md) | 否 |

## format

```TypeScript
public format(date: Date): string
```

对时间日期进行格式化，返回符合ISO 8601标准的时间日期字符串。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| string |
