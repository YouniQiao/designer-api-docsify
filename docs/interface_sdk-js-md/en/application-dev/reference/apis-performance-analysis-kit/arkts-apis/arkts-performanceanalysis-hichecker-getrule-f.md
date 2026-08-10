# getRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## getRule

```TypeScript
function getRule() : bigint
```

��ȡ��ǰ�̹߳��򡢽��̹��򡢸澯����ĺϼ���

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hichecker-function getRule() : bigint--><!--Device-hichecker-function getRule() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Return value:**

| Type | Description |
| --- | --- |
| bigint | ��ǰϵͳ�����ӵĹ��� |

## Examples

```TypeScript
// Add a rule.
hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);

// Obtain the collection of added rules.
hichecker.getRule(); // return 1n;
```

