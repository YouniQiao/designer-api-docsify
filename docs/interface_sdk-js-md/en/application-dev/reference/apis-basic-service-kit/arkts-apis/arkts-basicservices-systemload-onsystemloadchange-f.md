# onSystemLoadChange

## Modules to Import

```TypeScript
import { systemLoad } from 'systemLoad';
```

## onSystemLoadChange

```TypeScript
function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void
```

Register system load callback for perception system load change

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function onSystemLoadChange(callback: Callback<SystemLoadLevel>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md)&gt; | Yes | Asynchronous callback interface. |

