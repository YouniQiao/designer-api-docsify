# BreakIterator

提供文本换行相关的能力，包括可换行点的获取、移动和识别等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class BreakIterator--><!--Device-i18n-export class BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## current

```TypeScript
current(): int
```

获取换行迭代器在当前处理文本中的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-current(): int--><!--Device-BreakIterator-current(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 获取换行迭代器在当前处理的文本中的位置。 |

## first

```TypeScript
first(): int
```

将换行迭代器移动到第一个可换行点。第一个可换行点总是在被处理文本的起始位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-first(): int--><!--Device-BreakIterator-first(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 被处理文本的第一个可换行点的偏移量。 |

## following

```TypeScript
following(offset: int): int
```

将换行迭代器移动到指定位置后面一个可换行点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-following(offset: int): int--><!--Device-BreakIterator-following(offset: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | 将换行迭代器移动到文本指定位置的后面一个可换行点。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 换行迭代器移动后的位置。若offset所指定位置的下一个可换行点超出了文本的范围，则返回-1。 |

## getLineBreakText

```TypeScript
getLineBreakText(): string
```

获取BreakIterator对象当前处理的文本。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-getLineBreakText(): string--><!--Device-BreakIterator-getLineBreakText(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | BreakIterator对象正在处理的文本。 |

## isBoundary

```TypeScript
isBoundary(offset: int): boolean
```

判断指定位置是否为可换行点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-isBoundary(offset: int): boolean--><!--Device-BreakIterator-isBoundary(offset: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | 文本指定位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示offset指定的文本位置是一个可换行点，false表示offset指定的文本位置不是一个可换行点。 &lt;br&gt;返回true时，会将换行迭代器移动到offset指定的位置，否则相当于调用following。 |

## last

```TypeScript
last(): int
```

将换行迭代器移动到最后一个可换行点。最后一个可换行点总是在被处理文本末尾的下一个位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-last(): int--><!--Device-BreakIterator-last(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 被处理文本的最后一个可换行点的偏移量。 |

## next

```TypeScript
next(index?: int): int
```

将换行迭代器向后移动index个可换行点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-next(index?: int): int--><!--Device-BreakIterator-next(index?: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | 换行迭代器将要移动的可换行点数，取值为整数。 &lt;br&gt;正数表示向后移动index个可换行点，负数表示向前移动index个可换行点。 &lt;br&gt;默认值：1。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 移动index个可换行点后，当前换行迭代器在文本中的位置。 &lt;br&gt;若移动index个可换行点后超出了所处理的文本的长度范围，返回-1。 |

## previous

```TypeScript
previous(): int
```

将换行迭代器向前移动一个可换行点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-previous(): int--><!--Device-BreakIterator-previous(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | 移动到前一个可换行点后，当前换行迭代器在文本中的位置。 &lt;br&gt;若移动后超出了所处理的文本的长度范围，返回-1。 |

## setLineBreakText

```TypeScript
setLineBreakText(text: string): void
```

设置BreakIterator对象要处理的文本。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-setLineBreakText(text: string): void--><!--Device-BreakIterator-setLineBreakText(text: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 输入文本。 |

