# isDebugState

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## isDebugState

```TypeScript
function isDebugState(): boolean
```

��ȡӦ�ý��̵ĵ���״̬��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-function isDebugState(): boolean--><!--Device-hidebug-function isDebugState(): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Ӧ�ý��̵�Ark���Native���Ƿ��ڵ���״̬��true�����ڵ���״̬��false��δ���ڵ���״̬�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`isDebugState = ${hidebug.isDebugState()}`)
```

