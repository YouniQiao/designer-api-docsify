# addRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## addRule

```TypeScript
function addRule(rule: bigint): void
```

> **˵����**
> 
> ��API version 8��ʼ֧�֣���API version 9��ʼ����������ʹ��[hichecker.addCheckRule](arkts-performanceanalysis-hichecker-addcheckrule-f.md#addcheckrule)�����

����һ�����������ϵͳ��ϵͳ�������ӵĹ�����м�������

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [hichecker.addCheckRule](arkts-performanceanalysis-hichecker-addcheckrule-f.md#addcheckrule)

<!--Device-hichecker-function addRule(rule: bigint): void--><!--Device-hichecker-function addRule(rule: bigint): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rule | bigint | Yes | ��Ҫ���ӵĹ��� |

## Examples

```TypeScript
// Add a rule.
hichecker.addRule(hichecker.RULE_CAUTION_PRINT_LOG);

// Add multiple rules.
hichecker.addRule(
          hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
```

