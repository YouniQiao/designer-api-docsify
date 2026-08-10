# getAppVMObjectUsedSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppVMObjectUsedSize

```TypeScript
function getAppVMObjectUsedSize(): bigint
```

��ȡ��ǰ�������ArkTS������ռ�õ��ڴ��С��

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-hidebug-function getAppVMObjectUsedSize(): bigint--><!--Device-hidebug-function getAppVMObjectUsedSize(): bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | ��ǰ�������ArkTS������ռ�õ��ڴ��С����λΪKB�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`getAppVMObjectUsedSize = ${hidebug.getAppVMObjectUsedSize()}`);
```

