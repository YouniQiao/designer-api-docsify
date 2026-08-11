# chmodSync

## chmodSync

```TypeScript
declare function chmodSync(path: string, mode: number): void
```

Changes file permissions. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function chmodSync(path: string, mode: number): void--><!--Device-unnamed-declare function chmodSync(path: string, mode: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | number | Yes | Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (\|
