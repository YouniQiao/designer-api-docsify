# mkdirSync

## mkdirSync

```TypeScript
declare function mkdirSync(path: string, mode?: number): void
```

Creates a directory. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [@ohos.file.fs:mkdirSync](arkts-corefile-fileio-mkdirsync-f.md#mkdirsync)

<!--Device-unnamed-declare function mkdirSync(path: string, mode?: number): void--><!--Device-unnamed-declare function mkdirSync(path: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | No | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|
