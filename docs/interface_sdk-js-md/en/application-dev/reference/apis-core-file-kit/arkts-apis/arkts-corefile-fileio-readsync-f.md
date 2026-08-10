# readSync

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
  }
): number
```

以同步方法从文件读取数据。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readSync](arkts-corefile-fileio-readsync-f.md#readsync)

<!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): number--><!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: {    offset?: number;    length?: number;    position?: number;  }): number-End-->

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
| number | 实际读取的长度，单位为Byte。 |

