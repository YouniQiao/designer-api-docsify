# isAppUid

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## isAppUid

```TypeScript
function isAppUid(v: number): boolean
```

Checks whether a UID belongs to this application.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [isAppUid](arkts-arkts-process-processmanager-c.md#isappuid)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let result = process.isAppUid(688);
```

```TypeScript
let pro = new process.ProcessManager();
// Use process.uid to obtain the UID.
let pres = process.uid;
let result = pro.isAppUid(pres);
console.info("result: " + result); // result: true
```
