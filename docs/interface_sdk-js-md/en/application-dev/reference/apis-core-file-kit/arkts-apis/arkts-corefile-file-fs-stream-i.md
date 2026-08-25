# Stream

Provides API for stream operations. Before calling any API of **Stream**, you need to create a **Stream** instance by using [fileIo.createStream](../../../reference/apis-core-file-kit/js-apis-file-fs.md#fileiocreatestream) or [fileIo.fdopenStream](../../../reference/apis-core-file-kit/js-apis-file-fs.md#fileiofdopenstream).

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { fileIo, ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, DfsListeners, TaskSignal } from 'kits/@kit.CoreFileKit';
import { fileIo } from 'kits/@kit.CoreFileKit'
import { ConflictFiles, FileFilter, Filter, Options, ReaderIteratorResult, WatchEvent, WatchEventListener, Watcher, ReadOptions, ReadTextOptions, WriteOptions, ListFileExtOptions, ListFileOptions, TaskSignal } from 'kits/@kit.CoreFileKit';
```

## close

```TypeScript
close(): Promise<void>
```

Closes the file stream. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## closeSync

```TypeScript
closeSync(): void
```

Closes the file stream. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the file stream. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## flushSync

```TypeScript
flushSync(): void
```

Flushes the file stream. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## read

```TypeScript
read(
      buffer: ArrayBuffer,
      options?: ReadOptions
  ): Promise<number>
```

Reads data from a stream file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900044 |

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void
```

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900034 |
| 13900042 |

## read

```TypeScript
read(
      buffer: ArrayBuffer,
      options: ReadOptions,
      callback: AsyncCallback<number>
  ): void
```

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900034 |
| 13900042 |

## readSync

```TypeScript
readSync(
      buffer: ArrayBuffer,
      options?: ReadOptions
  ): number
```

Reads data from a stream file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900019 |
| 13900020 |
| 13900034 |
| 13900042 |
| 13900044 |

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): Promise<number>
```

Writes data to a stream file. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## write

```TypeScript
write(
      buffer: ArrayBuffer | string,
      options: WriteOptions,
      callback: AsyncCallback<number>
  ): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |

## writeSync

```TypeScript
writeSync(
      buffer: ArrayBuffer | string,
      options?: WriteOptions
  ): number
```

Writes data to a stream file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900013 |
| 13900020 |
| 13900024 |
| 13900025 |
| 13900034 |
| 13900041 |
| 13900042 |
