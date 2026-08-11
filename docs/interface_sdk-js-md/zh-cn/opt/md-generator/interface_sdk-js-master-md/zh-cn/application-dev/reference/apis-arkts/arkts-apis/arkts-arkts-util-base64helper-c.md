# Base64Helper

提供 Base64 和 Base64URL 的编解码。Base64 编码表包含 64 个字符，分别为大写字母（A-Z）、小写字母（a-z）、数字（0-9）以及特殊字符加号（+）和斜杠（/）。编码时，原始数据按三个字节一组进行划分，每组包含一个 6 位的数字。然后使用 Base64编码表中对应的字符来表示这些数字。如果最后一组只包含一个或两个字节，则使用等号（=）进行填充。Base64URL 编码表包含64 个字符，分别为大写字母（A-Z）、小写字母（a-z）、数字（0-9）以及特殊字符加号（+）和斜杠（/）。Base64URL 编码结果不包含等号（=）。

**起始版本：** 9

<!--Device-util-class Base64Helper--><!--Device-util-class Base64Helper-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor()
```

用于创建 **Base64Helper** 实例的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-constructor()--><!--Device-Base64Helper-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## decode

```TypeScript
decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>
```

将输入内容解码为 Uint8Array 对象。该接口使用 promise 返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array \| string | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Uint8Array&gt; |

## decodeSync

```TypeScript
decodeSync(src: Uint8Array | string, options?: Type): Uint8Array
```

将字符串解码为 Uint8Array 对象。该接口同步返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array--><!--Device-Base64Helper-decodeSync(src: Uint8Array | string, options?: Type): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array \| string | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## encode

```TypeScript
encode(src: Uint8Array, options?: Type): Promise<Uint8Array>
```

将输入内容编码为 Uint8Array 对象。该接口使用 promise 返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>--><!--Device-Base64Helper-encode(src: Uint8Array, options?: Type): Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Uint8Array&gt; |

## encodeSync

```TypeScript
encodeSync(src: Uint8Array, options?: Type): Uint8Array
```

将输入内容编码为 Uint8Array 对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array--><!--Device-Base64Helper-encodeSync(src: Uint8Array, options?: Type): Uint8Array-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

## encodeToString

```TypeScript
encodeToString(src: Uint8Array, options?: Type): Promise<string>
```

将输入内容编码为字符串。该接口使用 promise 返回结果。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>--><!--Device-Base64Helper-encodeToString(src: Uint8Array, options?: Type): Promise<string>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

## encodeToStringSync

```TypeScript
encodeToStringSync(src: Uint8Array, options?: Type): string
```

对输入的 Uint8Array 字节数组进行 Base64 编码，并返回字符串。该方法支持多种编码格式，包括标准 Base64 编码、符合MIME 规范的 Base64 编码（带换行）以及 URL 安全的 Base64 编码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string--><!--Device-Base64Helper-encodeToStringSync(src: Uint8Array, options?: Type): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | Uint8Array | 是 |
| options | [Type](arkts-arkts-util-type-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |
