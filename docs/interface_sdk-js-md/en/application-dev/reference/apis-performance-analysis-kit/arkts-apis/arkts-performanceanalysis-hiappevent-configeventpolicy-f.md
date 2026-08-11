# configEventPolicy

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## configEventPolicy

```TypeScript
function configEventPolicy(policy: EventPolicy): Promise<void>
```

Sets a system event configuration policy. This API uses a promise to return the result.

In the same lifecycle, you can set system event configuration by policy.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-hiAppEvent-function configEventPolicy(policy: EventPolicy): Promise<void>--><!--Device-hiAppEvent-function configEventPolicy(policy: EventPolicy): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [EventPolicy](arkts-performanceanalysis-hiappevent-eventpolicy-i.md) | Yes | System event configuration policy. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. &lt;br&gt;For details about the event configuration policy, see [EventPolicy]{ |

## Examples

The following example shows how to configure a policy for the MAIN_THREAD_JANK event:

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let policy: hiAppEvent.EventPolicy = {
  "mainThreadJankPolicy":{
    "logType": 1,
    "sampleInterval": 100,
    "ignoreStartupTime": 11,
    "sampleCount": 21,
    "reportTimesPerApp": 3,
    "autoStopSampling": true
  }
};
hiAppEvent.configEventPolicy(policy).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `Successfully set main thread jank event policy.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `Failed to set main thread jank event policy. Code: ${err?.code}, message: ${err?.message}`);
});
```

