# setProcDumpInSharedOOM

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setProcDumpInSharedOOM

```TypeScript
function setProcDumpInSharedOOM(enable: boolean): void
```

��ת���Ķѿ������̼߳���Ϊ���̼���

> **ע��**
> 
> Ҫ��ת�����̼��Ķѿ��գ����øýӿڲ�����true������OOMʱ��������SharedHeap OOM����������ȱһ���ɡ�
> 
> �ýӿڲ�Ӱ������������ת���Ķѿ������ݡ��磺����Ӱ��dumpJsRawHeapData�Ľ����
> 
> �ýӿ���Ӧ�õ����������ڿɱ���ε��ã��������һ�ε��õ�ִ�н������Ч��

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function setProcDumpInSharedOOM(enable: boolean): void--><!--Device-hidebug-function setProcDumpInSharedOOM(enable: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | �����̷���SharedHeap OOMʱ��ϵͳ�����ݸý��������������������һ�ε��øýӿ�����¼����Ϣ��ת����Ӧ����Ķѿ��ա� true�����̼��� false���̼߳��� Ĭ��ֵ��false�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.setProcDumpInSharedOOM(true);
```

