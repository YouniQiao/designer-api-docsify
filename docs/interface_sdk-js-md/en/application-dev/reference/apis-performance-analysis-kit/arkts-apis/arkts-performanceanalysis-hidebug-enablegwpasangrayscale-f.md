# enableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void
```

ʹ��GWP-ASan�����ڼ����ڴ�ʹ���еķǷ���Ϊ���ýӿ���Ҫ���ڶ�̬���ò�����GWP-ASan��������Ӧ���Զ����GWP-ASan�����ԡ�������Ӧ��������������Ч��

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | No | GWP-ASan�����δ����ʱ��ʹ��Ĭ�ϲ����� |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | GWP-ASan����ʱ�䣬��λΪ�죬Ĭ��ֵΪ7���贫�����0���������� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400114 | The number of GWP-ASAN applications of this device overflowed after last boot. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function enableGwpAsanTask(): void {
  let options: hidebug.GwpAsanOptions = {
    alwaysEnabled: true,
    sampleRate: 2500,
    maxSimutaneousAllocations: 5000,
  };
  let duration: number = 4;
  hidebug.enableGwpAsanGrayscale(options, duration);
}

taskpool.execute(enableGwpAsanTask).then(() => {
  console.info(`Succeeded in enabling GWP-ASan.`);
}).catch((error: BusinessError) => {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
})
```


## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

ʹ��GWP-ASan�����ڼ����ڴ�ʹ���еķǷ���Ϊ��

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 22.

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | No | GWP-ASan�����δ����ʱ��ʹ��Ĭ�ϲ����� |
| duration | number | No | GWP-ASan����ʱ�䣬��λΪ�죬Ĭ��ֵΪ7���贫�����0���������� |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11400114 | The number of GWP-ASAN applications of this device overflowed after last boot. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function enableGwpAsanTask(): void {
  let options: hidebug.GwpAsanOptions = {
    alwaysEnabled: true,
    sampleRate: 2500,
    maxSimutaneousAllocations: 5000,
  };
  let duration: number = 4;
  hidebug.enableGwpAsanGrayscale(options, duration);
}

taskpool.execute(enableGwpAsanTask).then(() => {
  console.info(`Succeeded in enabling GWP-ASan.`);
}).catch((error: BusinessError) => {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
})
```

