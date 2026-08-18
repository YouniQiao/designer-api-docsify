# writeSync

## Modules to Import

```TypeScript
```

## writeSync

```TypeScript
declare function writeSync(
  fd: number,
  buffer: ArrayBuffer | string,
  options?: WriteOptions
): number
```

Writes data to a file. This API returns the result synchronously.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): number--><!--Device-unnamed-declare function writeSync(  fd: number,  buffer: ArrayBuffer | string,  options?: WriteOptions): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| buffer | ArrayBuffer \| string | Yes |
| options | [WriteOptions](arkts-corefile-file-fs-writeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900001 |
| 13900034 |
| 13900013 |
| 13900008 |
| 13900024 |
| 13900025 |
| 13900041 |
| 13900010 |
| 13900042 |
