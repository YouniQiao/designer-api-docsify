# enableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

Enable the GWP-ASAN grayscale of your application.

**Since:** 23

**Deprecated since:** -1

<!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void--><!--Device-hidebug-function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | No |
| duration | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [11400114](../errorcode-hiviewdfx-hidebug.md#11400114-failed-to-enable-gwpasan) |

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
