# containsCheckRule

## containsCheckRule

```TypeScript
function containsCheckRule(rule: bigint) : boolean
```

��ǰ�����ӵĹ������Ƿ������ĳһ���ض��Ĺ����������Ĺ��򼶱�Ϊ�̼߳�������ڵ�ǰ�߳��н��в�ѯ��

**起始版本：** 9

<!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean--><!--Device-hichecker-function containsCheckRule(rule: bigint) : boolean-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    // 添加一条规则
    hichecker.addCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS);

    // 查询是否包含
    hichecker.containsCheckRule(hichecker.RULE_THREAD_CHECK_SLOW_PROCESS); // return true;
    hichecker.containsCheckRule(hichecker.RULE_CAUTION_PRINT_LOG); // return false;
} catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```
