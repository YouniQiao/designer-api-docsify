# @ohos.advertising(Ads Service Framework)

The advertising module provides APIs for requesting and displaying ads.

> **NOTE：**
> The initial APIs of this module are supported since API version 11.
> Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Since:** 11

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { AdComponent } from '@kit.AdsKit.AdComponent';
import AdsServiceExtensionAbility, { RespCallback } from '@kit.AdsKit.AdsServiceExtensionAbility';
import { AutoAdComponent } from '@kit.AdsKit.AutoAdComponent';
import advertising from '@kit.AdsKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [deleteWebAdInterface(Ads Service Framework)](arkts-ads-advertising-deletewebadinterface-f.md) | Deletes the ad JavaScript object injected through **registerWebAdInterface** (this API is only open to some pre-installed system applications). |
| [getAdRequestBody(Ads Service Framework)](arkts-ads-advertising-getadrequestbody-f.md) | Obtains the body of an ad request. This API uses a promise to return the result (this API is only open to some pre-installed system applications). |
| [parseAdResponse(Ads Service Framework)](arkts-ads-advertising-parseadresponse-f.md) | Parses and processes the body of an ad response (this API is only open to some pre-installed system applications). |
| [registerWebAdInterface(Ads Service Framework)](arkts-ads-advertising-registerwebadinterface-f.md) | Injects an ad JavaScript object to the **Web** component (this API is only open to some pre-installed system applications). |
| [registerWebAdInterface(Ads Service Framework)](arkts-ads-advertising-registerwebadinterface-f.md) | Injects an ad JavaScript object to the **Web** component (this API is only open to some pre-installed system applications). |
| [showAd(Ads Service Framework)](arkts-ads-advertising-showad-f.md) | Shows a full-screen ad. |

### Classes

| Name | Description |
| --- | --- |
| [AdLoader(Ads Service Framework)](arkts-ads-advertising-adloader-c.md) | Provides the APIs for loading ads. |

### Interfaces

| Name | Description |
| --- | --- |
| [AdDisplayOptions(Ads Service Framework)](arkts-ads-advertising-addisplayoptions-i.md) | Defines the ad display parameters. |
| [AdInteractionListener(Ads Service Framework)](arkts-ads-advertising-adinteractionlistener-i.md) | Defines the ad status change callback. |
| [AdLoadListener(Ads Service Framework)](arkts-ads-advertising-adloadlistener-i.md) | Enumerates the callbacks used for the request for loading an ad. |
| [AdOptions(Ads Service Framework)](arkts-ads-advertising-adoptions-i.md) | Defines the ad configuration. |
| [AdRequestParams(Ads Service Framework)](arkts-ads-advertising-adrequestparams-i.md) | Defines the ad request parameters. |
| [MultiSlotsAdLoadListener(Ads Service Framework)](arkts-ads-advertising-multislotsadloadlistener-i.md) | Enumerates the callbacks used for the request for loading multiple ads. |

### Types

| Name | Description |
| --- | --- |
| [Advertisement(Ads Service Framework)](arkts-ads-advertising-advertisement-t.md) | Defines the requested ad content. |
