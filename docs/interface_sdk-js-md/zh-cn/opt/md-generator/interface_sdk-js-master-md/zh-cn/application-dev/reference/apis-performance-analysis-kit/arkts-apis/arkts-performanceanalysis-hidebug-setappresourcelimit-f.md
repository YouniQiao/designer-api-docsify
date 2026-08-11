# setAppResourceLimit

## setAppResourceLimit

```TypeScript
function setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void
```

����Ӧ�õ��ļ��������������߳�������JS�ڴ��Native�ڴ���Դ���ơ���ҪӦ�ó������ڹ����ڴ�й©���ϡ�

> **ע��**
> 
> �������еĿ�����ѡ����ڿ�����ѡ���б����ҵ�"ϵͳ��Դй©��־"�����ã������豸��ӿ���Ч��

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void--><!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| value | number | 是 |
| enableDebugLog | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-cpuusage统计异常) |

## 示例

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
