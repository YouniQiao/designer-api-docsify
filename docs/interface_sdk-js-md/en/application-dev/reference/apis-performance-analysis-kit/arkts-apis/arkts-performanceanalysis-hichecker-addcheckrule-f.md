# addCheckRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## addCheckRule

```TypeScript
function addCheckRule(rule: bigint) : void
```

����һ�����������ϵͳ��ϵͳ�������ӵĹ�����м�������������Ӧ���򴥷�ʱ����hilog��grep HiChecker�鿴������Ϣ��

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hichecker-function addCheckRule(rule: bigint) : void--><!--Device-hichecker-function addCheckRule(rule: bigint) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rule | bigint | Yes | ��Ҫ���ӵĹ��� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Add a rule.
    hichecker.addCheckRule(hichecker.RULE_CAUTION_PRINT_LOG);
    // Add multiple rules.
    // hichecker.addCheckRule(
    //     hichecker.RULE_CAUTION_PRINT_LOG | hichecker.RULE_CAUTION_TRIGGER_CRASH);
} catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```

