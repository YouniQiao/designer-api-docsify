# getUidForName

## getUidForName

```TypeScript
function getUidForName(v: string): number
```

Obtains the UID of a user from the user database of the system based on the specified user name.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getUidForName](arkts-arkts-process-processmanager-c.md#getuidforname)

<!--Device-process-function getUidForName(v: string): number--><!--Device-process-function getUidForName(v: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | string | Yes | User name. |

**Return value:**

| Type | Description |
| --- | --- |
| number | UID of the user. |

**Example**

```TypeScript
let pres = process.getUidForName("tool");
```

