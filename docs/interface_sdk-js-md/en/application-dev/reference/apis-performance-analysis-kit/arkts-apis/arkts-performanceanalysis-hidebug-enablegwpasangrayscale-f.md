# enableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void
```

Enable the GWP-ASAN grayscale of your application.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | No | The options of GWP-ASAN grayscale. |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | The duration days of GWP-ASAN grayscale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [11400114](../errorcode-hiviewdfx-hidebug.md#11400114-failed-to-enable-gwpasan) | The number of GWP-ASAN applications of this device overflowed after last boot. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: hidebug.GwpAsanOptions = {
  alwaysEnabled: true,
  sampleRate: 2500,
  maxSimutaneousAllocations: 5000,
};
let duration: number = 4;

try {
  hidebug.enableGwpAsanGrayscale(options, duration);
  console.info(`Succeeded in enabling GWP-ASan.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to enable GWP-ASan. Code: ${err.code}, message: ${err.message}`);
}
```

