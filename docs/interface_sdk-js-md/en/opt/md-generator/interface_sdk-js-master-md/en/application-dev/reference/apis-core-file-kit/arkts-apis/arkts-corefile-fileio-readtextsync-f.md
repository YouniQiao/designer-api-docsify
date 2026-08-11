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

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:readTextSync](arkts-corefile-fileio-readtextsync-f.md#readtextsync)

<!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string--><!--Device-unnamed-declare function readTextSync(  filePath: string,  options?: {    position?: number;    length?: number;    encoding?: string;  }): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| options | {     position?: number;     length?: number;     encoding?: string;   } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
