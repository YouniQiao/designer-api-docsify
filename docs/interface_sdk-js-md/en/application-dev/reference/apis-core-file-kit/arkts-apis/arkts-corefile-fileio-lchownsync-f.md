# lchownSync

## Modules to Import

```TypeScript
```

## lchownSync

```TypeScript
declare function lchownSync(path: string, uid: number, gid: number): void
```

Changes the file owner based on a file path and changes the owner of the symbolic link (not the referenced file). This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| uid | number | Yes |
| gid | number | Yes |
