# set24HourClock

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## set24HourClock

```TypeScript
export function set24HourClock(option: boolean): boolean
```

修改系统时间的24小时制设置。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [i18n.System.set24HourClock](arkts-localization-i18n-system-c-sys.md#set24hourclock)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function set24HourClock(option: boolean): boolean--><!--Device-i18n-export function set24HourClock(option: boolean): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | boolean | Yes | true表示开启系统24小时制开关，false表示关闭系统24小时制开关。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示修改成功，false表示修改失败。 |

