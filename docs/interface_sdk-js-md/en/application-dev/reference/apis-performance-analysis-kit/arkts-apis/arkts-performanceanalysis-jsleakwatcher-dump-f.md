# dump

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## dump

```TypeScript
function dump(filePath: string): Array<string>
```

����й©�б���������ڴ���ա�

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>--><!--Device-jsLeakWatcher-function dump(filePath: string): Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | ������Ϣ���ɵ��ļ���ŵ�·����&lt;br&gt;**˵��**����API version 24��ʼ���������������ڣ����������µ�һ�ݿ�����Ϣ�� |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | ����������ֱ�Ϊ�ļ�����׺Ϊ.jsleaklist��й©�б����ļ�����׺Ϊ.heapsnapshot������ڴ�����ļ��� &lt;br&gt;**˵��**��dump�ɹ�������й©�б��ļ�·����������ڴ����·����dumpʧ�ܣ����ؿ����顣 |

## Examples

```TypeScript
let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```

