# StyledDateTimeFormat

提供富文本时间日期格式化的能力。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class StyledDateTimeFormat--><!--Device-i18n-export class StyledDateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,
        options?: StyledDateTimeFormatOptions)
```

创建需要富文本显示的时间日期格式化的对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledDateTimeFormat-constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,        options?: StyledDateTimeFormatOptions)--><!--Device-StyledDateTimeFormat-constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat,        options?: StyledDateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dateTimeFormat | Intl.DateTimeFormat \| SimpleDateTimeFormat | Yes | 用于格式化时间日期的对象。 |
| options | [StyledDateTimeFormatOptions](arkts-localization-i18n-styleddatetimeformatoptions-i.md) | No | 指定时间日期格式化对象的配置项。默认值：默认的文本样式。 |

## format

```TypeScript
format(date: Date): StyledString
```

对时间日期进行格式化，返回富文本对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-StyledDateTimeFormat-format(date: Date): StyledString--><!--Device-StyledDateTimeFormat-format(date: Date): StyledString-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledString](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-c.md) | 格式化后的富文本对象。 |

