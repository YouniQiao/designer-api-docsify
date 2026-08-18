# TimeZone

提供时区相关的能力，包括时区名称翻译、偏移量获取和跳变规则获取等。

**起始版本：** 23

<!--Device-i18n-export class TimeZone--><!--Device-i18n-export class TimeZone-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
```

## getAppDefaultTimeZone

```TypeScript
static getAppDefaultTimeZone(): TimeZone
```

获取应用使用的默认时区对象。若调用[setAppDefaultTimeZoneById](#setappdefaulttimezonebyid)设置了默认时区，则返回设置的默认时区对象；否 则，返回系统时区对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone--><!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let zoneID: string = 'Asia/Shanghai';
  i18n.TimeZone.setAppDefaultTimeZoneById(zoneID);
  console.info('setAppDefaultTimeZoneById success.');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call TimeZone.setAppDefaultTimeZoneById failed, error code: ${err.code}, message: ${err.message}.`);
}
let timeZone: i18n.TimeZone = i18n.TimeZone.getAppDefaultTimeZone();
let id: string = timeZone.getID();
console.info(`getAppDefaultTimeZone success, time zone id: ${id}`);
```

## getAvailableIDs

```TypeScript
static getAvailableIDs(): Array<string>
```

获取系统支持的时区ID列表。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getAvailableIDs(): Array<string>--><!--Device-TimeZone-static getAvailableIDs(): Array<string>-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// ids = ['America/Adak', 'America/Anchorage', 'America/Bogota', 'America/Denver', 'America/Los_Angeles', 'America/Montevideo', 'America/Santiago', 'America/Sao_Paulo', 'Asia/Ashgabat', 'Asia/Hovd', 'Asia/Jerusalem', 'Asia/Magadan', 'Asia/Omsk', 'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Yerevan', 'Atlantic/Cape_Verde', 'Australia/Lord_Howe', 'Europe/Dublin', 'Europe/London', 'Europe/Moscow', 'Pacific/Auckland', 'Pacific/Easter', 'Pacific/Pago-Pago']
let ids: Array<string> = i18n.TimeZone.getAvailableIDs();
```

## getAvailableZoneCityIDs

```TypeScript
static getAvailableZoneCityIDs(): Array<string>
```

获取系统支持的时区城市ID列表。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>--><!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// cityIDs = ['Auckland', 'Magadan', 'Lord Howe Island', 'Tokyo', 'Shanghai', 'Hovd', 'Omsk', 'Ashgabat', 'Yerevan', 'Moscow', 'Tel Aviv', 'Dublin', 'London', 'Praia', 'Montevideo', 'Brasília', 'Santiago', 'Bogotá', 'Easter Island', 'Salt Lake City', 'Los Angeles', 'Anchorage', 'Adak', 'Pago Pago']
let cityIDs: Array<string> = i18n.TimeZone.getAvailableZoneCityIDs();
```

## getCityDisplayName

```TypeScript
static getCityDisplayName(cityID: string, locale: string): string
```

获取时区城市名称在指定语言下的翻译。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string--><!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cityID | string | 是 |
| locale | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let displayName: string = i18n.TimeZone.getCityDisplayName('Shanghai', 'zh-CN'); // displayName = '上海 (中国)'
```

## getDisplayName

```TypeScript
getDisplayName(locale?: string, isDST?: boolean): string
```

获取时区对象名称在指定语言下的翻译。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string--><!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| locale | string | 否 |
| isDST | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneName: string = timezone.getDisplayName('zh-CN', false); // timezoneName = '中国标准时间'
```

## getID

```TypeScript
getID(): string
```

获取时区对象的ID。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-getID(): string--><!--Device-TimeZone-getID(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneID: string = timezone.getID(); // timezoneID = 'Asia/Shanghai'
```

## getOffset

```TypeScript
getOffset(date?: number): number
```

获取某一时刻时区对象所表示时区的偏移量。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-getOffset(date?: double): int--><!--Device-TimeZone-getOffset(date?: double): int-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getOffset(1234567890); // offset = 28800000
```

## getRawOffset

```TypeScript
getRawOffset(): number
```

获取时区对象所表示时区的原始偏移量。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-getRawOffset(): int--><!--Device-TimeZone-getRawOffset(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getRawOffset(); // offset = 28800000
```

## getTimezoneFromCity

```TypeScript
static getTimezoneFromCity(cityID: string): TimeZone
```

创建对应时区城市的时区对象。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone--><!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cityID | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.TimeZone.getTimezoneFromCity('Shanghai');
```

## getTimezonesByLocation

```TypeScript
static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>
```

创建地理位置对应的时区对象数组。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>--><!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| longitude | number | 是 |
| latitude | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[TimeZone](arkts-localization-i18n-timezone-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [890001](../errorcode-i18n.md#890001-参数校验错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let timezoneArray: Array<i18n.TimeZone> = i18n.TimeZone.getTimezonesByLocation(-118.1, 34.0);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call TimeZone.getTimezonesByLocation failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getZoneRules

```TypeScript
public getZoneRules(): ZoneRules
```

获取时区跳变规则，时区的跳变逻辑参考[夏令时跳变](../../../internationalization/i18n-dst-transition.md)。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-public getZoneRules(): ZoneRules--><!--Device-TimeZone-public getZoneRules(): ZoneRules-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [ZoneRules](arkts-localization-i18n-zonerules-c.md) |

## isDaylightSavingTime

```TypeScript
public isDaylightSavingTime(date: Date): boolean
```

判断指定的时间日期是否处于夏令时。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean--><!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | Date | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setAppDefaultTimeZoneById

```TypeScript
static setAppDefaultTimeZoneById(zoneID: string): void
```

设置当前应用的默认时区，在应用运行时生命周期内有效。 > **说明：** > > 进行日期时间格式化时，若未指定时区，会优先使用应用设置的默认时区。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void--><!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| zoneID | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let zoneID: string = 'Asia/Shanghai';
  i18n.TimeZone.setAppDefaultTimeZoneById(zoneID);
  console.info('setAppDefaultTimeZoneById success.');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call TimeZone.setAppDefaultTimeZoneById failed, error code: ${err.code}, message: ${err.message}.`);
}
```
