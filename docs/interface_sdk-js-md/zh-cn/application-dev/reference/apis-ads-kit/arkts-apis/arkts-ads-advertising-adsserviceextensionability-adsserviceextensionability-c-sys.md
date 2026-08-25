# AdsServiceExtensionAbility（系统接口）

本模块为设备厂商提供广告扩展能力，设备厂商可自主实现单广告位请求和多广告位请求的业务逻辑。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { AdsServiceExtensionAbility, RespCallback } from 'kits/@kit.AdsKit';
```

## onLoadAd

```TypeScript
onLoadAd(adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, respCallback: RespCallback)
```

单广告位请求业务实现方法，设备厂商需在该方法中实现广告请求业务逻辑并将结果回调给媒体。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [adParam](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | advertising.AdRequestParams | 是 |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | advertising.AdOptions | 是 |
| respCallback | [RespCallback](arkts-ads-advertising-adsserviceextensionability-respcallback-i.md) | 是 |

## onLoadAdWithMultiSlots

```TypeScript
onLoadAdWithMultiSlots(adParams: advertising.AdRequestParams[], adOptions: advertising.AdOptions, 
    respCallback: RespCallback)
```

多广告位请求业务实现方法，设备厂商需在该方法中实现广告请求业务逻辑并将结果回调给媒体。

**起始版本：** 11

**系统能力：** SystemCapability.Advertising.Ads

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| adParams | advertising.AdRequestParams[] | 是 |
| [adOptions](arkts-ads-advertising-autoadcomponent-autoadcomponent-s.md) | advertising.AdOptions | 是 |
| respCallback | [RespCallback](arkts-ads-advertising-adsserviceextensionability-respcallback-i.md) | 是 |
