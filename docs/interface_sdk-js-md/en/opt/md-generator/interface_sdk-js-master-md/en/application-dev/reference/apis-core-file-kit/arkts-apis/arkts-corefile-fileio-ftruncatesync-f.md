# ftruncateSync

## Modules to Import

```TypeScript
```

## ftruncateSync

```TypeScript
declare function ftruncateSync(fd: number, len?: number): void
```

Truncates a file based on the file descriptor. This API returns the result synchronously.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [truncateSync](arkts-corefile-file-fs-truncatesync-f.md#truncatesync)

<!--Device-unnamed-declare function ftruncateSync(fd: number, len?: number): void--><!--Device-unnamed-declare function ftruncateSync(fd: number, len?: number): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| len | number | No |
