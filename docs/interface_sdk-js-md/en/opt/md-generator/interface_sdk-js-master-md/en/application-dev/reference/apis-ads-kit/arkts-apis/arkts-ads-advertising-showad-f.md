# showAd

## Modules to Import

```TypeScript
```

## showAd

```TypeScript
function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void
```

Shows a full-screen ad. > **NOTE：**> > 1. To ensure that ads can be displayed correctly, this API must be used together with the ad request API. > > 2. This API only supports displaying rewarded ads and interstitial ads.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-advertising-function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void--><!--Device-advertising-function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ad | [Advertisement](arkts-ads-advertisement-advertisement-i.md) | Yes |
| options | [AdDisplayOptions](arkts-ads-advertising-addisplayoptions-i.md) | Yes |
| context | common.UIAbilityContext | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [21800004](../errorcode-ads.md#21800004-ad-display-failure) |
| [21800001](../errorcode-ads.md#21800001-internal-system-error) |

**Examples**

For details about how to obtain the context, see [Acquisition of Context](../../../application-models/application-context-stage.md#acquisition-of-context).

```TypeScript
import { common } from '@kit.AbilityKit';
import { advertising } from '@kit.AdsKit';

function showAd(ad: advertising.Advertisement, context?: common.UIAbilityContext): void {
  // Ad display parameters. You can set the parameters based on the project requirements.
  const adDisplayOptions: advertising.AdDisplayOptions = {};
  // Show the ad.
  advertising.showAd(ad, adDisplayOptions, context);
}
```
