# showAd

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## showAd

```TypeScript
function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void
```

展示全屏广告。

> **说明：**
> 
> 1. 为了保证广告能正确展示，该接口必须和请求广告接口配套使用。
> 
> 2. 该接口仅支持展示激励广告和插屏广告。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-advertising-function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void--><!--Device-advertising-function showAd(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ad | [Advertisement](arkts-ads-advertisement-advertisement-i.md) | Yes | 广告对象。 |
| options | [AdDisplayOptions](arkts-ads-advertising-addisplayoptions-i.md) | Yes | 广告展示参数。 |
| context | common.UIAbilityContext | No | UIAbility的上下文环境，不设置从api: [@ohos.app.ability.common](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ js-apis-app-ability-common)中获取。<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid input parameter. Possible causes: 1. Mandatory parameters are left unspecified. |
| 21800004 | Failed to display the ad. |
| 21800001 | System internal error. |

## Examples

For details about how to obtain the context, see [Acquisition of Context](../../application-models/application-context-stage.md#acquisition-of-context).

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

