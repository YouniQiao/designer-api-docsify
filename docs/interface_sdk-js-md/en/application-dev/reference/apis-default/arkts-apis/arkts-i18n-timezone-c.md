# TimeZone

Provides the API for accessing TimeZone name, rawOffset and offset information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-i18n-export class TimeZone--><!--Device-i18n-export class TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## getAppDefaultTimeZone

```TypeScript
static getAppDefaultTimeZone(): TimeZone
```

Obtains the default time zone object used by an application. If the default time zone has been set by calling setAppDefaultTimeZoneById, the default time zone object is returned. Otherwise, the system time zone object is returned.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone--><!--Device-TimeZone-static getAppDefaultTimeZone(): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [TimeZone](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-timezone-c.md) | TimeZone object, first set by application, then system time zone, last GMT time zone. |

## getAvailableIDs

```TypeScript
static getAvailableIDs(): Array<string>
```

Obtains the list of time zone IDs supported by the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getAvailableIDs(): Array<string>--><!--Device-TimeZone-static getAvailableIDs(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of time zone IDs supported by the system. |

## getAvailableZoneCityIDs

```TypeScript
static getAvailableZoneCityIDs(): Array<string>
```

Obtains the list of time zone city IDs supported by the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>--><!--Device-TimeZone-static getAvailableZoneCityIDs(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of time zone city IDs supported by the system. |

## getCityDisplayName

```TypeScript
static getCityDisplayName(cityID: string, locale: string): string
```

Obtains time zone city display name in the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string--><!--Device-TimeZone-static getCityDisplayName(cityID: string, locale: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cityID | string | Yes | Time zone city ID. |
| locale | string | Yes | System locale, which consists of the language, script, and country/region. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Time zone city display name in the specified language. |

## getDisplayName

```TypeScript
getDisplayName(locale?: string, isDST?: boolean): string
```

Obtains time zone display name in the specified language.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string--><!--Device-TimeZone-getDisplayName(locale?: string, isDST?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | System locale, which consists of the language, script, and country/region. The default value is the current system locale. |
| isDST | boolean | No | Whether DST information is displayed. The value "true" indicates that DST information is displayed, and the value "false" indicates the opposite. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Time zone display name in the specified language. |

## getID

```TypeScript
getID(): string
```

Obtains the ID of the specified TimeZone object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getID(): string--><!--Device-TimeZone-getID(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Time zone ID corresponding to the TimeZone object. |

## getOffset

```TypeScript
getOffset(date?: double): int
```

Obtains the offset of the specified time zone at the specified time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getOffset(date?: double): int--><!--Device-TimeZone-getOffset(date?: double): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | double | No | Specified time, in milliseconds. The default value is the system time. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Time zone offset, in milliseconds. When the DST is used, the time zone offset is the raw time zone offset plus the DST offset. |

## getRawOffset

```TypeScript
getRawOffset(): int
```

Obtains the raw offset of the specified time zone.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-getRawOffset(): int--><!--Device-TimeZone-getRawOffset(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Raw offset of the time zone, in milliseconds. |

## getTimezoneFromCity

```TypeScript
static getTimezoneFromCity(cityID: string): TimeZone
```

Creates a TimeZone object corresponding to the specified time zone city.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone--><!--Device-TimeZone-static getTimezoneFromCity(cityID: string): TimeZone-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cityID | string | Yes | Time zone city ID. The value must be a time zone city ID supported by the system. |

**Return value:**

| Type | Description |
| --- | --- |
| [TimeZone](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-timezone-c.md) | TimeZone object corresponding to the specified time zone city ID. |

## getTimezonesByLocation

```TypeScript
static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>
```

Creates an array of TimeZone objects corresponding to the specified location.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>--><!--Device-TimeZone-static getTimezonesByLocation(longitude: double, latitude: double): Array<TimeZone>-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| longitude | double | Yes | Longitude. The value range is [-180, 179.9). A positive value is used for east longitude and a negative value is used for west longitude. |
| latitude | double | Yes | Latitude. The value range is [-90, 89.9). A positive value is used for north latitude and a negative value is used for south latitude. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[TimeZone](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-timezone-c.md)&gt; | TimeZone objects corresponding to the specified location. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getZoneRules

```TypeScript
public getZoneRules(): ZoneRules
```

Get the zone rules object corresponds to the timezone objects.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TimeZone-public getZoneRules(): ZoneRules--><!--Device-TimeZone-public getZoneRules(): ZoneRules-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [ZoneRules](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-zonerules-c.md) | Returns a ZoneRuels object which defines timezone offset changing rule. |

## isDaylightSavingTime

```TypeScript
public isDaylightSavingTime(date: Date): boolean
```

Check if the given date use daylight saving time. The calculation will be based on the matched time zone rules.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean--><!--Device-TimeZone-public isDaylightSavingTime(date: Date): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Date and time. Note: The month starts from **0**, indicating January. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the date use daylight saving time, and false otherwise. |

## setAppDefaultTimeZoneById

```TypeScript
static setAppDefaultTimeZoneById(zoneID: string): void
```

Sets the default time zone for the current app, the value will be used on the application's runtime lifecycle. When the date time formatting function is used, the default time zone ID of the app is used preferentially.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void--><!--Device-TimeZone-static setAppDefaultTimeZoneById(zoneID: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoneID | string | Yes | Time zone ID that set default for app. for example, "Asia/Shanghai". <br> Time zone ID supported by the system |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |

