# Advertisement

本模块为请求的广告内容。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-export interface Advertisement--><!--Device-unnamed-export interface Advertisement-End-->

**System capability:** SystemCapability.Advertising.Ads

## [key:string]

```TypeScript
[key:string]: Object
```

自定义参数。

&lt;!--RP1--&gt;&lt;!--RP1End--&gt;

**Type:** Object

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-[key:string]: Object--><!--Device-Advertisement-[key:string]: Object-End-->

**System capability:** SystemCapability.Advertising.Ads

## adType

```TypeScript
adType: number
```

广告类型。

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

<!--Device-Advertisement-adType: number--><!--Device-Advertisement-adType: number-End-->

**System capability:** SystemCapability.Advertising.Ads

## clicked

```TypeScript
clicked: boolean
```

广告是否被点击。

- true：被点击。  
- false：未被点击。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-clicked: boolean--><!--Device-Advertisement-clicked: boolean-End-->

**System capability:** SystemCapability.Advertising.Ads

## rewardVerifyConfig

```TypeScript
rewardVerifyConfig: Map<string, string>
```

服务器验证参数。

{

customData: "test",

userId: "12345"

}

**Type:** Map&lt;string, string&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-rewardVerifyConfig: Map<string, string>--><!--Device-Advertisement-rewardVerifyConfig: Map<string, string>-End-->

**System capability:** SystemCapability.Advertising.Ads

## rewarded

```TypeScript
rewarded: boolean
```

广告是否获得奖励。

- true：获得奖励。  
- false：没有获得奖励。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-rewarded: boolean--><!--Device-Advertisement-rewarded: boolean-End-->

**System capability:** SystemCapability.Advertising.Ads

## shown

```TypeScript
shown: boolean
```

广告是否展示。

- true：展示。  
- false：未展示。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-shown: boolean--><!--Device-Advertisement-shown: boolean-End-->

**System capability:** SystemCapability.Advertising.Ads

## uniqueId

```TypeScript
uniqueId: string
```

广告唯一标识。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Advertisement-uniqueId: string--><!--Device-Advertisement-uniqueId: string-End-->

**System capability:** SystemCapability.Advertising.Ads

