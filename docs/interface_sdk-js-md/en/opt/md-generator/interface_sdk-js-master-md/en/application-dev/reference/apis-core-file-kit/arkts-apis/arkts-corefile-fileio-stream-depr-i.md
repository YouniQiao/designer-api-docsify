# Stream

Provides a stream for file operations. Before calling any API of the **Stream** class, use **createStream()** to create a **Stream** instance synchronously or asynchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream](arkts-corefile-fileio-stream-depr-i.md)

<!--Device-unnamed-declare interface Stream--><!--Device-unnamed-declare interface Stream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## close

```TypeScript
close(): Promise<void>
```

Closes the file stream. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.close](arkts-corefile-fileio-stream-depr-i.md#close)

<!--Device-Stream-close(): Promise<void>--><!--Device-Stream-close(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error:" + err);
});
```

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.close](arkts-corefile-fileio-stream-depr-i.md#close)

<!--Device-Stream-close(callback: AsyncCallback<void>): void--><!--Device-Stream-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // Do something.
});
```

## closeSync

```TypeScript
closeSync(): void
```

Closes the file stream. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.closeSync](arkts-corefile-fileio-stream-depr-i.md#closesync)

<!--Device-Stream-closeSync(): void--><!--Device-Stream-closeSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

## flush

```TypeScript
flush(): Promise<void>
```

Flushes the file stream. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.flush](arkts-corefile-fileio-stream-depr-i.md#flush)

<!--Device-Stream-flush(): Promise<void>--><!--Device-Stream-flush(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush().then(() => {
  console.info("flush succeed");
}).catch((err: BusinessError) => {
  console.error("flush failed with error:" + err);
});
```

## flush

```TypeScript
flush(callback: AsyncCallback<void>): void
```

Flushes the file stream. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.flush](arkts-corefile-fileio-stream-depr-i.md#flush)

<!--Device-Stream-flush(callback: AsyncCallback<void>): void--><!--Device-Stream-flush(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush((err: BusinessError) => {
  // Do something.
});
```

## flushSync

```TypeScript
flushSync(): void
```

Flushes the file stream. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.flushSync](arkts-corefile-fileio-stream-depr-i.md#flushsync)

<!--Device-Stream-flushSync(): void--><!--Device-Stream-flushSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flushSync();
```

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options?: {
      position?: number;
      offset?: number;
      length?: number;
    }
  ): Promise<ReadOut>
```

Reads data from a stream file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.read](arkts-corefile-fileio-stream-depr-i.md#read)

<!--Device-Stream-read(    buffer: ArrayBuffer,    options?: {      position?: number;      offset?: number;      length?: number;    }  ): Promise<ReadOut>--><!--Device-Stream-read(    buffer: ArrayBuffer,    options?: {      position?: number;      offset?: number;      length?: number;    }  ): Promise<ReadOut>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | {       position?: number;       offset?: number;       length?: number;     } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ReadOut&gt; |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option).then((readResult: fileio.ReadOut) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
  console.info(`The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error("read data failed with error:" + err);
});
```

## read

```TypeScript
read(buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

read.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.read](arkts-corefile-fileio-stream-depr-i.md#read)

<!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void--><!--Device-Stream-read(buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes |

## read

```TypeScript
read(
    buffer: ArrayBuffer,
    options: {
      position?: number;
      offset?: number;
      length?: number;
    },
    callback: AsyncCallback<ReadOut>
  ): void
```

Reads data from a stream file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.read](arkts-corefile-fileio-stream-depr-i.md#read)

<!--Device-Stream-read(    buffer: ArrayBuffer,    options: {      position?: number;      offset?: number;      length?: number;    },    callback: AsyncCallback<ReadOut>  ): void--><!--Device-Stream-read(    buffer: ArrayBuffer,    options: {      position?: number;      offset?: number;      length?: number;    },    callback: AsyncCallback<ReadOut>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | {       position?: number;       offset?: number;       length?: number;     } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option, (err: BusinessError, readResult: fileio.ReadOut) => {
  if (readResult.bytesRead) {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
    console.info(`The content of file: ${buf.toString()}`);
  }
});
```

## readSync

```TypeScript
readSync(
    buffer: ArrayBuffer,
    options?: {
      position?: number;
      offset?: number;
      length?: number;
    }
  ): number
```

Reads data from a stream file. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.readSync](arkts-corefile-fileio-stream-depr-i.md#readsync)

<!--Device-Stream-readSync(    buffer: ArrayBuffer,    options?: {      position?: number;      offset?: number;      length?: number;    }  ): number--><!--Device-Stream-readSync(    buffer: ArrayBuffer,    options?: {      position?: number;      offset?: number;      length?: number;    }  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| options | {       position?: number;       offset?: number;       length?: number;     } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let buf = new ArrayBuffer(4096)
let num = ss.readSync(buf, option);
```

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options?: {
      offset?: number;
      length?: number;
      position?: number;
      encoding?: string;
    }
  ): Promise<number>
```

Writes data to a stream file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.write](arkts-corefile-fileio-stream-depr-i.md#write)

<!--Device-Stream-write(    buffer: ArrayBuffer | string,    options?: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    }  ): Promise<number>--><!--Device-Stream-write(    buffer: ArrayBuffer | string,    options?: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    }  ): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option).then((number: number) => {
  console.info("write succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write failed with error:" + err);
});
```

## write

```TypeScript
write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.write](arkts-corefile-fileio-stream-depr-i.md#write)

<!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-Stream-write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## write

```TypeScript
write(
    buffer: ArrayBuffer | string,
    options: {
      offset?: number;
      length?: number;
      position?: number;
      encoding?: string;
    },
    callback: AsyncCallback<number>
  ): void
```

Writes data to a stream file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.write](arkts-corefile-fileio-stream-depr-i.md#write)

<!--Device-Stream-write(    buffer: ArrayBuffer | string,    options: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    },    callback: AsyncCallback<number>  ): void--><!--Device-Stream-write(    buffer: ArrayBuffer | string,    options: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    },    callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option, (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    // Do something.
    console.info("write succeed and size is:" + bytesWritten);
  }
});
```

## writeSync

```TypeScript
writeSync(
    buffer: ArrayBuffer | string,
    options?: {
      offset?: number;
      length?: number;
      position?: number;
      encoding?: string;
    }
  ): number
```

Writes data to a stream file. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:Stream.writeSync](arkts-corefile-fileio-stream-depr-i.md#writesync)

<!--Device-Stream-writeSync(    buffer: ArrayBuffer | string,    options?: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    }  ): number--><!--Device-Stream-writeSync(    buffer: ArrayBuffer | string,    options?: {      offset?: number;      length?: number;      position?: number;      encoding?: string;    }  ): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| string | Yes |
| options | {       offset?: number;       length?: number;       position?: number;       encoding?: string;     } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath,"r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let num = ss.writeSync("hello, world", option);
```
