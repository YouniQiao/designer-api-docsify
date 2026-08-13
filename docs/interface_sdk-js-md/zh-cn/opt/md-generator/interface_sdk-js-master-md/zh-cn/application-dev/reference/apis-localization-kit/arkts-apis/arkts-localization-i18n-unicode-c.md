# Unicode

提供字符属性相关的能力，包括判断字符是否为空格、数字和字母等。

**起始版本：** 23

**废弃版本：** -1

<!--Device-i18n-export class Unicode--><!--Device-i18n-export class Unicode-End-->

**系统能力：** SystemCapability.Global.I18n

## detectEncoding

```TypeScript
static detectEncoding(bytes: Uint8Array): EncodingInfo
```

识别输入字节流的编码信息。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static detectEncoding(bytes: Uint8Array): EncodingInfo--><!--Device-Unicode-static detectEncoding(bytes: Uint8Array): EncodingInfo-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bytes | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [EncodingInfo](arkts-localization-i18n-encodinginfo-i.md) |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let uint8Array = new Uint8Array([0xEF, 0xBB, 0xBF, 0xE4, 0xB8, 0xAD]);
let info = i18n.Unicode.detectEncoding(uint8Array); // info.encodingName = 'UTF-8', info.confidence = 100
```

## getType

```TypeScript
static getType(ch: string): string
```

获取输入的字符的一般类别值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static getType(ch: string): string--><!--Device-Unicode-static getType(ch: string): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
```

## isDigit

```TypeScript
static isDigit(ch: string): boolean
```

判断输入的字符是否是数字。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isDigit(ch: string): boolean--><!--Device-Unicode-static isDigit(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isDigit: boolean = i18n.Unicode.isDigit('1'); // isDigit = true
```

## isIdeograph

```TypeScript
static isIdeograph(ch: string): boolean
```

判断输入的字符是否是表意文字。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isIdeograph(ch: string): boolean--><!--Device-Unicode-static isIdeograph(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isIdeograph: boolean = i18n.Unicode.isIdeograph('a'); // isIdeograph = false
```

## isLetter

```TypeScript
static isLetter(ch: string): boolean
```

判断输入的字符是否是字母。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isLetter(ch: string): boolean--><!--Device-Unicode-static isLetter(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLetter: boolean = i18n.Unicode.isLetter('a'); // isLetter = true
```

## isLowerCase

```TypeScript
static isLowerCase(ch: string): boolean
```

判断输入的字符是否是小写字母。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isLowerCase(ch: string): boolean--><!--Device-Unicode-static isLowerCase(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isLowercase: boolean = i18n.Unicode.isLowerCase('a'); // isLowercase = true
```

## isRTL

```TypeScript
static isRTL(ch: string): boolean
```

判断输入的字符是否是从右到左语言的字符。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isRTL(ch: string): boolean--><!--Device-Unicode-static isRTL(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isRtl: boolean = i18n.Unicode.isRTL('a'); // isRtl = false
```

## isSpaceChar

```TypeScript
static isSpaceChar(ch: string): boolean
```

判断输入的字符是否是空格符。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isSpaceChar(ch: string): boolean--><!--Device-Unicode-static isSpaceChar(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isSpacechar: boolean = i18n.Unicode.isSpaceChar('a'); // isSpacechar = false
```

## isUpperCase

```TypeScript
static isUpperCase(ch: string): boolean
```

判断输入的字符是否是大写字母。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isUpperCase(ch: string): boolean--><!--Device-Unicode-static isUpperCase(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isUppercase: boolean = i18n.Unicode.isUpperCase('a'); // isUppercase = false
```

## isWhitespace

```TypeScript
static isWhitespace(ch: string): boolean
```

判断输入的字符是否是空白符。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Unicode-static isWhitespace(ch: string): boolean--><!--Device-Unicode-static isWhitespace(ch: string): boolean-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false
```
