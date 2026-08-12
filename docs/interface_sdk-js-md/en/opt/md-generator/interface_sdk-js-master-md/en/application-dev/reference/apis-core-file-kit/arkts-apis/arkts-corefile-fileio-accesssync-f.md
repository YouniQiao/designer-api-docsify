# accessSync

## accessSync

```TypeScript
declare function accessSync(path: string, mode?: number): void
```

Checks whether this process can access a file. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [accessSync](arkts-corefile-file-fs-accesssync-f.md#accessSync)

<!--Device-unnamed-declare function accessSync(path: string, mode?: number): void--><!--Device-unnamed-declare function accessSync(path: string, mode?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | No | Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (\|
