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

Writes data to a file. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:writeSync](arkts-corefile-fileio-writesync-f.md#writesync)

<!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number--><!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: {    offset?: number;    length?: number;    position?: number;    encoding?: string;  }): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer \| string | Yes |
| options | {     offset?: number;     length?: number;     position?: number;     encoding?: string;   } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
