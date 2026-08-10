# AdsServiceExtensionAbility (System API)

本模块为设备厂商提供广告扩展能力，设备厂商可自主实现单广告位请求和多广告位请求的业务逻辑。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-export default class AdsServiceExtensionAbility--><!--Device-unnamed-export default class AdsServiceExtensionAbility-End-->

**System capability:** SystemCapability.Advertising.Ads

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { RespCallback } from 'kits/@kit.AdsKit';
```

## onLoadAd

```TypeScript
onLoadAd(adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, respCallback: RespCallback)
```

单广告位请求业务实现方法，设备厂商需在该方法中实现广告请求业务逻辑并将结果回调给媒体。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AdsServiceExtensionAbility-onLoadAd(adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, respCallback: RespCallback)--><!--Device-AdsServiceExtensionAbility-onLoadAd(adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, respCallback: RespCallback)-End-->

**System capability:** SystemCapability.Advertising.Ads

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adParam | advertising.AdRequestParams | Yes | 广告请求参数。 |
| adOptions | advertising.AdOptions | Yes | 广告配置参数。 |
| respCallback | [RespCallback](arkts-ads-advertising-adsserviceextensionability-respcallback-i.md) | Yes | 广告请求回调。 |

## Examples

```TypeScript
import { AdsServiceExtensionAbility, advertising, RespCallback } from '@kit.AdsKit';

export default class AdsExtensionAbility extends AdsServiceExtensionAbility {
  onLoadAd(adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, respCallback: RespCallback) {
    const respData: Map<string, Array<advertising.Advertisement>> = new Map();
    // Set the returned ad data.
    // ...
    respCallback(respData);
  }
}
```

## onLoadAdWithMultiSlots

```TypeScript
onLoadAdWithMultiSlots(adParams: advertising.AdRequestParams[], adOptions: advertising.AdOptions, 
    respCallback: RespCallback)
```

多广告位请求业务实现方法，设备厂商需在该方法中实现广告请求业务逻辑并将结果回调给媒体。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-AdsServiceExtensionAbility-onLoadAdWithMultiSlots(adParams: advertising.AdRequestParams[], adOptions: advertising.AdOptions,     respCallback: RespCallback)--><!--Device-AdsServiceExtensionAbility-onLoadAdWithMultiSlots(adParams: advertising.AdRequestParams[], adOptions: advertising.AdOptions,     respCallback: RespCallback)-End-->

**System capability:** SystemCapability.Advertising.Ads

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adParams | advertising.AdRequestParams[] | Yes | 广告请求参数。 |
| adOptions | advertising.AdOptions | Yes | 广告配置参数。 |
| respCallback | [RespCallback](arkts-ads-advertising-adsserviceextensionability-respcallback-i.md) | Yes | 广告请求回调。 |

## Examples

```TypeScript
import { AdsServiceExtensionAbility, advertising, RespCallback } from '@kit.AdsKit';

export default class AdsExtensionAbility extends AdsServiceExtensionAbility {
  onLoadAdWithMultiSlots(adParams: advertising.AdRequestParams[], adOptions: advertising.AdOptions,
    respCallback: RespCallback) {
    const respData: Map<string, Array<advertising.Advertisement>> = new Map();
    // Set the returned ad data.
    // ...
    respCallback(respData);
  }
}
```

