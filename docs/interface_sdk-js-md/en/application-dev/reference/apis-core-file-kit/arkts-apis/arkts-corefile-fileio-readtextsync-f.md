# readTextSync

## readTextSync

```TypeScript
declare function readTextSync(
  filePath: string,
  options?: {
    position?: number;
    length?: number;
    encoding?: string;
  }
): string
```

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readTextSync](arkts-corefile-fileio-readtextsync-f.md#readtextsync)

<!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string--><!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 待读取文件的应用沙箱路径。 |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No | 支持如下选项：&lt;br/&gt;-?position，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。&lt;br/&gt;-?length，number 类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度减去偏移长度。&lt;br/&gt;-?encoding，string类型，当数据是?string?类型时有效，表示数据的编码方式，默认?'utf-8'，仅支持?'utf- 8'。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回读取文件的内容。 |

