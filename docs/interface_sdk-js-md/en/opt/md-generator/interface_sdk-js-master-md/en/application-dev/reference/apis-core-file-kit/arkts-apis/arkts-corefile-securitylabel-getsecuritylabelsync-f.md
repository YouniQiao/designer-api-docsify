# getSecurityLabelSync

## Modules to Import

```TypeScript
```

## getSecurityLabelSync

```TypeScript
function getSecurityLabelSync(path: string): string
```

Obtains the data security level of a file or directory in synchronous mode. If no data security level has been set, **s3** is returned by default.

**Since:** 23

<!--Device-securityLabel-function getSecurityLabelSync(path: string): string--><!--Device-securityLabel-function getSecurityLabelSync(path: string): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

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
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

**Examples**

```TypeScript
let filePath = pathDir + '/test.txt';
let type = securityLabel.getSecurityLabelSync(filePath);
console.info("getSecurityLabel successfully, Label: " + type);
```
