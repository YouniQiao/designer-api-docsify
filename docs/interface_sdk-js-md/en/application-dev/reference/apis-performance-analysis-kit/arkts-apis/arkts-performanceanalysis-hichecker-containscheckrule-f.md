# containsCheckRule

## Modules to Import

```TypeScript
import { hichecker } from 'kits/@kit.PerformanceAnalysisKit';
```

## containsCheckRule

```TypeScript
function containsCheckRule(rule: bigint) : boolean
```

��ǰ�����ӵĹ������Ƿ������ĳһ���ض��Ĺ����������Ĺ��򼶱�Ϊ�̼߳�������ڵ�ǰ�߳��н��в�ѯ��

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean--><!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rule | bigint | Yes | ��Ҫ��ѯ�Ĺ��� |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | ��ѯ�����true ��ʾ���������ӣ�false ��ʾ����δ���ӡ� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

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

