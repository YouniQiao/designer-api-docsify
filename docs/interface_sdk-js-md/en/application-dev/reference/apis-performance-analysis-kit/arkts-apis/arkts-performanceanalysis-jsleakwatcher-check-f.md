# check

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## check

```TypeScript
function check(): string
```

��ȡ��ͨ��jsLeakWatcher.watchע�ᷢ��й©�Ķ����б�������GC��δ�����յĶ���ᱻ���Ϊй©��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function check(): string--><!--Device-jsLeakWatcher-function check(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Return value:**

| Type | Description |
| --- | --- |
| string | ����GC��δ�����յ�й©�����б��� &lt;br&gt;**˵��**��check�ɹ�������JSON��ʽ��й©�����б���checkʧ�ܣ����ؿ��ַ����� |

## Examples

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```

