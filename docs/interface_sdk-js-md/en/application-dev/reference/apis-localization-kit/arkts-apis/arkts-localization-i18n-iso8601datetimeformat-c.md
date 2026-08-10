# ISO8601DateTimeFormat

符合ISO 8601标准的日期格式化对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-i18n-export class ISO8601DateTimeFormat--><!--Device-i18n-export class ISO8601DateTimeFormat-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## constructor

```TypeScript
public constructor(options?: ISO8601DateTimeFormatOptions)
```

创建符合ISO 8601标准的日期格式化对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ISO8601DateTimeFormat-public constructor(options?: ISO8601DateTimeFormatOptions)--><!--Device-ISO8601DateTimeFormat-public constructor(options?: ISO8601DateTimeFormatOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ISO8601DateTimeFormatOptions](arkts-localization-i18n-iso8601datetimeformatoptions-i.md) | No | 符合ISO 8601标准的日期格式化对象创建时的配置项。 默认值：所有属性都取默认值时的配置项。 |

## format

```TypeScript
public format(date: Date): string
```

对时间日期进行格式化，返回符合ISO 8601标准的时间日期字符串。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ISO8601DateTimeFormat-public format(date: Date): string--><!--Device-ISO8601DateTimeFormat-public format(date: Date): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 符合ISO8601标准的时间日期字符串。 |

