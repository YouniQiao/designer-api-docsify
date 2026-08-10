# getInstance

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getInstance

```TypeScript
export function getInstance(locale?:string): IndexUtil
```

创建并返回IndexUtil对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getInstance(locale?:string): IndexUtil--><!--Device-i18n-export function getInstance(locale?:string): IndexUtil-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | No | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 &lt;br&gt;默认值：系统当前区域ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IndexUtil](arkts-localization-i18n-indexutil-c.md) | 根据区域ID创建的IndexUtil对象。 |

