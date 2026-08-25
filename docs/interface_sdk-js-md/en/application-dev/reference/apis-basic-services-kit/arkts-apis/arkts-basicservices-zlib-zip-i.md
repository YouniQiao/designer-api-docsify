# Zip

Defines the **Zip** instance. It provides APIs to zip or unzip data in Zlib, Deflate, or Gzip format.

**Since:** 12

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## compress

```TypeScript
compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>
```

Compresses the source buffer into the destination buffer. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dest | ArrayBuffer | Yes |
| source | ArrayBuffer | Yes |
| sourceLen | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## compress2

```TypeScript
compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number,): Promise<ZipOutputInfo>
```

Compresses the source buffer into the destination buffer. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dest | ArrayBuffer | Yes |
| source | ArrayBuffer | Yes |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | Yes |
| sourceLen | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## compressBound

```TypeScript
compressBound(sourceLen: number): Promise<number>
```

Calculates the maximum size of the compressed data to be returned. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceLen | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## deflate

```TypeScript
deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>
```

Deflates data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| flush | [CompressFlushMode](arkts-basicservices-zlib-compressflushmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## deflateBound

```TypeScript
deflateBound(strm: ZStream, sourceLength: number): Promise<number>
```

Calculates the maximum size of the compressed data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| [sourceLength](arkts-basicservices-zlib-decompressionoutputinfo-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## deflateCopy

```TypeScript
deflateCopy(source: Zip): Promise<ReturnStatus>
```

Copies a compression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [Zip](arkts-basicservices-zlib-zip-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateEnd

```TypeScript
deflateEnd(strm: ZStream): Promise<ReturnStatus>
```

Releases all dynamically allocated data structs of a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateGetDictionary

```TypeScript
deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>
```

Obtains the content and length of the decompression dictionary used in a compression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| dictionary | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DictionaryOutputInfo](arkts-basicservices-zlib-dictionaryoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateInit

```TypeScript
deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>
```

Initializes a compression stream with a specified compression level. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateInit2

```TypeScript
deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number,
        memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

Initializes a compression stream with the specified compression level, compression method, window size, memory level, and compression strategy. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | Yes |
| method | [CompressMethod](arkts-basicservices-zlib-compressmethod-e.md) | Yes |
| windowBits | number | Yes |
| [memLevel](arkts-basicservices-zlib-options-i.md) | [MemLevel](arkts-basicservices-zlib-memlevel-e.md) | Yes |
| strategy | [CompressStrategy](arkts-basicservices-zlib-compressstrategy-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateParams

```TypeScript
deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

Dynamically updates the compression level and compression strategy. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| level | [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md) | Yes |
| strategy | [CompressStrategy](arkts-basicservices-zlib-compressstrategy-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflatePending

```TypeScript
deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>
```

Returns the number of bytes and bits of output that has been generated but not yet provided in the available output. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DeflatePendingOutputInfo](arkts-basicservices-zlib-deflatependingoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflatePrime

```TypeScript
deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>
```

Inserts bits and values into the compression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| [bits](arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateReset

```TypeScript
deflateReset(strm: ZStream): Promise<ReturnStatus>
```

Equivalent to call the **deflateEnd** API and then the **deflateInit** API. However, this API does not release or reallocate the internal decompression state. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateResetKeep

```TypeScript
deflateResetKeep(strm: ZStream): Promise<ReturnStatus>
```

Resets the initialized compression stream, but retains the compression parameters and dictionaries set by it. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateSetDictionary

```TypeScript
deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>
```

Initializes the compression dictionary from a given sequence of bytes. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| dictionary | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateSetHeader

```TypeScript
deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>
```

Provides the header information of a gzip file when **deflateInit2()** requests a gzip stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| head | [GzHeader](arkts-basicservices-zlib-gzheader-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## deflateTune

```TypeScript
deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>
```

Fine-tunes the internal compression parameters of **deflate**. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| goodLength | number | Yes |
| maxLazy | number | Yes |
| niceLength | number | Yes |
| maxChain | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## getZStream

```TypeScript
getZStream(): Promise<ZStream>
```

Obtains this stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ZStream](arkts-basicservices-zlib-zstream-i.md)&gt; |

## inflate

```TypeScript
inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>
```

Inflates data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| flush | [CompressFlushMode](arkts-basicservices-zlib-compressflushmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-incorrect-input-data) |

## inflateBack

```TypeScript
inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>
```

Implements decompression and uses callbacks to process input and output data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| backIn | [InflateBackInputCallback](arkts-basicservices-zlib-inflatebackinputcallback-t.md) | Yes |
| inDesc | object | Yes |
| backOut | [InflateBackOutputCallback](arkts-basicservices-zlib-inflatebackoutputcallback-t.md) | Yes |
| outDesc | object | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateBackEnd

```TypeScript
inflateBackEnd(strm: ZStream): Promise<ReturnStatus>
```

Releases all memory allocated by the **inflateBackInit()** function. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateBackInit

```TypeScript
inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>
```

Initializes the internal stream state for decompression before using the **inflateBack()** function. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| windowBits | number | Yes |
| [window](../../apis-arkui/arkts-components/arkts-arkui-window-t.md) | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateCodesUsed

```TypeScript
inflateCodesUsed(strm: ZStream): Promise<number>
```

Describes the number of Huffman trees used in a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inflateCopy

```TypeScript
inflateCopy(source: Zip): Promise<ReturnStatus>
```

Copies a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [Zip](arkts-basicservices-zlib-zip-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateEnd

```TypeScript
inflateEnd(strm: ZStream): Promise<ReturnStatus>
```

Releases all dynamically allocated data structs of a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateGetDictionary

```TypeScript
inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>
```

Obtains the content and length of the decompression dictionary used in a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| dictionary | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DictionaryOutputInfo](arkts-basicservices-zlib-dictionaryoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateGetHeader

```TypeScript
inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>
```

Obtains the header information of a gzip file before decompressing data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| header | [GzHeader](arkts-basicservices-zlib-gzheader-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateInit

```TypeScript
inflateInit(strm: ZStream): Promise<ReturnStatus>
```

Initializes a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inflateInit2

```TypeScript
inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>
```

Initializes a decompression stream with the specified **windowBits**. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| windowBits | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateMark

```TypeScript
inflateMark(strm: ZStream): Promise<number>
```

Marks the location of the input data for random access. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## inflatePrime

```TypeScript
inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>
```

Sets the initial number of bits and bit value in the specified decompression stream to pre-fill the bit buffer at the beginning of the decompression stream to correctly process the data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| [bits](arkts-basicservices-zlib-deflatependingoutputinfo-i.md) | number | Yes |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateReset

```TypeScript
inflateReset(strm: ZStream): Promise<ReturnStatus>
```

Resets the status of the specified decompression stream to the initial state to start a new decompression operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateReset2

```TypeScript
inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>
```

Resets the status of the specified decompression stream and updates the window size to start a new decompression operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| windowBits | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateResetKeep

```TypeScript
inflateResetKeep(strm: ZStream): Promise<ReturnStatus>
```

Resets the state of the decompression stream to retain the allocated Huffman tree and preset dictionary. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateSetDictionary

```TypeScript
inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>
```

Initializes the dictionary content of a decompression stream based on the given dictionary data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| dictionary | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-incorrect-input-data) |

## inflateSync

```TypeScript
inflateSync(strm: ZStream): Promise<ReturnStatus>
```

Skips invalid compressed data until a possible complete refresh point is found. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-incorrect-input-data) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## inflateSyncPoint

```TypeScript
inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>
```

Finds the synchronization point of a decompression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## inflateValidate

```TypeScript
inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>
```

Validates the checksum inside the compression stream. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strm | [ZStream](arkts-basicservices-zlib-zstream-i.md) | Yes |
| [check](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-jsleakwatcher-check-f.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## uncompress

```TypeScript
uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>
```

Decompresses the compressed data into the raw data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dest | ArrayBuffer | Yes |
| source | ArrayBuffer | Yes |
| sourceLen | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ZipOutputInfo](arkts-basicservices-zlib-zipoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-incorrect-input-data) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## uncompress2

```TypeScript
uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>
```

Decompresses the compressed data into the raw data. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dest | ArrayBuffer | Yes |
| source | ArrayBuffer | Yes |
| sourceLen | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DecompressionOutputInfo](arkts-basicservices-zlib-decompressionoutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800005](../../apis-ability-kit/errorcode-zlib.md#17800005-incorrect-input-data) |
| [17800007](../../apis-ability-kit/errorcode-zlib.md#17800007-incorrect-input-buffer) |

## zlibCompileFlags

```TypeScript
zlibCompileFlags(): Promise<number>
```

Returns the flags indicating compile-time options. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## zlibVersion

```TypeScript
zlibVersion(): Promise<string>
```

Obtains the version information of this zlib library connected. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |
