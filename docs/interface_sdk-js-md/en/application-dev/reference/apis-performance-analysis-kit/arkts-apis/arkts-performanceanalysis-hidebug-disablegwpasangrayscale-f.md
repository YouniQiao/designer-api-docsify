# disableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## disableGwpAsanGrayscale

```TypeScript
function disableGwpAsanGrayscale(): void
```

ֹͣʹ��GWP-ASan�����øýӿڽ�ȡ���Զ������ã��ָ�Ĭ�ϲ���GwpAsanOptions��

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function disableGwpAsanGrayscale(): void--><!--Device-hidebug-function disableGwpAsanGrayscale(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
function disableGwpAsanTask(): void {
  hidebug.disableGwpAsanGrayscale();
}
taskpool.execute(disableGwpAsanTask).then(() => {
  console.info(`Disable GWP-ASan succeeded.`);
})
```

