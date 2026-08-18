# is24HourClock

## 导入模块

```TypeScript
```

## is24HourClock

```TypeScript
export function is24HourClock(): boolean
```

判断系统时间是否为24小时制。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [is24HourClock](arkts-localization-i18n-system-c.md#is24hourclock)

<!--Device-i18n-export function is24HourClock(): boolean--><!--Device-i18n-export function is24HourClock(): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.is24HourClock();
```
