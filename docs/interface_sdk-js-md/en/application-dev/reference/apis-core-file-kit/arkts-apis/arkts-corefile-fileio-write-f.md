# write

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

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No | The options are as follows:&lt;br&gt;- **offset** (number): offset of the write position relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.&lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length minus the offset.&lt;br&gt;- **position** (number): start position to write the data into the file, in bytes. This parameter is optional. By default, data is written from the current position.&lt;br&gt;- **encoding** ( string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.&lt;br&gt;Constraints: offset + length <= Buffer size |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise that returns the length of the data written, in bytes. |


## write

```TypeScript
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void
```

Writes data to a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback invoked when the data is written asynchronously. return the length of the data written, in bytes. |


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

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void--><!--Device-unnamed-declare function write(  fd: number,  buffer: ArrayBuffer | string,  options: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  },  callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer \| string | Yes | Data to write. It can be a string or data from a buffer. |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | Yes | The options are as follows:&lt;br&gt;- **offset** (number): offset of the write position relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.&lt;br&gt;- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the buffer length minus the offset.&lt;br&gt;- **position** (number): start position to write the data into the file, in bytes. This parameter is optional. By default, data is written from the current position.&lt;br&gt;- **encoding** ( string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.&lt;br&gt;Constraints: offset + length <= Buffer size |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback invoked when the data is written asynchronously. return the length of the data written, in bytes. |

