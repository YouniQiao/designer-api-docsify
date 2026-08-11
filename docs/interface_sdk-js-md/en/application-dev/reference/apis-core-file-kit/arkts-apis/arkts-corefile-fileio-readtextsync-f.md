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

Reads the text content of a file. This API returns the result synchronously.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readTextSync](arkts-corefile-fileio-readtextsync-f.md#readtextsync)

<!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string--><!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No | The options are as follows:&lt;br&gt;- **position** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.&lt;br&gt;- **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length minus the offset.&lt;br&gt;- **encoding** (string): format of the data to be encoded.&lt;br&gt;It is valid only when the data is of the string type.&lt;br&gt;The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| string | File content read. |

