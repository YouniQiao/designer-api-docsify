# TextDecoder

提供将字节数组解码为字符串的 API。支持多种格式，包括 UTF-8、UTF-16LE、UTF-16BE、ISO-8859 和 Windows-1251。

**起始版本：** 7

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

用于创建 **TextDecoder** 对象的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })
```

用于创建 **TextDecoder** 对象的构造函数。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [create](#create)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [encoding](#encoding) | string | 否 |
| options | { fatal?: boolean; ignoreBOM?: boolean } | 否 |

## create

```TypeScript
static create(encoding?: string, options?: TextDecoderOptions): TextDecoder
```

创建一个 **TextDecoder** 对象。提供与已弃用的带参构造函数相同的功能。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [encoding](#encoding) | string | 否 |
| options | [TextDecoderOptions](arkts-arkts-util-textdecoderoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextDecoder](arkts-arkts-util-textdecoder-c.md) |

## decode

```TypeScript
decode(input: Uint8Array, options?: { stream?: false }): string
```

将输入内容解码为字符串。

> **说明：**&gt;
> 该接口会正常解析值为\0的字节，将其转换为Unicode字符\u0000（空字符），不会导致解码中断或错误。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [decodeToString](#decodetostring)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | Uint8Array | 是 |
| options | { stream?: false } | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## decodeToString

```TypeScript
decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string
```

将输入内容解码为字符串。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | Uint8Array | 是 |
| options | [DecodeToStringOptions](arkts-arkts-util-decodetostringoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## decodeWithStream

```TypeScript
decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string
```

将输入内容解码为字符串。如果 **input** 是空数组，则返回 **undefined**。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [decodeToString](#decodetostring)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| input | Uint8Array | 是 |
| options | [DecodeWithStreamOptions](arkts-arkts-util-decodewithstreamoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## encoding

```TypeScript
readonly encoding: string
```

编码格式。  
-&nbsp;支持格式：utf-8、ibm866、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、 iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、 windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、 x-mac-cyrillic、gbk、gb18030、big5、euc-jp、iso-2022-jp、shift_jis、euc-kr、utf-16be、utf-16le、gb2312、iso-8859-1。

**类型：** string

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## fatal

```TypeScript
readonly fatal: boolean
```

是否显示致命错误，true表示显示，false表示不显示。

**类型：** boolean

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## ignoreBOM

```TypeScript
readonly ignoreBOM = false
```

是否忽略BOM（byte order marker）标记，true表示忽略BOM标记，false表示解码结果包含BOM标记，默认值为false。

**类型：** false

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
