# IndexUtil

提供索引相关的能力，包括区域索引列表和文本索引值获取。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class IndexUtil--><!--Device-i18n-export class IndexUtil-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## addLocale

```TypeScript
addLocale(locale: string): void
```

在当前区域的索引列表中，添加新区域的索引列表，形成复合列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-addLocale(locale: string): void--><!--Device-IndexUtil-addLocale(locale: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组 成。 |

## getIndex

```TypeScript
getIndex(text: string): string
```

获取输入文本对应的索引值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-getIndex(text: string): string--><!--Device-IndexUtil-getIndex(text: string): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入文本。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 输入文本对应的索引值。无合适索引时返回空字符串。 |

## getIndexList

```TypeScript
getIndexList(): Array<string>
```

获取当前区域的索引列表。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-IndexUtil-getIndexList(): Array<string>--><!--Device-IndexUtil-getIndexList(): Array<string>-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 当前区域的索引列表。第一个元素和最后一个元素为“...”。 |

