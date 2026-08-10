# AdComponent

本模块提供展示广告的能力，覆盖了原生、贴片、开屏等广告样式。

> **说明：**
> 
> 为了保证广告能正确展示，该接口必须和请求广告接口配套使用。效果和使用方法可参考
> [原生广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-native)、
> [贴片广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll)、
> [开屏广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-splash)
> 接入和展示。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Decorator:** @Component

<!--Device-unnamed-declare struct AdComponent--><!--Device-unnamed-declare struct AdComponent-End-->

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { AdComponent } from 'kits/@kit.AdsKit';
```

## adRenderer

```TypeScript
adRenderer?: () => void
```

应用自渲染广告样式。应用自渲染广告样式为受限使用能力，具体请前往  
[流量变现官网客服支持](https://developer.huawei.com/consumer/cn/doc/monetize/kefuzhichi-0000001104461922)进行咨询。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @BuilderParam

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AdComponent-adRenderer?: () => void--><!--Device-AdComponent-adRenderer?: () => void-End-->

**System capability:** SystemCapability.Advertising.Ads

## build

```TypeScript
build(): void
```

用于创建AdComponent对象的构造函数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdComponent-build(): void--><!--Device-AdComponent-build(): void-End-->

**System capability:** SystemCapability.Advertising.Ads

## ads

```TypeScript
ads: advertising.Advertisement[]
```

广告对象数组。

说明：非贴片广告类型，组件只展示数组第一个数据。

**Type:** advertising.Advertisement[]

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdComponent-ads: advertising.Advertisement[]--><!--Device-AdComponent-ads: advertising.Advertisement[]-End-->

**System capability:** SystemCapability.Advertising.Ads

## displayOptions

```TypeScript
displayOptions: advertising.AdDisplayOptions
```

广告展示参数。

**Type:** advertising.AdDisplayOptions

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdComponent-displayOptions: advertising.AdDisplayOptions--><!--Device-AdComponent-displayOptions: advertising.AdDisplayOptions-End-->

**System capability:** SystemCapability.Advertising.Ads

## interactionListener

```TypeScript
interactionListener: advertising.AdInteractionListener
```

广告状态变化回调。

**Type:** advertising.AdInteractionListener

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdComponent-interactionListener: advertising.AdInteractionListener--><!--Device-AdComponent-interactionListener: advertising.AdInteractionListener-End-->

**System capability:** SystemCapability.Advertising.Ads

## rollPlayState

```TypeScript
rollPlayState?: number
```

用于对外提供贴片广告播放状态，设置1为播放，2为暂停，默认值为2，其他值为非法值，不改变之前的播放状态。在贴片广告所在页面需要通过@State关联属性，使用方法参考  
[示例代码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll#展示广告)。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AdComponent-rollPlayState?: number--><!--Device-AdComponent-rollPlayState?: number-End-->

**System capability:** SystemCapability.Advertising.Ads

