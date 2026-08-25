# enableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableGwpAsanGrayscale

```TypeScript
function enableGwpAsanGrayscale(options?: GwpAsanOptions, duration?: number): void
```

Enables GWP-ASan to detect illegal behaviors in heap memory usage.This API is used to dynamically configure and enable GWP-ASan to adapt to the custom GWP-ASan detection policy. The configuration takes effect after the application is restarted.

> **NOTE：**&gt;
> 1. If the number of GWP-ASan applications configured using this API exceeds the quota during device running, this
> API fails to be called and an error code is thrown. Use **try-catch** to capture exceptions to prevent the
> application from exiting abnormally.&gt;
> 2. After the device restarts, the GWP-ASan parameters set by this API are invalid.&gt;
> 3. This API involves cross-process communication and takes a number time. To avoid performance problems, you are
> advised not to call this API in the main thread. You can use [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md) or
> [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md) to enable asynchronous threads to avoid application frame freezing.

**Since:** 20

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) | No |
| duration | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [11400114](../errorcode-hiviewdfx-hidebug.md#11400114-failed-to-enable-gwp-asan) |
