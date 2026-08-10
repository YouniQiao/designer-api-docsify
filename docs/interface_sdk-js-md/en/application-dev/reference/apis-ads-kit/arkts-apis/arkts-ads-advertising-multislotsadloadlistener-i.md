# MultiSlotsAdLoadListener

多广告位广告请求回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-advertising-export interface MultiSlotsAdLoadListener--><!--Device-advertising-export interface MultiSlotsAdLoadListener-End-->

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## onAdLoadFailure

```TypeScript
onAdLoadFailure(errorCode: number, errorMsg: string): void
```

广告请求失败回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MultiSlotsAdLoadListener-onAdLoadFailure(errorCode: number, errorMsg: string): void--><!--Device-MultiSlotsAdLoadListener-onAdLoadFailure(errorCode: number, errorMsg: string): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errorCode | number | Yes | 广告请求失败的错误码。 |
| errorMsg | string | Yes | 广告请求失败的错误信息。 |

## Examples

```TypeScript
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
  },
  onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
  }
}
```

## onAdLoadSuccess

```TypeScript
onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void
```

多广告位广告请求成功后回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MultiSlotsAdLoadListener-onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void--><!--Device-MultiSlotsAdLoadListener-onAdLoadSuccess(adsMap: Map<string, Array<Advertisement>>): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| adsMap | Map&lt;string, Array&lt;Advertisement&gt;&gt; | Yes | 广告数据，是以广告位ID为键，存储请求到的广告内容的映射集合。 |

## Examples

```TypeScript
import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const multiSlotsAdLoadListener: advertising.MultiSlotsAdLoadListener = {
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
  },
  onAdLoadSuccess: (adsMap: Map<string, Array<advertising.Advertisement>>) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
  }
}
```

