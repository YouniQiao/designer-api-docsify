# AdRequestParams

广告请求参数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-advertising-export interface AdRequestParams--><!--Device-advertising-export interface AdRequestParams-End-->

**System capability:** SystemCapability.Advertising.Ads

## Modules to Import

```TypeScript
import { advertising } from 'kits/@kit.AdsKit';
```

## [key: string]

```TypeScript
[key: string]: number | boolean | string | undefined
```

自定义参数。

&lt;!--RP2--&gt;&lt;!--RP2End--&gt;

**Type:** number \| boolean \| string \| undefined

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-[key: string]: number | boolean | string | undefined--><!--Device-AdRequestParams-[key: string]: number | boolean | string | undefined-End-->

**System capability:** SystemCapability.Advertising.Ads

## adCount

```TypeScript
adCount?: number
```

请求的广告数量。不填以业务逻辑为准。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adCount?: number--><!--Device-AdRequestParams-adCount?: number-End-->

**System capability:** SystemCapability.Advertising.Ads

## adHeight

```TypeScript
adHeight?: number
```

请求广告时期望的创意高度，单位vp（横幅广告必填）。不填以业务逻辑为准。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adHeight?: number--><!--Device-AdRequestParams-adHeight?: number-End-->

**System capability:** SystemCapability.Advertising.Ads

## adId

```TypeScript
adId: string
```

广告位ID。

说明：getAdRequestBody接口可以不传该参数。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adId: string--><!--Device-AdRequestParams-adId: string-End-->

**System capability:** SystemCapability.Advertising.Ads

## adSearchKeyword

```TypeScript
adSearchKeyword?: string
```

广告关键字。不填默认""。

说明：暂不支持使用。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adSearchKeyword?: string--><!--Device-AdRequestParams-adSearchKeyword?: string-End-->

**System capability:** SystemCapability.Advertising.Ads

## adType

```TypeScript
adType?: number
```

请求的广告类型。

- 1：开屏广告。  
- 3：原生广告。  
- 7：激励广告。  
- 8：横幅广告。  
- 12：插屏广告。  
- 60：贴片广告。

不填默认为原生广告类型。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adType?: number--><!--Device-AdRequestParams-adType?: number-End-->

**System capability:** SystemCapability.Advertising.Ads

## adWidth

```TypeScript
adWidth?: number
```

请求广告时期望的创意宽度，单位vp（横幅广告必填）。不填以业务逻辑为准。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdRequestParams-adWidth?: number--><!--Device-AdRequestParams-adWidth?: number-End-->

**System capability:** SystemCapability.Advertising.Ads

