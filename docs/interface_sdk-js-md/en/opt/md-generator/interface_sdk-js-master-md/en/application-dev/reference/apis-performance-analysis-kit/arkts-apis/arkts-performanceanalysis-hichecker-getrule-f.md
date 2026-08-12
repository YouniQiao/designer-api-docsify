# getRule

## Modules to Import

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## getRule

```TypeScript
function getRule() : bigint
```

Obtains a collection of thread, process, and alarm rules that have been added.

**Since:** 8

<!--Device-hichecker-function getRule() : bigint--><!--Device-hichecker-function getRule() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## Examples

```TypeScript
// Add a rule.
hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);

// Obtain the collection of added rules.
hichecker.getRule(); // return 1n;
```
