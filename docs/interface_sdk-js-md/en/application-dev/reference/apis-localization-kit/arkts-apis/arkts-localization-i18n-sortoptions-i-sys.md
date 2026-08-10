# SortOptions (System API)

语言或国家地区排序选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export interface SortOptions--><!--Device-i18n-export interface SortOptions-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## isSuggestedFirst

```TypeScript
isSuggestedFirst?: boolean
```

true表示将推荐语言或国家地区在排序结果中置顶，false表示不将推荐语言或国家地区在排序结果中置顶。默认值：true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SortOptions-isSuggestedFirst?: boolean--><!--Device-SortOptions-isSuggestedFirst?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## isUseLocalName

```TypeScript
isUseLocalName?: boolean
```

true表示使用本地名称进行排序，false表示不使用本地名称进行排序。若调用方法为getLanguageInfoArray，isUseLocalName属性默认值为true。若调用方法为getRegionInfoArray，isUseLocalName属性默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SortOptions-isUseLocalName?: boolean--><!--Device-SortOptions-isUseLocalName?: boolean-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## locale

```TypeScript
locale?: string
```

表示区域ID的字符串，由语言、脚本、国家或地区组成，如"zh-Hans-CN"。默认值：系统当前区域ID。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SortOptions-locale?: string--><!--Device-SortOptions-locale?: string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

