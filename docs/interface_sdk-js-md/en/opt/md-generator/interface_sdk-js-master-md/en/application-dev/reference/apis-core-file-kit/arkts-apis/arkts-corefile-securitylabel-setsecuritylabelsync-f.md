# setSecurityLabelSync

## Modules to Import

```TypeScript
```

## setSecurityLabelSync

```TypeScript
function setSecurityLabelSync(path: string, type: DataLevel): void
```

Sets the data security level for a file or directory in synchronous mode. The level can only be adjusted from low to high, or set to the same level.

**Since:** 23

<!--Device-securityLabel-function setSecurityLabelSync(path: string, type: DataLevel): void--><!--Device-securityLabel-function setSecurityLabelSync(path: string, type: DataLevel): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | Yes |

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
securityLabel.setSecurityLabelSync(filePath, "s0");
```
