# writeSync

## writeSync

```TypeScript
declare function writeSync(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
  }
): number
```

以同步方法将数据写入文件。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:writeSync](arkts-corefile-fileio-writesync-f.md#writesync)

<!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number--><!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | 待写入文件的文件描述符。 |
| buffer | ArrayBuffer \| string | Yes | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No | 支持如下选项：&lt;br/&gt;-?offset，number类型，表示期望写入数据的位置相对于数据首地址的偏移，单位为Byte。可选，默认为0。&lt;br/&gt;-?length， number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。&lt;br/&gt;-?position，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。&lt;br/&gt;-? encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认?'utf-8'。仅支持?'utf-8'。&lt;br/&gt;约束：offset+length<=buffer.size。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |

