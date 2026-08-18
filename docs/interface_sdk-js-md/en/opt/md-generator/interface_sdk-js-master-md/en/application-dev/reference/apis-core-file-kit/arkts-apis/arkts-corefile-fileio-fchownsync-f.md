# fchownSync

## Modules to Import

```TypeScript
```

## fchownSync

```TypeScript
declare function fchownSync(fd: number, uid: number, gid: number): void
```

Changes the file owner based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function fchownSync(fd: number, uid: number, gid: number): void--><!--Device-unnamed-declare function fchownSync(fd: number, uid: number, gid: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| uid | number | Yes |
| gid | number | Yes |
