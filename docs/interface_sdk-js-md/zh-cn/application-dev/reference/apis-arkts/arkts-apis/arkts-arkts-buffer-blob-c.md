# Blob

将数据处理为blob类型。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## arrayBuffer

```TypeScript
arrayBuffer(): Promise<ArrayBuffer>
```

将Blob数据放入ArrayBuffer中返回，使用Promise进行异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## constructor

```TypeScript
constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object)
```

根据传入的数据源和可选配置项创建Blob对象，Blob实例将包含数据源中的内容。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sources | string[] \| ArrayBuffer[] \| TypedArray[] \| DataView[] \| [Blob](arkts-arkts-buffer-blob-c.md)[] | 是 |
| options | Object | 否 |

## slice

```TypeScript
slice(start?: number, end?: number, type?: string): Blob
```

创建并返回一个包含原Blob对象中指定长度数据的新Blob对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 否 |
| end | number | 否 |
| [type](#type) | string | 否 |

**返回值：**

| 类型 |
| --- |
| [Blob](arkts-arkts-buffer-blob-c.md) |

## text

```TypeScript
text(): Promise<string>
```

使用utf8解码并返回字符串。使用Promise进行异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## size

```TypeScript
get size(): number
```

Blob实例的总字节大小。

**类型：** number

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## type

```TypeScript
get type(): string
```

Blob实例的内容类型。

**类型：** string

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
