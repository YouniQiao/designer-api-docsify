# @ohos.resourceschedule.systemload

The **systemload** module allows the system to determine the system load level based on the current temperature, load, and scenario, and notifies registered applications of level changes, if any.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace systemLoad--><!--Device-unnamed-declare namespace systemLoad-End-->

**System capability:** SystemCapability.ResourceSchedule.SystemLoad

## Modules to Import

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getLevel](arkts-basicservices-systemload-getlevel-f.md#getLevel) | Obtains the system load level. This API uses a promise to return the result. |
| [offSystemLoadChange](arkts-basicservices-systemload-offsystemloadchange-f.md#offSystemLoadChange) | Unregister system load callback for perception system load change |
| off_systemLoadChange | Disables listening for system load level changes. This API uses an asynchronous callback to return the result. |
| [onSystemLoadChange](arkts-basicservices-systemload-onsystemloadchange-f.md#onSystemLoadChange) | Register system load callback for perception system load change |
| on_systemLoadChange | Enables listening for system load level changes. This API uses an asynchronous callback to return the result. |

### Enums

| Name | Description |
| --- | --- |
| [SystemLoadLevel](arkts-basicservices-systemload-systemloadlevel-e.md) | Enumerates system load levels. |

