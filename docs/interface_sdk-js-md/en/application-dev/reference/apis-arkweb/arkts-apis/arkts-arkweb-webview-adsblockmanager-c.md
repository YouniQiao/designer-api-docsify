# AdsBlockManager

AdsBlockManager is a class in the ArkWeb framework used to manage the ad filtering feature of Web components. It provides capabilities such as setting ad filtering rules, managing domain AllowedList/DisallowedList, and controlling filtering policies. All Web components in each app share a single AdsBlockManager static class. Developers can use this class to inject ad filtering configuration files that conform to the universal EasyList syntax into Web components and flexibly control the ad filtering status for specific websites.The core mechanism of AdsBlockManager is based on a two-tier AllowedList/DisallowedList strategy using domain suffix matching: the DisallowedList is used to disable ad filtering for specific websites, while the AllowedList has a higher priority and can re-enable ad filtering for certain subdomains within the scope of the DisallowedList. After successful internal parsing, ad filtering rules are persistently stored and do not need to be set again after an app restart. However, they are not persistent and must be reconfigured after an app restart.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## addAdsBlockAllowedList

```TypeScript
static addAdsBlockAllowedList(domainSuffixes: Array<string>): void
```

Adds an array of domain names to the AllowedList of this AdsBlockManager object. This API is typically used to re -enable ad filtering for certain websites in the DisallowedList.

> **NOTE：**&gt;
> - The domain names set by this API are not persistent; they need to be set again after the app is restarted.&gt;
> - The AllowedList has a higher priority than the DisallowedList. For example, if ['example.com'] is configured
> in the DisallowedList, ad filtering is disabled for all web pages under the example.com domain. To enable ad
> filtering for 'news.example.com', you can use addAdsBlockAllowedList(['news.example.com']).&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domainSuffixes | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## addAdsBlockDisallowedList

```TypeScript
static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void
```

Adds an array of domain names to the disallowed list of this **AdsBlockManager** object. When the ad blocking feature is enabled, ad blocking for these websites will be disabled.

> **NOTE：**&gt;
> - The domain names set by this API are not persistent; they need to be set again after the app is restarted.&gt;
> - The ad filtering feature uses suffix matching to determine whether the domainSuffix matches the URL of the
> current site. For example, if the website opened in the current Web component is https://www.example.com and
> the DisallowedList contains 'example.com' or 'www.example.com', the suffix match succeeds, ad filtering will be
> disabled for this website, and ad filtering will also be disabled when accessing 'https://m.example.com'.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domainSuffixes | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clearAdsBlockAllowedList

```TypeScript
static clearAdsBlockAllowedList(): void
```

Clears the allowed list of this **AdsBlockManager** object.

> **NOTE：**&gt;
> - The AllowedList of AdsBlockManager is not persistent; it needs to be set again after the app is restarted.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clearAdsBlockDisallowedList

```TypeScript
static clearAdsBlockDisallowedList(): void
```

Clears the disallowed list of this **AdsBlockManager** object.

> **NOTE：**&gt;
> - The DisallowedList of AdsBlockManager is not persistent; it needs to be set again after the app is restarted.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## removeAdsBlockAllowedList

```TypeScript
static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void
```

Removes an array of domain names from the allowed list of this **AdsBlockManager** object.

> **NOTE：**&gt;
> - The AllowedList of AdsBlockManager is not persistent; it needs to be set again after the app is restarted.
> Removing an entry that does not exist does not trigger an exception.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domainSuffixes | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## removeAdsBlockDisallowedList

```TypeScript
static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void
```

Removes an array of domain names from the disallowed list of this **AdsBlockManager** object.

> **NOTE：**&gt;
> - The DisallowedList of AdsBlockManager is not persistent; it needs to be set again after the app is restarted.
> Removing an entry that does not exist does not trigger an exception.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domainSuffixes | Array & lt;string & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setAdsBlockRules

```TypeScript
static setAdsBlockRules(rulesFile: string, replace: boolean): void
```

Sets a custom ad filtering configuration file that conforms to the universal EasyList syntax in the Web components.

> **NOTE：**&gt;
> - The ad filtering rules set by this API will be persistently stored after successful internal parsing; you do
> not need to set them again after the app is restarted.&gt;
> - Starting from API version 18, calling this API on a device that does not support the ad filtering feature
> will throw an 801 exception.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rulesFile | string | Yes |
| replace | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
