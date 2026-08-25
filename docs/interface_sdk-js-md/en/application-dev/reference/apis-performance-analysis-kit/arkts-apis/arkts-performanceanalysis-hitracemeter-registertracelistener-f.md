# registerTraceListener

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## registerTraceListener

```TypeScript
function registerTraceListener(callback: TraceEventListener): number
```

Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result.After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes.Callbacks are stored in the application process. A maximum of 10 callbacks can be registered in a process.

> **NOTE：**&gt;
> If the callback contains time-consuming operations, the registration or deregistration will be blocked (waiting
> for the callback execution to complete) when the callback is executed.&gt;
> Therefore, you are advised not to register or deregister callbacks containing time-consuming operations in the
> main thread of the application to avoid application freeze.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [TraceEventListener](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
