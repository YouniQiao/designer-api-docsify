# setSecurityLabelSync

## Modules to Import

```TypeScript
import { securityLabel } from 'kits/@kit.CoreFileKit';
```

## setSecurityLabelSync

```TypeScript
function setSecurityLabelSync(path: string, type: DataLevel): void
```

Sets the data security level for a file or directory in synchronous mode. The level can only be adjusted from low to high, or set to the same level.

**Since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |
