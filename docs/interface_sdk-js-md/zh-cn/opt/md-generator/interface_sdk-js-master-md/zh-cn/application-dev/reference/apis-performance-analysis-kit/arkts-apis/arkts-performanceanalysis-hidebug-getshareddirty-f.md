# getSharedDirty

## getSharedDirty

```TypeScript
function getSharedDirty() : bigint
```

��ȡ���̵Ĺ������ڴ��С���ӿ�ʵ�ַ�ʽ����ȡ/proc/{pid}/smaps_rollup�ڵ��е�Shared_Dirtyֵ��

> **ע��**
> 
> ����/proc/{pid}/smaps_rollup�Ķ�ȡ��ʱ�ϳ������鲻Ҫ�����߳���ʹ�øýӿڣ���ͨ��@ohos.taskpool��@ohos.worker�����첽�߳��Ա���Ӧ�ó��ֿ��١�

**起始版本：** 8

<!--Device-hidebug-function getSharedDirty() : bigint--><!--Device-hidebug-function getSharedDirty() : bigint-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| bigint |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let sharedDirty: bigint = hidebug.getSharedDirty();
console.info(`sharedDirty = ${sharedDirty}`);
```
