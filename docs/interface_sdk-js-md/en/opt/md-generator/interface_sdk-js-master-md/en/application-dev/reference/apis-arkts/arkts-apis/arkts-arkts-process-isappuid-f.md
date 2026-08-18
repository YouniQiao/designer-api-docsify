# isAppUid

## Modules to Import

```TypeScript
```

## isAppUid

```TypeScript
function isAppUid(v: number): boolean
```

Checks whether a UID belongs to this application.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isAppUid](arkts-arkts-process-processmanager-c.md#isappuid)

<!--Device-process-function isAppUid(v: number): boolean--><!--Device-process-function isAppUid(v: number): boolean-End-->

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
