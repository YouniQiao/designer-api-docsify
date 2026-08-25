# rmdirSync

## Modules to Import

```TypeScript
```

## rmdirSync

```TypeScript
declare function rmdirSync(path: string): void
```

Removes a directory. This API returns the result synchronously.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [rmdirSync](arkts-corefile-file-fs-rmdirsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Examples**

```TypeScript
let dirPath = pathDir + '/testDir';
fileio.rmdirSync(dirPath);
```
