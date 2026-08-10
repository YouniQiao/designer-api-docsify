# read

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

从文件读取数据，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): Promise<ReadOut>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | Yes | 用于保存读取到的文件数据的缓冲区。 |
| options | {     offset?: number;     length?: number;     position?: number;   } | No | 支持如下选项：&lt;br/&gt;-?offset，number类型，表示将数据读取到缓冲区的位置，即相对于缓冲区首地址的偏移，单位为Byte。可选，默认为0。&lt;br/&gt;-? length，number类型，表示期望读取数据的长度。可选，默认缓冲区长度减去偏移长度，单位为Byte。&lt;br/&gt;-?position，number类型，表示期望读取文件的位置。可选，默认从当前位置开始读，单位为Byte。&lt; br/&gt;约束：offset+length<=buffer.size。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ReadOut&gt; | Promise对象。返回读取的结果。 |


## read

```TypeScript
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void
```

从文件读取数据，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | Yes | 用于保存读取到的文件数据的缓冲区。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes | 异步读取数据之后的回调。 |


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

从文件读取数据，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:read](arkts-corefile-fileio-read-f.md#read)

<!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void--><!--Device-unnamed-declare function read(  fd: number,  buffer: ArrayBuffer,  options: {    offset?: number;    length?: number;    position?: number;  },  callback: AsyncCallback<ReadOut>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待读取文件的文件描述符。 |
| buffer | ArrayBuffer | Yes | 用于保存读取到的文件数据的缓冲区。 |
| options | {     offset?: number;     length?: number;     position?: number;   } | Yes | 支持如下选项：&lt;br/&gt;-?offset，number类型，表示将数据读取到缓冲区的位置，单位为Byte，即相对于缓冲区首地址的偏移。可选，默认为0。&lt;br/&gt;-? length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。&lt;br/&gt;-?position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。&lt; br/&gt;约束：offset+length<=buffer.size。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ReadOut&gt; | Yes | 异步读取数据之后的回调。 |

