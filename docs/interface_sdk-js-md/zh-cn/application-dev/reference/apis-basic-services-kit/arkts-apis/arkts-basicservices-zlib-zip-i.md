# Zip

压缩解压缩对象实例，支持以zlib、deflate、gzip格式对数据进行压缩与解压。

**起始版本：** 12

**系统能力：** SystemCapability.BundleManager.Zlib

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## compress

```TypeScript
compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>
```

将源缓冲区压缩到目标缓冲区。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dest | ArrayBuffer | 是 |
| source | ArrayBuffer | 是 |
| sourceLen | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## compress2

```TypeScript
compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number,): Promise<ZipOutputInfo>
```

将源缓冲区压缩到目标缓冲区。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dest | ArrayBuffer | 是 |
| source | ArrayBuffer | 是 |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | 是 |
| sourceLen | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## compressBound

```TypeScript
compressBound(sourceLen: number): Promise<number>
```

计算返回压缩大小的上限。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceLen | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## deflate

```TypeScript
deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>
```

压缩数据。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
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
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## deflateBound

```TypeScript
deflateBound(strm: ZStream, sourceLength: number): Promise<number>
```

计算压缩大小的上限。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| [sourceLength](arkts-basicservices-zlib-decompressionoutputinfo-i.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## deflateCopy

```TypeScript
deflateCopy(source: Zip): Promise<ReturnStatus>
```

复制压缩流。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [Zip](arkts-basicservices-zlib-zip-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateEnd

```TypeScript
deflateEnd(strm: ZStream): Promise<ReturnStatus>
```

解压流的所有动态分配的数据结构都被释放。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateGetDictionary

```TypeScript
deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>
```

获取当前压缩流中使用的解压缩字典内容及其长度。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| dictionary | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DictionaryOutputInfo](arkts-basicservices-zlib-dictionaryoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateInit

```TypeScript
deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>
```

初始化压缩流并设置指定压缩级别。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateInit2

```TypeScript
deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number,
        memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

初始化压缩流并设置压缩级别、压缩方法、窗口大小、内存级别和压缩策略。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | 是 |
| method | [CompressMethod](arkts-basicservices-zlib-compressmethod-e.md) | 是 |
| windowBits | number | 是 |
| [memLevel](arkts-basicservices-zlib-options-i.md) | [MemLevel](arkts-basicservices-zlib-memlevel-e.md) | 是 |
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

## deflateParams

```TypeScript
deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

动态更新压缩级别和压缩策略。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
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

## deflatePending

```TypeScript
deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>
```

返回已生成但尚未在可用输出中提供的输出的字节数和位数。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DeflatePendingOutputInfo](arkts-basicservices-zlib-deflatependingoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflatePrime

```TypeScript
deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>
```

在压缩流中插入位和值。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| [bits](arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | 是 |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateReset

```TypeScript
deflateReset(strm: ZStream): Promise<ReturnStatus>
```

这个函数相当于先调用deflateEnd再调用deflateInit，但是并不会释放和重新分配内部解压缩状态。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateResetKeep

```TypeScript
deflateResetKeep(strm: ZStream): Promise<ReturnStatus>
```

重置初始化的deflate压缩流，但保留其设置的压缩参数和字典。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateSetDictionary

```TypeScript
deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>
```

从给定的字节序列初始化压缩字典。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| dictionary | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateSetHeader

```TypeScript
deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>
```

当deflateInit2()请求gzip流时，提供gzip标头信息。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| head | [GzHeader](arkts-basicservices-zlib-gzheader-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## deflateTune

```TypeScript
deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>
```

微调deflate的内部压缩参数。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| goodLength | number | 是 |
| maxLazy | number | 是 |
| niceLength | number | 是 |
| maxChain | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## getZStream

```TypeScript
getZStream(): Promise<ZStream>
```

输出流。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ZStream](arkts-basicservices-zlib-zstream-i.md)&gt; |

## inflate

```TypeScript
inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>
```

解压数据。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
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
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-传入的数据错误) |

## inflateBack

```TypeScript
inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>
```

实现原始解压缩，采用回调接口来处理输入和输出。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| backIn | [InflateBackInputCallback](arkts-basicservices-zlib-inflatebackinputcallback-t.md) | 是 |
| inDesc | object | 是 |
| backOut | [InflateBackOutputCallback](arkts-basicservices-zlib-inflatebackoutputcallback-t.md) | 是 |
| outDesc | object | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateBackEnd

```TypeScript
inflateBackEnd(strm: ZStream): Promise<ReturnStatus>
```

inflateBackInit()函数分配的所有内存都被释放。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateBackInit

```TypeScript
inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>
```

使用inflateBack()函数前初始化内部流状态以进行解压缩。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| windowBits | number | 是 |
| [window](../../apis-arkui/arkts-components/arkts-arkui-window-t.md) | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateCodesUsed

```TypeScript
inflateCodesUsed(strm: ZStream): Promise<number>
```

当前解压缩流中使用的霍夫曼编码树的数量。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inflateCopy

```TypeScript
inflateCopy(source: Zip): Promise<ReturnStatus>
```

复制解压流。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [Zip](arkts-basicservices-zlib-zip-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateEnd

```TypeScript
inflateEnd(strm: ZStream): Promise<ReturnStatus>
```

解压流的所有动态分配的数据结构都被释放。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateGetDictionary

```TypeScript
inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>
```

获取当前解压缩流中使用的解压缩字典内容及其长度。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| dictionary | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DictionaryOutputInfo](arkts-basicservices-zlib-dictionaryoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateGetHeader

```TypeScript
inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>
```

用于在解压缩数据前设置gzip文件头部信息。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| header | [GzHeader](arkts-basicservices-zlib-gzheader-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateInit

```TypeScript
inflateInit(strm: ZStream): Promise<ReturnStatus>
```

初始化解压缩流。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inflateInit2

```TypeScript
inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>
```

初始化解压缩流并设置指定的 windowBits 参数。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| windowBits | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateMark

```TypeScript
inflateMark(strm: ZStream): Promise<number>
```

用于标记输入数据中的位置以供随机访问。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inflatePrime

```TypeScript
inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>
```

在指定解压缩流中设置初始比特数和比特值，用于在解压流开始时预填充比特缓冲区，以正确处理流起始位置的数据。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| [bits](arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | 是 |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateReset

```TypeScript
inflateReset(strm: ZStream): Promise<ReturnStatus>
```

重置指定解压缩流的状态，使其恢复到初始化状态以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateReset2

```TypeScript
inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>
```

重置指定解压缩流的状态并更新窗口大小配置，以重新开始新的解压操作。不会释放或重新分配内部缓冲区。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| windowBits | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateResetKeep

```TypeScript
inflateResetKeep(strm: ZStream): Promise<ReturnStatus>
```

重置解压缩流的状态，以保留分配的霍夫曼解码树和预设字典。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateSetDictionary

```TypeScript
inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>
```

使用给定的字典数据初始化当前解压缩流的字典内容。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| dictionary | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-传入的数据错误) |

## inflateSync

```TypeScript
inflateSync(strm: ZStream): Promise<ReturnStatus>
```

跳过无效的压缩数据，直到找到一个可能的完整刷新点为止。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-传入的数据错误) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## inflateSyncPoint

```TypeScript
inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>
```

查找当前解压缩流的同步点。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## inflateValidate

```TypeScript
inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>
```

验证压缩流结构内部的校验和。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | 是 |
| [check](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-jsleakwatcher-check-f.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-压缩流或解压流错误) |

## uncompress

```TypeScript
uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>
```

将压缩后的数据解压缩为原始的未压缩形式。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dest | ArrayBuffer | 是 |
| source | ArrayBuffer | 是 |
| sourceLen | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-传入的数据错误) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## uncompress2

```TypeScript
uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>
```

将压缩后的数据解压缩为原始的未压缩形式。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dest | ArrayBuffer | 是 |
| source | ArrayBuffer | 是 |
| sourceLen | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DecompressionOutputInfo](arkts-basicservices-zlib-decompressionoutputinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-传入的数据错误) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-传入的缓冲区错误) |

## zlibCompileFlags

```TypeScript
zlibCompileFlags(): Promise<number>
```

返回指示编译时选项的标志。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## zlibVersion

```TypeScript
zlibVersion(): Promise<string>
```

获取当前链接的zlib库的版本信息。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |
