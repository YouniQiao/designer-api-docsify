# getUriFromPath

## Modules to Import

```TypeScript
```

## getUriFromPath

```TypeScript
function getUriFromPath(path: string): string
```

Get the uri from the path of file in app sandbox

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-fileUri-function getUriFromPath(path: string): string--><!--Device-fileUri-function getUriFromPath(path: string): string-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
let filePath = pathDir + "/test";
let uri = fileUri.getUriFromPath(filePath);
```
