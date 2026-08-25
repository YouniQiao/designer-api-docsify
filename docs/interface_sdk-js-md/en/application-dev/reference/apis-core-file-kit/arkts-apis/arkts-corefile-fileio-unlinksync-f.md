# unlinkSync

## Modules to Import

```TypeScript
```

## unlinkSync

```TypeScript
declare function unlinkSync(path: string): void
```

Removes a file. This API returns the result synchronously.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [unlinkSync](arkts-corefile-file-fs-unlinksync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
fileio.unlinkSync(filePath);
```
