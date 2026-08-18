# createReadStream

## Modules to Import

```TypeScript
```

## createReadStream

```TypeScript
declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream
```

Creates a readable stream. This API returns the result synchronously.

**Since:** 12

<!--Device-unnamed-declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream--><!--Device-unnamed-declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| options | [ReadStreamOptions](arkts-corefile-file-fs-readstreamoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ReadStream](arkts-corefile-file-fs-readstream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900022 |
| 13900017 |
| 13900019 |
| 13900030 |
| 13900024 |
| 13900004 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900038 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900011 |
