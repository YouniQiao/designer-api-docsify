# System

Provides system functions.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-i18n-export class System--><!--Device-i18n-export class System-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
```

## addPreferredLanguage

```TypeScript
static addPreferredLanguage(language: string, index?: int): void
```

Adds a preferred language to the specified position on the preferred language list.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static addPreferredLanguage(language: string, index?: int): void--><!--Device-System-static addPreferredLanguage(language: string, index?: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid ID of the language to be added as a preferred language. |
| index | int | No | Position to which the preferred language is added. The default value is the length of the preferred language list. <br>The value should be an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getSystemCollations

```TypeScript
static getSystemCollations(): Map<string, string>
```

Gets collations supported by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getSystemCollations(): Map<string, string>--><!--Device-System-static getSystemCollations(): Map<string, string>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;string, string&gt; | The map will containing the collation's identifier and name. If the map is empty of the collation for given locale does not need to be set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getSystemMeasurements

```TypeScript
static getSystemMeasurements(): Map<string, string>
```

Gets measurements supported by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getSystemMeasurements(): Map<string, string>--><!--Device-System-static getSystemMeasurements(): Map<string, string>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;string, string&gt; | a map will containing identifier and name of measurements supported by system locale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getSystemNumberPatterns

```TypeScript
static getSystemNumberPatterns(): Map<string, string>
```

Gets commonly used number patterns for system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getSystemNumberPatterns(): Map<string, string>--><!--Device-System-static getSystemNumberPatterns(): Map<string, string>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;string, string&gt; | a map containing the used number patterns and example of system locale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getSystemNumberingSystems

```TypeScript
static getSystemNumberingSystems(): Map<string, string>
```

Gets numbering systems supported by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getSystemNumberingSystems(): Map<string, string>--><!--Device-System-static getSystemNumberingSystems(): Map<string, string>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;string, string&gt; | a map will containing the numbering system 's identifier and sample. If the map is empty, there is no local digit for given locale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getSystemNumericalDatePatterns

```TypeScript
static getSystemNumericalDatePatterns(): Map<string, string>
```

Gets numerical date patterns and examples supported by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getSystemNumericalDatePatterns(): Map<string, string>--><!--Device-System-static getSystemNumericalDatePatterns(): Map<string, string>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;string, string&gt; | a map containing the date patterns and examples |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getUsingCollation

```TypeScript
static getUsingCollation(): string
```

Gets collation currently used by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getUsingCollation(): string--><!--Device-System-static getUsingCollation(): string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | The identifier of the collation model used by system locale will be return. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getUsingMeasurement

```TypeScript
static getUsingMeasurement(): string
```

Gets measurement currently used by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getUsingMeasurement(): string--><!--Device-System-static getUsingMeasurement(): string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | The identifier of measurement system using by system locale |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getUsingNumberPattern

```TypeScript
static getUsingNumberPattern(): string
```

Gets number pattern used by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getUsingNumberPattern(): string--><!--Device-System-static getUsingNumberPattern(): string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | The number pattern identifier used by system locale |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getUsingNumberingSystem

```TypeScript
static getUsingNumberingSystem(): string
```

Gets numbering system currently used by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getUsingNumberingSystem(): string--><!--Device-System-static getUsingNumberingSystem(): string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | the numbering systems's identifier. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## getUsingNumericalDatePattern

```TypeScript
static getUsingNumericalDatePattern(): string
```

Gets numerical date pattern currently used by system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-System-static getUsingNumericalDatePattern(): string--><!--Device-System-static getUsingNumericalDatePattern(): string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | The numerical date pattern used by system locale |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## removePreferredLanguage

```TypeScript
static removePreferredLanguage(index: int): void
```

Removes a preferred language from the specified position on the preferred language list.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static removePreferredLanguage(index: int): void--><!--Device-System-static removePreferredLanguage(index: int): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Position of the preferred language to delete. <br>The value should be an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed.<br>**Applicable version:** 23 - 24 |

## set24HourClock

```TypeScript
static set24HourClock(option: boolean): void
```

Sets whether to use the 24-hour clock.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static set24HourClock(option: boolean): void--><!--Device-System-static set24HourClock(option: boolean): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | boolean | Yes | Whether to use the 24-hour clock. The value "true" means to use the 24-hour clock, the the value "false" means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed.<br>**Applicable version:** 23 - 24 |

## setFirstDayOfWeek

```TypeScript
static setFirstDayOfWeek(type: WeekDay): void
```

Sets the first day of a week.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setFirstDayOfWeek(type: WeekDay): void--><!--Device-System-static setFirstDayOfWeek(type: WeekDay): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [WeekDay](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-weekday-e.md) | Yes | Start day of a week. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setSystemCollation

```TypeScript
static setSystemCollation(identifier: string): void
```

Sets the system collation mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemCollation(identifier: string): void--><!--Device-System-static setSystemCollation(identifier: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identifier | string | Yes | Identifier of the collation mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## setSystemLanguage

```TypeScript
static setSystemLanguage(language: string): void
```

Sets the system language.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemLanguage(language: string): void--><!--Device-System-static setSystemLanguage(language: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Valid language ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setSystemMeasurement

```TypeScript
static setSystemMeasurement(identifier: string): void
```

Sets the measurement system used by the system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemMeasurement(identifier: string): void--><!--Device-System-static setSystemMeasurement(identifier: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identifier | string | Yes | Identifier of the measurement system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## setSystemNumberPattern

```TypeScript
static setSystemNumberPattern(pattern: string): void
```

Sets the number pattern used by the system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumberPattern(pattern: string): void--><!--Device-System-static setSystemNumberPattern(pattern: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pattern | string | Yes | Identifier of the number pattern. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## setSystemNumberingSystem

```TypeScript
static setSystemNumberingSystem(identifier: string): void
```

Sets the numbering system used by the system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumberingSystem(identifier: string): void--><!--Device-System-static setSystemNumberingSystem(identifier: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identifier | string | Yes | Identifier of the numbering system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## setSystemNumericalDatePattern

```TypeScript
static setSystemNumericalDatePattern(identifier : string): void
```

Sets the numerical date pattern used by the system locale.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemNumericalDatePattern(identifier : string): void--><!--Device-System-static setSystemNumericalDatePattern(identifier : string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identifier | string | Yes | Identifier of the numerical date pattern. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8900001](../../apis-localization-kit/errorcode-i18n.md#8900001-parameter-verification-error) | Invalid parameter. Possible causes: Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## setSystemRegion

```TypeScript
static setSystemRegion(region: string): void
```

Sets the system region.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setSystemRegion(region: string): void--><!--Device-System-static setSystemRegion(region: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| region | string | Yes | Valid region ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setTemperatureType

```TypeScript
static setTemperatureType(type: TemperatureType): void
```

Sets the temperature unit of the system.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setTemperatureType(type: TemperatureType): void--><!--Device-System-static setTemperatureType(type: TemperatureType): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TemperatureType](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-temperaturetype-e.md) | Yes | Temperature unit. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## setUsingLocalDigit

```TypeScript
static setUsingLocalDigit(flag: boolean): void
```

Specifies whether to enable use of local digits.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-System-static setUsingLocalDigit(flag: boolean): void--><!--Device-System-static setUsingLocalDigit(flag: boolean): void-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flag | boolean | Yes | Whether to turn on the local digit switch. The value "true" means to turn on the local digit switch, and the value "false" indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |

