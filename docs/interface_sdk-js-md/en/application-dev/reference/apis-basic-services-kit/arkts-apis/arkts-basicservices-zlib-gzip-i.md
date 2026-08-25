# GZip

Describes gzip-related APIs.

**Since:** 12

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## gzbuffer

```TypeScript
gzbuffer(size: number): Promise<number>
```

Sets the internal buffer size for the current library function. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzclearerr

```TypeScript
gzclearerr(): Promise<void>
```

Clears the errors and end-of-file flags of a file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## gzclose

```TypeScript
gzclose(): Promise<ReturnStatus>
```

Clears all pending output of the file. Closes the file and releases the decompression or compression state if necessary. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800006](../../apis-ability-kit/errorcode-zlib.md#17800006-memory-allocation-failure) |

## gzcloser

```TypeScript
gzcloser(): Promise<ReturnStatus>
```

Implements the same functions as that of **gzclose()** for reading only. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## gzclosew

```TypeScript
gzclosew(): Promise<ReturnStatus>
```

Implements the same functions as that of **gzclose()** for writing or appending. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800006](../../apis-ability-kit/errorcode-zlib.md#17800006-memory-allocation-failure) |

## gzdirect

```TypeScript
gzdirect(): Promise<number>
```

Checks whether the specified gzip file handle directly accesses the original uncompressed data and reallocates the buffer. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## gzdopen

```TypeScript
gzdopen(fd: number, mode: string): Promise<void>
```

Associates gzip file with the file descriptor (fd) and opens the file for reading and decompressing, or compressing and writing. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800002](../../apis-ability-kit/errorcode-zlib.md#17800002-incorrect-file-or-access-mode) |

## gzeof

```TypeScript
gzeof(): Promise<number>
```

Checks whether the position from which data is read has reached the end of the gzip file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## gzerror

```TypeScript
gzerror(): Promise<GzErrorOutputInfo>
```

Describes the last error message that reported for the file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[GzErrorOutputInfo](arkts-basicservices-zlib-gzerroroutputinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |

## gzflush

```TypeScript
gzflush(flush: CompressFlushMode): Promise<ReturnStatus>
```

Flushes all pending output into a compressed file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
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

## gzfread

```TypeScript
gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>
```

Decompresses and reads data from a gzip file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| size | number | Yes |
| nitems | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzfwrite

```TypeScript
gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>
```

Compresses data blocks that are declared with size and nitems from the buffer and writes the data blocks to a file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| size | number | Yes |
| nitems | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzgetc

```TypeScript
gzgetc(): Promise<number>
```

Reads and decompresses a byte from a file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzgets

```TypeScript
gzgets(buf: ArrayBuffer): Promise<string>
```

Reads bytes from a compressed file until len-1 characters are read, a newline character is read and transferred to a buffer, or an end-of-file condition is encountered. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzoffset

```TypeScript
gzoffset(): Promise<number>
```

Returns the current compressed read or write offset of the file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzopen

```TypeScript
gzopen(path: string, mode: string): Promise<void>
```

Opens the .gz file in the specified path for reading and decompressing, or compressing and writing. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800002](../../apis-ability-kit/errorcode-zlib.md#17800002-incorrect-file-or-access-mode) |

## gzprintf

```TypeScript
gzprintf(format: string, ...args: Array<string | number>): Promise<number>
```

Converts and formats the parameters under the control of the string format and then compresses and writes them into a file, as shown in the **fprintf()**. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| format | string | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;string \ | number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800004](../../apis-ability-kit/errorcode-zlib.md#17800004-compressed-or-decompressed-flow-error) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzputc

```TypeScript
gzputc(ch: number): Promise<number>
```

Compresses **char** converted to an unsigned character and writes it to a file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ch | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzputs

```TypeScript
gzputs(str: string): Promise<number>
```

Compresses the given null-terminated strings and writes them to the file, excluding the null operator. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| str | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzread

```TypeScript
gzread(buf: ArrayBuffer): Promise<number>
```

Reads a maximum of **len** uncompressed bytes from a file and decompresses them into the buffer. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzrewind

```TypeScript
gzrewind(): Promise<ReturnStatus>
```

Repositions the file pointer to the beginning of the file. This feature is applied only for reading. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ReturnStatus](arkts-basicservices-zlib-returnstatus-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzseek

```TypeScript
gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>
```

Sets the start position to the offset position relative to the next **gzread** or **gzwrite** in the file.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| whence | [OffsetReferencePoint](arkts-basicservices-zlib-offsetreferencepoint-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzsetparams

```TypeScript
gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>
```

Dynamically updates the compression level and compression strategy of a file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
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

## gztell

```TypeScript
gztell(): Promise<number>
```

Returns the start position of the next **gzread** or **gzwrite** in the file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzungetc

```TypeScript
gzungetc(c: number): Promise<number>
```

Pushes **c** back into the input stream so that it will be read as the first character the next time the file is read. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| c | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |

## gzwrite

```TypeScript
gzwrite(buf: ArrayBuffer, len: number): Promise<number>
```

Compresses the uncompressed bytes of the declared length in the buffer and writes them to the file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| len | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17800009](../../apis-ability-kit/errorcode-zlib.md#17800009-internal-structure-error) |
