# BreakIterator

The BreakIterator class is used for finding the location of break point in text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export class BreakIterator--><!--Device-i18n-export class BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## current

```TypeScript
current(): int
```

Obtains the position of the break iterator in the text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-current(): int--><!--Device-BreakIterator-current(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Position of the break iterator in the text. |

## first

```TypeScript
first(): int
```

Moves the break iterator to the first line break point, which is always at the beginning of the processed text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-first(): int--><!--Device-BreakIterator-first(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Offset of the first line break point in the processed text. |

## following

```TypeScript
following(offset: int): int
```

Moves the line break iterator to the line break point after the specified position.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-following(offset: int): int--><!--Device-BreakIterator-following(offset: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | Offset of the line break point. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Position of the break iterator in the text after movement. The value -1 is returned if the position of the break iterator is outside of the processed text after movement. |

## getLineBreakText

```TypeScript
getLineBreakText(): string
```

Obtains the text processed by the BreakIterator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-getLineBreakText(): string--><!--Device-BreakIterator-getLineBreakText(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Text being processed by the BreakIterator object. |

## isBoundary

```TypeScript
isBoundary(offset: int): boolean
```

Checks whether the specified position is a line break point.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-isBoundary(offset: int): boolean--><!--Device-BreakIterator-isBoundary(offset: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | Specified position in the text. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the specified position is a line break point. The value "true" indicates that the specified position is a line break point, and the value "false" indicates the opposite. If true is returned, the break iterator is moved to the position specified by offset. Otherwise, the break iterator is moved to the text line break point after the position specified by offset, which is equivalent to calling following. |

## last

```TypeScript
last(): int
```

Moves the break iterator to the last line break point, which is always the next position after the end of the processed text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-last(): int--><!--Device-BreakIterator-last(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Offset of the last line break point in the processed text. |

## next

```TypeScript
next(index?: int): int
```

Moves the break iterator backward by the specified number of line break points.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-next(index?: int): int--><!--Device-BreakIterator-next(index?: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | No | Number of line break points for moving the break iterator. The value is an integer. A positive number means to move the break iterator backward, and a negative number means to move the break iterator forward. The default value is 1. &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Position of the break iterator in the text after movement. The value -1 is returned if the position of the break iterator is outside of the processed text after movement. |

## previous

```TypeScript
previous(): int
```

Moves the break iterator foreward by one line break point.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-previous(): int--><!--Device-BreakIterator-previous(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| int | Position of the break iterator in the text after movement. The value -1 is returned if the position of the break iterator is outside of the processed text after movement. |

## setLineBreakText

```TypeScript
setLineBreakText(text: string): void
```

Sets the text to be processed by the BreakIterator object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BreakIterator-setLineBreakText(text: string): void--><!--Device-BreakIterator-setLineBreakText(text: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Input text. |

