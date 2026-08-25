# createStreamSync

## Modules to Import

```TypeScript
```

## createStreamSync

```TypeScript
declare function createStreamSync(path: string, mode: string): Stream
```

Creates a stream based on the file path. This API returns the result synchronously.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [createStreamSync](arkts-corefile-file-fs-createstreamsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| mode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Stream](arkts-corefile-fileio-stream-depr-i.md) |

**Examples**

```TypeScript
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
```
