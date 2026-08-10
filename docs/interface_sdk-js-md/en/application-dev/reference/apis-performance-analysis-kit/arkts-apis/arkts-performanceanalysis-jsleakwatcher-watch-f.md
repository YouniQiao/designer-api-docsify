# watch

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## watch

```TypeScript
function watch(obj: object, msg: string): void
```

ע������й©�Ķ���

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function watch(obj: object, msg: string): void--><!--Device-jsLeakWatcher-function watch(obj: object, msg: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | object | Yes | ��Ҫ���Ķ���&lt;br&gt;**˵��**���ɴ����κη�null��ArkTS���󣬲�֧��undefined�ͻ������͡� |
| msg | string | Yes | �Զ��������Ϣ�� |

## Examples

```TypeScript
let obj:Object = new Object();
jsLeakWatcher.watch(obj, "Trace Object");
```

