# GZip

Gzip相关接口。

**起始版本：** 12

**系统能力：** SystemCapability.BundleManager.Zlib

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## gzbuffer

```TypeScript
gzbuffer(size: number): Promise<number>
```

为当前库函数设置内部缓冲区尺寸。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzclearerr

```TypeScript
gzclearerr(): Promise<void>
```

清除文件的错误和文件结束标志。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## gzclose

```TypeScript
gzclose(): Promise<ReturnStatus>
```

清除文件的所有挂起输出，如有必要，关闭文件和释放（解）压缩状态。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800006](../../apis-ability-kit/errorcode-zlib.md#17800006-内存分配失败错误) |

## gzcloser

```TypeScript
gzcloser(): Promise<ReturnStatus>
```

与gzclose()功能相同，仅适用于读取时。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## gzclosew

```TypeScript
gzclosew(): Promise<ReturnStatus>
```

与gzclose()功能相同，仅适用于写入或追加时。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800006](../../apis-ability-kit/errorcode-zlib.md#17800006-内存分配失败错误) |

## gzdirect

```TypeScript
gzdirect(): Promise<number>
```

检查指定的gzip文件句柄文件是否直接访问原始未压缩数据，重新分配缓冲区。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## gzdopen

```TypeScript
gzdopen(fd: number, mode: string): Promise<void>
```

将gzFile与文件描述符fd相关联，打开文件，用于进行读取并解压缩，或者压缩并写入。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800002](../../apis-ability-kit/errorcode-zlib.md#17800002-传入的文件或访问模式错误) |

## gzeof

```TypeScript
gzeof(): Promise<number>
```

检查gzip压缩文件的读取位置是否已到达文件的末尾。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## gzerror

```TypeScript
gzerror(): Promise<GzErrorOutputInfo>
```

文件上发生的最后一个错误的错误消息。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[GzErrorOutputInfo](arkts-basicservices-zlib-gzerroroutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## gzflush

```TypeScript
gzflush(flush: CompressFlushMode): Promise<ReturnStatus>
```

将所有挂起的输出刷新到文件中。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flush | [CompressFlushMode](arkts-basicservices-zlib-compressflushmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## gzfread

```TypeScript
gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>
```

从gzip压缩文件中解压缩并读取数据。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| size | number | 是 |
| nitems | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzfwrite

```TypeScript
gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>
```

将大小为size，数量为nitems的数据块从buf压缩并写入文件。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| size | number | 是 |
| nitems | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzgetc

```TypeScript
gzgetc(): Promise<number>
```

从文件中读取并解压缩一个字节。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzgets

```TypeScript
gzgets(buf: ArrayBuffer): Promise<string>
```

从文件中读取字节并将其解压缩到buf中，直到读取len-1字符，或者直到读取换行符并将其传输到buf，或者遇到文件结束条件。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzoffset

```TypeScript
gzoffset(): Promise<number>
```

返回文件的当前压缩（实际）读或写偏移量。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzopen

```TypeScript
gzopen(path: string, mode: string): Promise<void>
```

打开位于指定路径的gzip(.gz)文件，用于进行读取并解压缩，或者压缩并写入。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800002](../../apis-ability-kit/errorcode-zlib.md#17800002-传入的文件或访问模式错误) |

## gzprintf

```TypeScript
gzprintf(format: string, ...args: Array<string | number>): Promise<number>
```

在字符串格式的控制下，将参数转换和格式化后，压缩并写入文件，如fprintf中所示。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzputc

```TypeScript
gzputc(ch: number): Promise<number>
```

将转换为无符号字符的c压缩并写入文件。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ch | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzputs

```TypeScript
gzputs(str: string): Promise<number>
```

压缩给定的以null结尾的字符串并将其写入文件，不包括终止的null字符。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| str | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzread

```TypeScript
gzread(buf: ArrayBuffer): Promise<number>
```

从文件中读取最多len个未压缩字节并将其解压缩到buf中。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzrewind

```TypeScript
gzrewind(): Promise<ReturnStatus>
```

将文件指针重新定位到文件的开头，此功能仅用于读取。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzseek

```TypeScript
gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>
```

将起始位置设置为相对于文件中下一个gzread或gzwrite的偏移位置。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| whence | [OffsetReferencePoint](arkts-basicservices-zlib-offsetreferencepoint-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzsetparams

```TypeScript
gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

动态更新文件的压缩级别和压缩策略。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | 是 |
| strategy | [CompressStrategy](arkts-basicservices-zlib-compressstrategy-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## gztell

```TypeScript
gztell(): Promise<number>
```

返回文件中下一个gzread或gzwrite的起始位置。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzungetc

```TypeScript
gzungetc(c: number): Promise<number>
```

将c推回到流中，以便在下次读取文件时将作为第一个字符读取。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| c | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |

## gzwrite

```TypeScript
gzwrite(buf: ArrayBuffer, len: number): Promise<number>
```

将buf中的len长度的未压缩字节进行压缩并将其写入文件。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| len | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-内部结构错误) |
