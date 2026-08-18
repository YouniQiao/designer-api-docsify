# fstatSync

## Modules to Import

```TypeScript
```

## fstatSync

```TypeScript
declare function fstatSync(fd: number): Stat
```

Obtains file status based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [statSync](arkts-corefile-file-fs-statsync-f.md#statsync)

<!--Device-unnamed-declare function fstatSync(fd: number): Stat--><!--Device-unnamed-declare function fstatSync(fd: number): Stat-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stat](arkts-corefile-fileio-stat-depr-i.md) |
