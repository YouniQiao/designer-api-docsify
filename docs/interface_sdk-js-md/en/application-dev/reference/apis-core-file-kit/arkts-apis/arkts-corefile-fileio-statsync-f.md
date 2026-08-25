# statSync

## Modules to Import

```TypeScript
```

## statSync

```TypeScript
declare function statSync(path: string): Stat
```

Obtains file information. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [statSync](arkts-corefile-file-fs-statsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stat](arkts-corefile-fileio-stat-depr-i.md) |

**Examples**

```TypeScript
let stat = fileio.statSync(pathDir);
// Example code in Stat
```
