# read

## Modules to Import

```TypeScript
```

## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): Promise<ReadOut>
```

Reads data from a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | {     offset?: number;     length?: number;     position?: number;   } | No | The options are as follows:<br>- **offset** (number): position to store the data read in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position, in bytes.<br> Constraints: offset + length &lt;= Buffer size |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; | Promise that returns the data read. |

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
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md)

<!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; | Yes | Callback invoked when the data is read asynchronously. |

**Examples**

See [read](#read)


## read

```TypeScript
declare function read(
  fd: number,
  buffer: ArrayBuffer,
  options: {
    offset?: number;
    length?: number;
    position?: number;
  },
  callback: AsyncCallback<ReadOut>
): void
```

Reads data from a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | {     offset?: number;     length?: number;     position?: number;   } | Yes | The options are as follows:<br>- **offset** (number): byte offset from the start of the buffer where the read data is stored. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length minus the offset.<br>- **position** (number): position in the file to read from, in bytes. This parameter is optional. By default, data is read from the current position.<br>Constraints: offset + length &lt;= Buffer size |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ReadOut](arkts-corefile-fileio-readout-depr-i.md)&gt; | Yes | Callback invoked when the data is read asynchronously. |

**Examples**

See [read](#read)

