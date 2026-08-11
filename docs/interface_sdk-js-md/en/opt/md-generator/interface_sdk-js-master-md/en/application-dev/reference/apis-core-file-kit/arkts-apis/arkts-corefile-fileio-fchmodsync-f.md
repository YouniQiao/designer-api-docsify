# fchmodSync

## fchmodSync

```TypeScript
declare function fchmodSync(fd: number, mode: number): void
```

Changes the file permissions based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function fchmodSync(fd: number, mode: number): void--><!--Device-unnamed-declare function fchmodSync(fd: number, mode: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|
