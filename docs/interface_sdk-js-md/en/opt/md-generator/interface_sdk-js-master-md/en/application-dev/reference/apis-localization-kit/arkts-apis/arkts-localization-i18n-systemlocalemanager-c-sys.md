# SystemLocaleManager (System API)

Provide some functions for settings and startup guide to select language or region.

**Since:** 23

**Deprecated since:** -1

<!--Device-i18n-export class SystemLocaleManager--><!--Device-i18n-export class SystemLocaleManager-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## constructor

```TypeScript
constructor()
```

Creates a SystemLocaleManager object.

**Since:** 23

**Deprecated since:** -1

<!--Device-SystemLocaleManager-constructor()--><!--Device-SystemLocaleManager-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
```

## getLanguageInfoArray

```TypeScript
getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>
```

Obtains the list of languages after sorting.

**Since:** 23

**Deprecated since:** -1

<!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getLanguageInfoArray(languages: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [languages](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontdescriptor-i.md) | Array & lt;string & gt; | Yes |
| options | [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[LocaleItem](arkts-localization-i18n-localeitem-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// Assume that the system language is zh-Hans, the system region is CN, and the system locale is zh-Hans-CN.
let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
let languages: string[] = ["zh-Hans", "en-US", "pt", "ar"];
let sortOptions: i18n.SortOptions = {locale: "zh-Hans-CN", isUseLocalName: true, isSuggestedFirst: true};
try {
    // The language list after sorting is [zh-Hans, en-US, pt, ar].
    let sortedLanguages: Array<i18n.LocaleItem> = systemLocaleManager.getLanguageInfoArray(languages, sortOptions);
} catch(error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call systemLocaleManager.getLanguageInfoArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getRegionInfoArray

```TypeScript
getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>
```

Obtains the IDs of the countries or regions after sorting.

**Since:** 23

**Deprecated since:** -1

<!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>--><!--Device-SystemLocaleManager-getRegionInfoArray(regions: Array<string>, options?: SortOptions): Array<LocaleItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| regions | Array & lt;string & gt; | Yes |
| options | [SortOptions](arkts-localization-i18n-sortoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[LocaleItem](arkts-localization-i18n-localeitem-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [890001](../errorcode-i18n.md#890001-parameter-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// Assume that the system language is zh-Hans, the system region is CN, and the system locale is zh-Hans-CN.
let systemLocaleManager: i18n.SystemLocaleManager = new i18n.SystemLocaleManager();
let regions: string[] = ["CN", "US", "PT", "EG"];
let sortOptions: i18n.SortOptions = {locale: "zh-Hans-CN", isUseLocalName: false, isSuggestedFirst: true};
try {
    // The country/region list after sorting is [CN, EG, US, PT].
    let sortedRegions: Array<i18n.LocaleItem> = systemLocaleManager.getRegionInfoArray(regions, sortOptions);
} catch(error) {
    let err: BusinessError = error as BusinessError;
    console.error(`call systemLocaleManager.getRegionInfoArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

## getTimeZoneCityItemArray

```TypeScript
static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>
```

Obtains list of time zone city items after sorting.

**Since:** 23

**Deprecated since:** -1

<!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>--><!--Device-SystemLocaleManager-static getTimeZoneCityItemArray(): Array<TimeZoneCityItem>-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[TimeZoneCityItem](arkts-localization-i18n-timezonecityitem-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let timeZoneCityItemArray: Array<i18n.TimeZoneCityItem> = i18n.SystemLocaleManager.getTimeZoneCityItemArray();
  for (let i = 0; i < timeZoneCityItemArray.length; i++) {
      console.info(timeZoneCityItemArray[i].zoneId + ", " + timeZoneCityItemArray[i].cityId + ", " + timeZoneCityItemArray[i].cityDisplayName +
          ", " + timeZoneCityItemArray[i].offset + "\r\n");
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SystemLocaleManager.getTimeZoneCityItemArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```
