# write

## Modules to Import

```TypeScript
```

## write

```TypeScript
declare function write(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): Promise<number>
```

Writes data into a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No | The options are as follows:<br>- **offset** (number): offset of the write position relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** ( string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>Constraints: offset + length &lt;= Buffer size |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise that returns the length of the data written, in bytes. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world").then((number: number) => {
  console.info("write data to file succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world", (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    console.info("write data to file succeed and size is:" + bytesWritten);
  }
});
```

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


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback invoked when the data is written asynchronously. return the length of the data written, in bytes. |

**Examples**

See [write](#write)


## write

```TypeScript
declare function write(
  fd: number,
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

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | Yes | The options are as follows:<br>- **offset** (number): offset of the write position relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** ( string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.<br>Constraints: offset + length &lt;= Buffer size |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback invoked when the data is written asynchronously. return the length of the data written, in bytes. |

**Examples**

See [write](#write)

