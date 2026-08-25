# Unicode

提供字符属性相关的能力，包括判断字符是否为空格、数字和字母等。

**起始版本：** 9

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## detectEncoding

```TypeScript
static detectEncoding(bytes: Uint8Array): EncodingInfo
```

识别输入字节流的编码信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bytes | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [EncodingInfo](arkts-localization-i18n-encodinginfo-i.md) |

## getType

```TypeScript
static getType(ch: string): string
```

获取输入的字符的一般类别值。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## isDigit

```TypeScript
static isDigit(ch: string): boolean
```

判断输入的字符是否是数字。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isIdeograph

```TypeScript
static isIdeograph(ch: string): boolean
```

判断输入的字符是否是表意文字。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLetter

```TypeScript
static isLetter(ch: string): boolean
```

判断输入的字符是否是字母。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isLowerCase

```TypeScript
static isLowerCase(ch: string): boolean
```

判断输入的字符是否是小写字母。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isRTL

```TypeScript
static isRTL(ch: string): boolean
```

判断输入的字符是否是从右到左语言的字符。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSpaceChar

```TypeScript
static isSpaceChar(ch: string): boolean
```

判断输入的字符是否是空格符。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUpperCase

```TypeScript
static isUpperCase(ch: string): boolean
```

判断输入的字符是否是大写字母。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWhitespace

```TypeScript
static isWhitespace(ch: string): boolean
```

判断输入的字符是否是空白符。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
