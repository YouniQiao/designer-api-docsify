# Dir

Manages directories. Before calling a method of the **Dir** class, use the **opendir()** method synchronously or asynchronously to create a **Dir** instance.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-unnamed-declare interface Dir--><!--Device-unnamed-declare interface Dir-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): Promise<void>
```

Closes a directory. This API uses a promise to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-close(): Promise<void>--><!--Device-Dir-close(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | return Promise |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd, (err: BusinessError) => {
  // Do something.
});
```

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

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // Do something.
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
dir.close().then(() => {
  console.info("close dir successfully");
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
dir.close((err: BusinessError) => {
  console.info("close dir successfully");
});
```

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes a directory. This API uses an asynchronous callback to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-close(callback: AsyncCallback<void>): void--><!--Device-Dir-close(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | callback. |

**Examples**

See [close](#close)

## closeSync

```TypeScript
closeSync(): void
```

Closes a directory. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-closeSync(): void--><!--Device-Dir-closeSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);
```

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();
```

```TypeScript
dir.closeSync();
```

## read

```TypeScript
read(): Promise<Dirent>
```

Reads the next directory entry. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-read(): Promise<Dirent>--><!--Device-Dir-read(): Promise<Dirent>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; | Promise that returns the next directory entry. |

**Examples**

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

```TypeScript
import { BusinessError } from '@ohos.base';
dir.read().then((dirent: fileio.Dirent) => {
  console.info("read succeed, the name of dirent is " + dirent.name);
}).catch((err: BusinessError) => {
  console.error("read failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
dir.read((err: BusinessError, dirent: fileio.Dirent) => {
  if (dirent) {
    // Do something.
    console.info("read succeed, the name of file is " + dirent.name);
  }
});
```

## read

```TypeScript
read(callback: AsyncCallback<Dirent>): void
```

Reads the next directory entry. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-read(callback: AsyncCallback<Dirent>): void--><!--Device-Dir-read(callback: AsyncCallback<Dirent>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; | Yes | Callback invoked when the next directory entry is asynchronously read. |

**Examples**

See [read](#read)

## readSync

```TypeScript
readSync(): Dirent
```

Reads the next directory entry. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-Dir-readSync(): Dirent--><!--Device-Dir-readSync(): Dirent-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| [Dirent](arkts-corefile-fileio-dirent-depr-i.md) | Directory entry read. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o2);
let buf = new ArrayBuffer(4096);
let num = fileio.readSync(fd, buf);
```

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

```TypeScript
let dirent = dir.readSync();
```

