# contains

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## contains

```TypeScript
function contains(rule: bigint): boolean
```

Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md)

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
