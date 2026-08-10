# setAppResourceLimit

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setAppResourceLimit

```TypeScript
function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void
```

����Ӧ�õ��ļ��������������߳�������JS�ڴ��Native�ڴ���Դ���ơ���ҪӦ�ó������ڹ����ڴ�й©���ϡ�

> **ע��**
> 
> �������еĿ�����ѡ����ڿ�����ѡ���б����ҵ�"ϵͳ��Դй©��־"�����ã������豸��ӿ���Ч��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void--><!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | й©��Դ���ͣ������֣� - pss_memory��native�ڴ棩 - js_heap��js���ڴ棩 - fd���ļ��������� - thread���̣߳� |
| value | int | Yes | ��Ӧй©��Դ���͵����ֵ����Χ�� - pss_memory���ͣ�[1024, 4 1024 1024]����λ��KB�� - js_heap���ͣ�[85, 95]�������JS���ڴ����޵�85%~95%�� - fd���ͣ�[10, 10000] - thread���ͣ�[1, 1000]��������Χ�ᵼ�¹���ʧЧ�� |
| enableDebugLog | boolean | Yes | �Ƿ������ⲿ������־���ⲿ������־����ڻҶȰ汾����ʽ�汾����֮ǰ������һС�����û��Ƴ��Ĳ��԰汾�������ã���Ϊ�ռ�������־��ռ�ô�����cpu��Դ���ڴ���Դ�����ܻ�����Ӧ�����������⡣ true�������ⲿ������־�� false�������ⲿ������־�� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid argument, Possible causes: 1.The limit parameter is too small 2.The parameter is not in the specified type 3.The parameter type error or parameter order error |
| 11400104 | Set limit failed due to remote exception |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let type: string = 'js_heap';
let value: number = 85;
let enableDebugLog: boolean = false;
try {
  hidebug.setAppResourceLimit(type, value, enableDebugLog);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

