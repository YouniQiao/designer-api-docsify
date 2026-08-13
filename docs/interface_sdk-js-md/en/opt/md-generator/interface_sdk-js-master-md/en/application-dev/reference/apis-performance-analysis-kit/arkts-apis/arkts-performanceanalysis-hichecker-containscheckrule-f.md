# containsCheckRule

## Modules to Import

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## containsCheckRule

```TypeScript
function containsCheckRule(rule: bigint) : boolean
```

Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread.

**Since:** 23

**Deprecated since:** -1

<!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean--><!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | bigint | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Add a rule.
    hichecker.addCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS);

    // Check whether the added rule exists in the collection of added rules.
    hichecker.containsCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS); // return true;
    hichecker.containsCheckRule(hichecker.RULE_CAUTION_PRINT_LOG); // return false;
} catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```
