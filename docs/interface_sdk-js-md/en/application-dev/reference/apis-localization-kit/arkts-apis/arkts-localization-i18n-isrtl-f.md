# isRTL

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## isRTL

```TypeScript
export function isRTL(locale: string): boolean
```

判断语言是否为镜像语言。在镜像语言下，UI界面需要[镜像显示](../../../internationalization/i18n-ui-design.md#界面镜像)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function isRTL(locale: string): boolean--><!--Device-i18n-export function isRTL(locale: string): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示该语言是镜像语言，false表示该语言不是镜像语言。 |

