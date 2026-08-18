# set24HourClock

## 导入模块

```TypeScript
```

## set24HourClock

```TypeScript
export function set24HourClock(option: boolean): boolean
```

修改系统时间的24小时制设置。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [set24HourClock](arkts-localization-i18n-system-c-sys.md#set24hourclock)

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function set24HourClock(option: boolean): boolean--><!--Device-i18n-export function set24HourClock(option: boolean): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// 将系统时间设置为24小时制
let success: boolean = i18n.set24HourClock(true);
```
