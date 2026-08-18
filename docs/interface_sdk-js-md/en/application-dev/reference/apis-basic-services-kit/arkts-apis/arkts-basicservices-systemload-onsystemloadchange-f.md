# onSystemLoadChange

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## onSystemLoadChange

```TypeScript
function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void
```

Register system load callback for perception system load change

**Since:** 23

<!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | Yes | Asynchronous callback interface. |

