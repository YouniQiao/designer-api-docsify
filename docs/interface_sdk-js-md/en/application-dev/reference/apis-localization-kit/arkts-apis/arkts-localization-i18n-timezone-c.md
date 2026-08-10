# TimeZone

提供时区相关的能力，包括时区名称翻译、偏移量获取和跳变规则获取等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class TimeZone--><!--Device-i18n-export class TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getAppDefaultTimeZone

```TypeScript
static getAppDefaultTimeZone(): TimeZone
```

获取应用使用的默认时区对象。若调用[setAppDefaultTimeZoneById](arkts-localization-i18n-timezone-c.md#setappdefaulttimezonebyid)设置了默认时区，则返回设置的默认时区对象；否则，返回系统时区对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone--><!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) | 应用使用的默认时区对象。 |

## getAvailableIDs

```TypeScript
static getAvailableIDs(): Array<string>
```

获取系统支持的时区ID列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getAvailableIDs(): Array<string>--><!--Device-TimeZone-static getAvailableIDs(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 系统支持的时区ID列表。 |

## getAvailableZoneCityIDs

```TypeScript
static getAvailableZoneCityIDs(): Array<string>
```

获取系统支持的时区城市ID列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>--><!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 系统支持的时区城市ID列表。 |

## getCityDisplayName

```TypeScript
static getCityDisplayName(cityID: string, locale: string): string
```

获取时区城市名称在指定语言下的翻译。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string--><!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cityID | string | Yes | 时区城市ID。 |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 时区城市名称在指定语言下的翻译。 |

## getDisplayName

```TypeScript
getDisplayName(locale?: string, isDST?: boolean): string
```

获取时区对象名称在指定语言下的翻译。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string--><!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区 组成。默认值：系统当前区域ID。 |
| isDST | boolean | No | true表示显示夏令时信息，false表示不显示夏令时信息。默认值：false。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 时区对象名称在指定语言下的翻译。 |

## getID

```TypeScript
getID(): string
```

获取时区对象的ID。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getID(): string--><!--Device-TimeZone-getID(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | 时区对象对应的时区ID。 |

## getOffset

```TypeScript
getOffset(date?: double): int
```

获取某一时刻时区对象所表示时区的偏移量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getOffset(date?: double): int--><!--Device-TimeZone-getOffset(date?: double): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | double | No | 待计算时区偏移量的时刻，单位为毫秒（ms）。默认值：系统时间。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 时区的偏移量，单位为毫秒（ms）。当处于夏令时时，时区偏移量为时区原始偏移量加夏令时偏移量。 |

## getRawOffset

```TypeScript
getRawOffset(): int
```

获取时区对象所表示时区的原始偏移量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getRawOffset(): int--><!--Device-TimeZone-getRawOffset(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 时区的原始偏移量，单位为毫秒（ms）。 |

## getTimezoneFromCity

```TypeScript
static getTimezoneFromCity(cityID: string): TimeZone
```

创建对应时区城市的时区对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone--><!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cityID | string | Yes | 时区城市ID，要求是系统支持的时区城市ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) | 时区城市对应的时区对象。 |

## getTimezonesByLocation

```TypeScript
static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>
```

创建地理位置对应的时区对象数组。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>--><!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| longitude | double | Yes | 经度，范围[-180, 179.9)，东经取正值，西经取负值。 |
| latitude | double | Yes | 纬度，范围[-90, 89.9)，北纬取正值，南纬取负值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[TimeZone](arkts-localization-i18n-timezone-c.md)&gt; | 时区对象数组，数组中对象对应的时区为该地理位置推荐的时区。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

## getZoneRules

```TypeScript
public getZoneRules(): ZoneRules
```

获取时区跳变规则，时区的跳变逻辑参考[夏令时跳变](../../../internationalization/i18n-dst-transition.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-public getZoneRules(): ZoneRules--><!--Device-TimeZone-public getZoneRules(): ZoneRules-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ZoneRules](arkts-localization-i18n-zonerules-c.md) | 时区跳变规则，包含跳变的时间点、跳变前后的偏移量信息。 |

## isDaylightSavingTime

```TypeScript
public isDaylightSavingTime(date: Date): boolean
```

判断指定的时间日期是否处于夏令时。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean--><!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | 时间日期。 &lt;br&gt;**说明：** &lt;br&gt;月份从0开始计数，0表示一月。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否处于夏令时。true表示处于夏令时，false表示不处于夏令时。 |

## setAppDefaultTimeZoneById

```TypeScript
static setAppDefaultTimeZoneById(zoneID: string): void
```

设置当前应用的默认时区，在应用运行时生命周期内有效。

> **说明：**
> 
> 进行日期时间格式化时，若未指定时区，会优先使用应用设置的默认时区。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void--><!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoneID | string | Yes | 应用设置默认的时区ID，如："Asia/Shanghai"。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

