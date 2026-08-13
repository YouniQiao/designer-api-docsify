# @ohos.multimodalAwareness.motion

The **motion** module provides the user motion awareness capabilities, including user gestures and actions.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace motion--><!--Device-unnamed-declare namespace motion-End-->

**System capability:** SystemCapability.MultimodalAwareness.Motion

## Modules to Import

```TypeScript
import { motion } from '@kit.MultimodalAwarenessKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getRecentOperatingHandStatus](arkts-multimodalawareness-motion-getrecentoperatinghandstatus-f.md#getRecentOperatingHandStatus) | Obtains the latest operating hand status. |
| [offHoldingHandChanged](arkts-multimodalawareness-motion-offholdinghandchanged-f.md#offHoldingHandChanged) | Unsubscribe from the holding hand changed event. |
| [offOperatingHandChanged](arkts-multimodalawareness-motion-offoperatinghandchanged-f.md#offOperatingHandChanged) | Unsubscribe from the operating hand changed event. |
| off_holdingHandChanged | Disables listening for holding hand status changes. |
| off_operatingHandChanged | Unsubscribes from operating hand change events. |
| [onHoldingHandChanged](arkts-multimodalawareness-motion-onholdinghandchanged-f.md#onHoldingHandChanged) | Subscribe to detect the holding hand changed event. |
| [onOperatingHandChanged](arkts-multimodalawareness-motion-onoperatinghandchanged-f.md#onOperatingHandChanged) | Subscribe to detect the operating hand changed event. |
| on_holdingHandChanged | Enables listening for holding hand status changes. |
| on_operatingHandChanged | Subscribes to operating hand change events. If the device does not support this function, error code 801 is returned. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [offHoverHandChange](arkts-multimodalawareness-motion-offhoverhandchange-f-sys.md#offHoverHandChange) | Unsubscribe to hover hand event. |
| [offPickupChange](arkts-multimodalawareness-motion-offpickupchange-f-sys.md#offPickupChange) | Unsubscribe to pick up sensor event. |
| [offRotateChange](arkts-multimodalawareness-motion-offrotatechange-f-sys.md#offRotateChange) | Unsubscribe to rotate sensor event. |
| [offSmartRotateChange](arkts-multimodalawareness-motion-offsmartrotatechange-f-sys.md#offSmartRotateChange) | Unsubscribe to smart rotate sensor event. |
| [onHoverHandChange](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md#onHoverHandChange) | Subscribes to hover hand events and immediately starts detection for five seconds. |
| [onHoverHandChange](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md#onHoverHandChange-(System-API)) | Subscribes to hover hand events and immediately starts detection. |
| [onPickupChange](arkts-multimodalawareness-motion-onpickupchange-f-sys.md#onPickupChange) | Subscribe to pick up sensor event. |
| [onRotateChange](arkts-multimodalawareness-motion-onrotatechange-f-sys.md#onRotateChange) | Subscribe to rotate sensor event. |
| [onSmartRotateChange](arkts-multimodalawareness-motion-onsmartrotatechange-f-sys.md#onSmartRotateChange) | Subscribe to smart rotate sensor event. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | The basic data structure of the hover hand detection area. |
| [SmartRotateEvent](arkts-multimodalawareness-motion-smartrotateevent-i-sys.md) | The basic data structure of the smart rotate sensor event. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md) | Represents the holding hand status. The holding hand status is returned if listening for holding hand status changes is enabled. |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) | Defines the status of the operating hand. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md) | Enum for hover hand actions. |
| [LogicalOrientation](arkts-multimodalawareness-motion-logicalorientation-e-sys.md) | Enum for logical orientation calculated by smart algorithms. |
| [PhysicalOrientation](arkts-multimodalawareness-motion-physicalorientation-e-sys.md) | Enum for physical orientation detected by the sensor. |
| [PickupEvent](arkts-multimodalawareness-motion-pickupevent-e-sys.md) | Enum for pickup event. |
| [RotateEvent](arkts-multimodalawareness-motion-rotateevent-e-sys.md) | Enum for rotate event. |
<!--DelEnd-->

