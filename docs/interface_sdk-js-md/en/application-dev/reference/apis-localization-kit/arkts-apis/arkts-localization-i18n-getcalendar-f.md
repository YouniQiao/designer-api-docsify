# getCalendar

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getCalendar

```TypeScript
export function getCalendar(locale: string, type?: string): Calendar
```

获取指定区域和历法的日历对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar--><!--Device-i18n-export function getCalendar(locale: string, type?: string): Calendar-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成，例 如zh-Hans-CN。 |
| type | string | No | 表示历法，取值包括：buddhist, chinese, coptic, ethiopic, hebrew, gregory, indian, islamic_civil,  islamic_tbla, islamic_umalqura, japanese, persian。 &lt;br&gt;默认值：区域默认的历法。不同取值代表的含义和使用场景请参考[设置日历和历法](../../../internationalization/i18n-calendar.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Calendar](arkts-localization-i18n-calendar-c.md) | 日历对象。 |

