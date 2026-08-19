# SystemLocaleManager (System API)

Provide some functions for settings and startup guide to select language or region.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-i18n-export class SystemLocaleManager--><!--Device-i18n-export class SystemLocaleManager-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Creates a SystemLocaleManager object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SystemLocaleManager-constructor()--><!--Device-SystemLocaleManager-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 26.0.0 and later |

## getLanguageInfoArray

```TypeScript
getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>
```

Obtains the list of languages after sorting.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| languages | Array&lt;string&gt; | Yes | Valid IDs of the languages to be sorted. |
| options | [SortOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-sortoptions-i-sys.md) | No | Language sorting option. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[LocaleItem](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-localeitem-i-sys.md)&gt; | Language list after sorting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getRegionInfoArray

```TypeScript
getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>
```

Obtains the IDs of the countries or regions after sorting.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regions | Array&lt;string&gt; | Yes | Valid IDs of the countries or regions to be sorted. |
| options | [SortOptions](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-sortoptions-i-sys.md) | No | Country/region sorting option. By default, locale is the current system locale, isUseLocalName is false, and isSuggestedFirst is true. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[LocaleItem](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-localeitem-i-sys.md)&gt; | IDs of the countries or regions after sorting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [890001](../../apis-localization-kit/errorcode-i18n.md#890001-parameter-error) | Invalid parameter. Possible causes: Parameter verification failed. |

## getTimeZoneCityItemArray

```TypeScript
static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>
```

Obtains list of time zone city items after sorting.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>--><!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[TimeZoneCityItem](../../apis-localization-kit/arkts-apis/arkts-localization-i18n-timezonecityitem-i-sys.md)&gt; | List of time zone city items after sorting. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

