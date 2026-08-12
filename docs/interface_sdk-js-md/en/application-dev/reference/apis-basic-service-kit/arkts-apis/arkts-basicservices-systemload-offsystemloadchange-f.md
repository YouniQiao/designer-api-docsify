# offSystemLoadChange

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## offSystemLoadChange

```TypeScript
function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void
```

Unregister system load callback for perception system load change

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-systemLoad-function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | No | Asynchronous callback interface. |

