# contains

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## contains

```TypeScript
function contains(rule: bigint): boolean
```

> **˵����**
> 
> ��API version 8��ʼ֧�֣���API version 9��ʼ����������ʹ��[hichecker.containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md#containscheckrule)�����

��ǰ�����ӵĹ������Ƿ������ĳһ���ض��Ĺ����������Ĺ��򼶱�Ϊ�̼߳�������ڵ�ǰ�߳��н��в�ѯ��

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [hichecker.containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md#containscheckrule)

<!--Device-hichecker-function contains(rule: bigint): boolean--><!--Device-hichecker-function contains(rule: bigint): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rule | bigint | Yes | ��Ҫ��ѯ�Ĺ��� |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | ��ѯ�����true ��ʾ���������ӣ�false ��ʾ����δ���ӡ� |

## Examples

```TypeScript
// Add a rule.
hichecker.addRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS);

// Check whether the added rule exists in the collection of added rules.
hichecker.contains(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS); // return true;
hichecker.contains(hichecker.RULE_CAUTION_PRINT_LOG); // return false;
```

