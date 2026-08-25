# AdLoadListener

Enumerates the callbacks used for the request for loading an ad.

**Since:** 11

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## onAdLoadFailure

```TypeScript
onAdLoadFailure(errorCode: number, errorMsg: string): void
```

Called when an ad request fails.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| errorCode | number | Yes |
| errorMsg | string | Yes |

## onAdLoadSuccess

```TypeScript
onAdLoadSuccess(ads: Array<Advertisement>): void
```

Called when an ad request is successful.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ads](arkts-ads-advertising-adcomponent-adcomponent-s.md) | Array & lt;Advertisement & gt; | Yes |
