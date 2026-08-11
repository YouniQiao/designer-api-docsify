# lstatSync

## lstatSync

```TypeScript
declare function lstatSync(path: string): Stat
```

Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:lstatSync](arkts-corefile-fileio-lstatsync-f.md#lstatsync)

<!--Device-unnamed-declare function lstatSync(path: string): Stat--><!--Device-unnamed-declare function lstatSync(path: string): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stat](arkts-corefile-file-fs-stat-i.md) |
