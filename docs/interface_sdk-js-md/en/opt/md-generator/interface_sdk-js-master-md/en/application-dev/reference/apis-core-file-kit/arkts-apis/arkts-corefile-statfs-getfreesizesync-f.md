# getFreeSizeSync

## Modules to Import

```TypeScript
import { statfs } from 'kits/@kit.CoreFileKit';
```

## getFreeSizeSync

```TypeScript
function getFreeSizeSync(path: string): number
```

Obtains the free size of the specified file system, in bytes. This API returns the result synchronously.

**Since:** 10

<!--Device-statfs-function getFreeSizeSync(path: string): long--><!--Device-statfs-function getFreeSizeSync(path: string): long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
let number = statfs.getFreeSizeSync(path);
console.info("getFreeSizeSync succeed, Size: " + number);
```
