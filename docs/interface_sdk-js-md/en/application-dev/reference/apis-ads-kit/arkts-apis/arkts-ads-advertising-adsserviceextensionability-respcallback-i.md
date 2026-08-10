# RespCallback

广告请求回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-export interface RespCallback--><!--Device-unnamed-export interface RespCallback-End-->

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { RespCallback } from 'kits/@kit.AdsKit';
```

## [[Call]]

```TypeScript
(respData: Map<string, Array<advertising.Advertisement>>): void
```

广告请求回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-RespCallback-(respData: Map<string, Array<advertising.Advertisement>>): void--><!--Device-RespCallback-(respData: Map<string, Array<advertising.Advertisement>>): void-End-->

**System capability:** SystemCapability.Advertising.Ads

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| respData | Map&lt;string, Array&lt;advertising.Advertisement&gt;&gt; | Yes | 广告请求回调数据，是以广告位ID为键， 存储请求到的广告内容的映射集合。 |

