# getxattrSync

## Modules to Import

```TypeScript
```

## getxattrSync

```TypeScript
declare function getxattrSync(path: string, key: string): string
```

Obtains an extended attribute of a file or directory. This API returns the result synchronously.

**Since:** 12

<!--Device-unnamed-declare function getxattrSync(path: string, key: string): string--><!--Device-unnamed-declare function getxattrSync(path: string, key: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900037 |
| 13900038 |
| 13900007 |
| 13900002 |
| 13900012 |
| 13900031 |
| 13900042 |
