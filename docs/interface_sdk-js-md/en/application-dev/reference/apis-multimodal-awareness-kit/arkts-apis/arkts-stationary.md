# @ohos.stationary

The **stationary** module provides APIs to report the device status, including absolute still and relative still. > **NOTE：**> > This module does not support x86 emulators.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace stationary--><!--Device-unnamed-declare namespace stationary-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

## Modules to Import

```TypeScript
import { stationary } from '@kit.MultimodalAwarenessKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off_ActivityType](arkts-multimodalawareness-stationary-offactivitytype-f.md#off_ActivityType) | Unsubscribes from the device status. |
| [on_ActivityType](arkts-multimodalawareness-stationary-onactivitytype-f.md#on_ActivityType) | Subscribes to the device status. |
| [once_ActivityType](arkts-multimodalawareness-stationary-onceactivitytype-f.md#once_ActivityType) | Obtains the device status. |

### Interfaces

| Name | Description |
| --- | --- |
| [ActivityResponse](arkts-multimodalawareness-stationary-activityresponse-i.md) | Defines the response interface to receive the device status. |

### Enums

| Name | Description |
| --- | --- |
| [ActivityEvent](arkts-multimodalawareness-stationary-activityevent-e.md) | Enumerates the device status events. |
| [ActivityState](arkts-multimodalawareness-stationary-activitystate-e.md) | Enumerates the device statuses. |

### Types

| Name | Description |
| --- | --- |
| [ActivityType](arkts-multimodalawareness-stationary-activitytype-t.md) | Enumerates the device status types. |

