# Base64

将包含 Base64 数据的字符串或 Uint8Array 解码为重新分配的 Uint8Array。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [Base64Helper](arkts-arkts-util-base64helper-c.md)

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

用于创建 **Base64** 对象的构造函数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [constructor](arkts-arkts-util-base64helper-c.md#constructor)

**系统能力：** SystemCapability.Utils.Lang

## decode

```TypeScript
decode(src: Uint8Array | string): Promise<Uint8Array>
```

将输入内容解码为 Uint8Array 对象。该接口使用 promise 返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [decode](arkts-arkts-util-base64helper-c.md#decode)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array \| string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string): Uint8Array
```

将输入内容解码为 Uint8Array 对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [decodeSync](arkts-arkts-util-base64helper-c.md#decodesync)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array \| string | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## encode

```TypeScript
encode(src: Uint8Array): Promise<Uint8Array>
```

将输入内容编码为 Uint8Array 对象。该接口使用 promise 返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [encode](arkts-arkts-util-base64helper-c.md#encode)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

## encodeSync

```TypeScript
encodeSync(src: Uint8Array): Uint8Array
```

对输入的 Uint8Array 字节数组进行 Base64 编码，并返回编码后的 Uint8Array。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [encodeSync](arkts-arkts-util-base64helper-c.md#encodesync)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## encodeToString

```TypeScript
encodeToString(src: Uint8Array): Promise<string>
```

将输入内容编码为字符串。该接口使用 promise 返回结果。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [encodeToString](arkts-arkts-util-base64helper-c.md#encodetostring)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array): string
```

对输入的 Uint8Array 字节数组进行 Base64 编码，并返回编码后的字符串。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [encodeToStringSync](arkts-arkts-util-base64helper-c.md#encodetostringsync)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| string |
