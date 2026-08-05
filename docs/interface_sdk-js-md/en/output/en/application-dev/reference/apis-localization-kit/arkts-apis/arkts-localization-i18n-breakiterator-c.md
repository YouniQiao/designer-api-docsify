# BreakIterator

Provides text line breaking capabilities, such as obtaining, moving, and identifying break points.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-i18n-export class BreakIterator--><!--Device-i18n-export class BreakIterator-End-->

**System capability:** SystemCapability.Global.I18n

## current

ArkTS-Dyn:
```TypeScript
current(): number
```

ArkTS-Sta:
```TypeScript
current(): int
```

Obtains the position of the break iterator in the text.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-current(): int--><!--Device-BreakIterator-current(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Position of the break iterator in the text. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let currentPos: number = iterator.current(); // currentPos = 0
```

## first

ArkTS-Dyn:
```TypeScript
first(): number
```

ArkTS-Sta:
```TypeScript
first(): int
```

Moves the break iterator to the first line break point, which is always at the beginning of the processed text.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-first(): int--><!--Device-BreakIterator-first(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Offset of the first line break point in the processed text. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let firstPos: number = iterator.first(); // firstPos = 0
```

## following

ArkTS-Dyn:
```TypeScript
following(offset: number): number
```

ArkTS-Sta:
```TypeScript
following(offset: int): int
```

Moves the line break iterator to the line break point after the specified position.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-following(offset: int): int--><!--Device-BreakIterator-following(offset: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Offset of the line break point. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Position of the break iterator in the text after movement. The value **-1** is returned if the |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.following(0); // pos = 6
pos = iterator.following(100); // pos = -1
pos = iterator.current(); // pos = 27
```

## getLineBreakText

```TypeScript
getLineBreakText(): string
```

Obtains the text processed by the **BreakIterator** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-getLineBreakText(): string--><!--Device-BreakIterator-getLineBreakText(): string-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| string | Text being processed by the **BreakIterator** object. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let breakText: string = iterator.getLineBreakText(); // breakText = 'Apple is my favorite fruit.'
```

## isBoundary

ArkTS-Dyn:
```TypeScript
isBoundary(offset: number): boolean
```

ArkTS-Sta:
```TypeScript
isBoundary(offset: int): boolean
```

Checks whether the specified position is a line break point.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-isBoundary(offset: int): boolean--><!--Device-BreakIterator-isBoundary(offset: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Specified position in the text. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the specified position is a line break point. The value **true** indicates that the |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let isBoundary: boolean = iterator.isBoundary(0); // isBoundary = true;
isBoundary = iterator.isBoundary(5); // isBoundary = false;
```

## last

ArkTS-Dyn:
```TypeScript
last(): number
```

ArkTS-Sta:
```TypeScript
last(): int
```

Moves the break iterator to the last line break point, which is always the next position after the end of the processed text.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-last(): int--><!--Device-BreakIterator-last(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Offset of the last line break point in the processed text. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let lastPos: number = iterator.last(); // lastPos = 27
```

## next

ArkTS-Dyn:
```TypeScript
next(index?: number): number
```

ArkTS-Sta:
```TypeScript
next(index?: int): int
```

Moves the break iterator backward by the specified number of line break points.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-next(index?: int): int--><!--Device-BreakIterator-next(index?: int): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Number of line break points for moving the break iterator. The value is an integer.A positive number means to move the break iterator backward, and a negative number means to move the break iterator forward.The default value is **1**. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Position of the break iterator in the text after movement. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(); // pos = 6
pos = iterator.next(10); // pos = -1
```

## previous

ArkTS-Dyn:
```TypeScript
previous(): number
```

ArkTS-Sta:
```TypeScript
previous(): int
```

Moves the break iterator foreward by one line break point.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-previous(): int--><!--Device-BreakIterator-previous(): int-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Position of the break iterator in the text after movement. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(3); // pos = 12
pos = iterator.previous(); // pos = 9
```

## setLineBreakText

```TypeScript
setLineBreakText(text: string): void
```

Sets the text to be processed by the **BreakIterator** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BreakIterator-setLineBreakText(text: string): void--><!--Device-BreakIterator-setLineBreakText(text: string): void-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Input text. |

**Example**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.'); // Set the text to be processed.
```

