# readTextSync

## Modules to Import

```TypeScript
```

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

**Deprecated since:** 9

**Substitutes:** [readTextSync](arkts-corefile-file-fs-readtextsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No | The options are as follows:   - **position** (number): position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the current position.   - **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length minus the offset.   - **encoding** (string): format of the data to be encoded.   It is valid only when the data is of the string type.The default value is **'utf-8'**, which is the only value supported. |

**Return value:**

| Type | Description |
| --- | --- |
| string | File content read. |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.length = 3;
let str = fileio.readTextSync(filePath, option);
```
