# BreakIterator

提供文本换行相关的能力，包括可换行点的获取、移动和识别等。

**起始版本：** 8

<!--Device-i18n-export class BreakIterator--><!--Device-i18n-export class BreakIterator-End-->

**系统能力：** SystemCapability.Global.I18n

## current

```TypeScript
current(): number
```

获取换行迭代器在当前处理文本中的位置。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-current(): int--><!--Device-BreakIterator-current(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let currentPos: number = iterator.current(); // currentPos = 0
```

## first

```TypeScript
first(): number
```

将换行迭代器移动到第一个可换行点。第一个可换行点总是在被处理文本的起始位置。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-first(): int--><!--Device-BreakIterator-first(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let firstPos: number = iterator.first(); // firstPos = 0
```

## following

```TypeScript
following(offset: number): number
```

将换行迭代器移动到指定位置后面一个可换行点。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-following(offset: int): int--><!--Device-BreakIterator-following(offset: int): int-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

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

获取BreakIterator对象当前处理的文本。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-getLineBreakText(): string--><!--Device-BreakIterator-getLineBreakText(): string-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let breakText: string = iterator.getLineBreakText(); // breakText = 'Apple is my favorite fruit.'
```

## isBoundary

```TypeScript
isBoundary(offset: number): boolean
```

判断指定位置是否为可换行点。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-isBoundary(offset: int): boolean--><!--Device-BreakIterator-isBoundary(offset: int): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let isBoundary: boolean = iterator.isBoundary(0); // isBoundary = true;
isBoundary = iterator.isBoundary(5); // isBoundary = false;
```

## last

```TypeScript
last(): number
```

将换行迭代器移动到最后一个可换行点。最后一个可换行点总是在被处理文本末尾的下一个位置。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-last(): int--><!--Device-BreakIterator-last(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let lastPos: number = iterator.last(); // lastPos = 27
```

## next

```TypeScript
next(index?: number): number
```

将换行迭代器向后移动index个可换行点。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-next(index?: int): int--><!--Device-BreakIterator-next(index?: int): int-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(); // pos = 6
pos = iterator.next(10); // pos = -1
```

## previous

```TypeScript
previous(): number
```

将换行迭代器向前移动一个可换行点。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-previous(): int--><!--Device-BreakIterator-previous(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## 示例

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

设置BreakIterator对象要处理的文本。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-BreakIterator-setLineBreakText(text: string): void--><!--Device-BreakIterator-setLineBreakText(text: string): void-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.'); // 设置处理文本
```
