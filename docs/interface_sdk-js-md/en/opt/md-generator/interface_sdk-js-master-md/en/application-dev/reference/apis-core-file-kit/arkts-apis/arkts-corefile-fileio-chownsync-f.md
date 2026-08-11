# chownSync

## chownSync

```TypeScript
declare function chownSync(path: string, uid: number, gid: number): void
```

Changes the file owner based on its path. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

<!--Device-unnamed-declare function chownSync(path: string, uid: number, gid: number): void--><!--Device-unnamed-declare function chownSync(path: string, uid: number, gid: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| uid | number | Yes |
| gid | number | Yes |
