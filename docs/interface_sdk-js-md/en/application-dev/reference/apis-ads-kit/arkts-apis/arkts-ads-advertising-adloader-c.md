# AdLoader

Provides the APIs for loading ads.

**Since:** 11

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## constructor

```TypeScript
constructor(context: common.Context)
```

Constructor.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |

## loadAd

```TypeScript
loadAd(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void
```

Loads an ad.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [adParam](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md) | Yes |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | Yes |
| listener | [AdLoadListener](arkts-ads-advertising-adloadlistener-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |
| [21800003](../errorcode-ads.md#21800003-ad-loading-failure) |
| [801](../errorcode-ads.md#801-ad-request-failure) |

## loadAdWithMultiSlots

```TypeScript
loadAdWithMultiSlots(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void
```

Loads multiple ads.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| adParams | [AdRequestParams](arkts-ads-advertising-adrequestparams-i.md)[] | Yes |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | [AdOptions](arkts-ads-advertising-adoptions-i.md) | Yes |
| listener | [MultiSlotsAdLoadListener](arkts-ads-advertising-multislotsadloadlistener-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |
| [21800003](../errorcode-ads.md#21800003-ad-loading-failure) |
| [801](../errorcode-ads.md#801-ad-request-failure) |
