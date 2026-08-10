# getLineInstance

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getLineInstance

```TypeScript
export function getLineInstance(locale: string): BreakIterator
```

获取用于定位文本可换行点的BreakIterator对象。该对象内部维护一个换行迭代器，可以用于访问各个可换行点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-i18n-export function getLineInstance(locale: string): BreakIterator--><!--Device-i18n-export function getLineInstance(locale: string): BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成。 &lt;br&gt;生成的[BreakIterator](arkts-localization-i18n-breakiterator-c.md)将按照指定区域的规则计算可换行点的位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BreakIterator](arkts-localization-i18n-breakiterator-c.md) | 可换行点处理器。 |

