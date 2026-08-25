# Readable

可从中读取数据的流。可读流用于从源（如文件或网络套接字）读取数据。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { stream } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

创建**Readable**对象的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(options: ReadableOptions)
```

创建**Readable**对象的构造函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ReadableOptions](arkts-arkts-stream-readableoptions-i.md) | 是 |

## doInitialize

```TypeScript
doInitialize(callback: Function): void
```

需要由开发者实现此API。在可读流首次调用on时调用此API。使用异步回调返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Function | 是 |

## doRead

```TypeScript
doRead(size: number): void
```

数据读取API，需在子类中实现。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

## isPaused

```TypeScript
isPaused(): boolean
```

检查可读流是否已暂停。流在调用[pause()](#pause)后暂停，在调用[resume()](#resume)后从暂停状态恢复。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## off

```TypeScript
off(event: string, callback?: Callback<emitter.EventData>): void
```

移除通过on注册的事件处理函数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' \| 'data' \| 'end' \| 'error' \| 'readable' \| 'pause' \|
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | 否 |

## on

```TypeScript
on(event: string, callback: Callback<emitter.EventData>): void
```

注册事件处理函数来监听可读流上的不同事件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件包括：'close' \| 'data' \| 'end' \| 'error' \| 'readable' \| 'pause' \|
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;emitter.EventData&gt; | 是 |

## pause

```TypeScript
pause(): Readable
```

暂停流动模式下的可读流。可以使用**isPaused**检查流是否已暂停。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## pipe

```TypeScript
pipe(destination: Writable, options?: Object): Writable
```

将一个可写流附加到可读流上，以实现数据的自动传输。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Writable](arkts-arkts-stream-writable-c.md) | 是 |
| options | Object | 否 |

**返回值：**

| 类型 |
| --- |
| [Writable](arkts-arkts-stream-writable-c.md) |

## push

```TypeScript
push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean
```

将数据推入可读流的缓冲区。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| chunk | Uint8Array \| string \| undefined \| null | 是 | 读取的数据。 API version22开始发生兼容性变更，在API version21及之前的版本其类型为：`Uint8Array \| string \|
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## read

```TypeScript
read(size?: number): string | null
```

从可读流的缓冲区中读取数据，并返回读取的数据。如果没有读取到数据，则返回**null**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 否 |

**返回值：**

| 类型 |
| --- |
| string \| null |

**错误码：**

| 错误码ID |
| --- |
| [10200038](../errorcode-utils.md#10200038-doread接口未实现) |

## resume

```TypeScript
resume(): Readable
```

恢复已显式暂停的可读流。可以使用**isPaused**检查流是否已暂停。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## setEncoding

```TypeScript
setEncoding(encoding?: string): boolean
```

设置可读流的字符编码类型。 当缓冲区有数据时，不允许设置字符编码类型，返回值为**false**。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## unpipe

```TypeScript
unpipe(destination?: Writable): Readable
```

将之前附加到可读流的可写流分离。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Writable](arkts-arkts-stream-writable-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Readable](arkts-arkts-stream-readable-c.md) |

## readable

```TypeScript
get readable(): boolean
```

表示可读流是否处于可读状态。true表示流处于可读状态，false表示流中没有更多数据可供读取。

**类型：** boolean

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableEncoding

```TypeScript
get readableEncoding(): string | null
```

被解码成字符串时所使用的字符编码。默认值是'utf8'，当前版本支持'utf8'、'gb18030'、'gbk'以及'gb2312'。

**类型：** string

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableEnded

```TypeScript
get readableEnded(): boolean
```

表示当前可读流是否已经结束。true表示流已经没有更多数据可读且已结束，false表示流尚未结束，仍有数据可读或等待读取。

**类型：** boolean

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableFlowing

```TypeScript
get readableFlowing(): boolean | null
```

表示当前可读流的状态。true表示流处于流动模式，false表示流处于非流动模式。默认值是true。

**类型：** boolean

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableHighWatermark

```TypeScript
get readableHighWatermark(): number
```

定义缓冲区的最大数据量，单位：字节。默认值为16 * 1024字节。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableLength

```TypeScript
get readableLength(): number
```

表示缓冲区的当前字节数。

**类型：** number

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## readableObjectMode

```TypeScript
get readableObjectMode(): boolean
```

用于指定可读流是否以对象模式工作。true表示流被配置为对象模式，false表示流处于非对象模式。当前版本只支持原始数据（字符串和Uint8Array），返回值为false。

**类型：** boolean

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
