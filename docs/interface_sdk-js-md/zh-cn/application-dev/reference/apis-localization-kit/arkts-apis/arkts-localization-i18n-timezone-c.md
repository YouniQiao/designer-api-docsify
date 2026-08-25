# TimeZone

提供时区相关的能力，包括时区名称翻译、偏移量获取和跳变规则获取等。

**起始版本：** 7

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getAppDefaultTimeZone

```TypeScript
static getAppDefaultTimeZone(): TimeZone
```

获取应用使用的默认时区对象。若调用[setAppDefaultTimeZoneById](#setappdefaulttimezonebyid)设置了默认时区，则返回设置的默认时区对象；否 则，返回系统时区对象。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |

## getAvailableIDs

```TypeScript
static getAvailableIDs(): Array<string>
```

获取系统支持的时区ID列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getAvailableZoneCityIDs

```TypeScript
static getAvailableZoneCityIDs(): Array<string>
```

获取系统支持的时区城市ID列表。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## getCityDisplayName

```TypeScript
static getCityDisplayName(cityID: string, locale: string): string
```

获取时区城市名称在指定语言下的翻译。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

## getDisplayName

```TypeScript
getDisplayName(locale?: string, isDST?: boolean): string
```

获取时区对象名称在指定语言下的翻译。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

## getID

```TypeScript
getID(): string
```

获取时区对象的ID。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## getOffset

```TypeScript
getOffset(date?: number): number
```

获取某一时刻时区对象所表示时区的偏移量。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| date | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## getRawOffset

```TypeScript
getRawOffset(): number
```

获取时区对象所表示时区的原始偏移量。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getTimezoneFromCity

```TypeScript
static getTimezoneFromCity(cityID: string): TimeZone
```

创建对应时区城市的时区对象。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cityID | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TimeZone](arkts-localization-i18n-timezone-c.md) |

## getTimezonesByLocation

```TypeScript
static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>
```

创建地理位置对应的时区对象数组。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

## getZoneRules

```TypeScript
public getZoneRules(): ZoneRules
```

获取时区跳变规则，时区的跳变逻辑参考[夏令时跳变](../../../internationalization/i18n-dst-transition.md)。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

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

设置当前应用的默认时区，在应用运行时生命周期内有效。

> **说明：**&gt;
> 进行日期时间格式化时，若未指定时区，会优先使用应用设置的默认时区。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| zoneID | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [8900001](../errorcode-i18n.md#8900001-参数校验错误) |
