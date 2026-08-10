# removeRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## removeRule

```TypeScript
function removeRule(rule: bigint): void
```

> **˵����**
> 
> ��API version 8��ʼ֧�֣���API version 9��ʼ����������ʹ��[hichecker.removeCheckRule](arkts-performanceanalysis-hichecker-removecheckrule-f.md#removecheckrule)�����

ɾ��һ�����������ɾ���Ĺ��������������Ч��

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [hichecker.removeCheckRule](arkts-performanceanalysis-hichecker-removecheckrule-f.md#removecheckrule)

<!--Device-hichecker-function removeRule(rule: bigint): void--><!--Device-hichecker-function removeRule(rule: bigint): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rule | bigint | Yes | ��Ҫɾ���Ĺ��� |

## Examples

```TypeScript
// Remove a rule.
hichecker.removeRule(hichecker.RULE_CAUTION_PRINT_LOG);

// Remove multiple rules.
hichecker.removeRule(
          hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
```

