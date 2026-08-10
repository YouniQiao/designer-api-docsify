# @ohos.multimodalAwareness.motion

The **motion** module provides the user motion awareness capabilities, including user gestures and actions.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace motion--><!--Device-unnamed-declare namespace motion-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

## 导入模块

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getRecentOperatingHandStatus](arkts-multimodalawareness-motion-getrecentoperatinghandstatus-f.md#getrecentoperatinghandstatus) | Obtains the latest operating hand status. |
| [off](arkts-multimodalawareness-motion-off-f.md#off) | Unsubscribes from operating hand change events. |
| [off](arkts-multimodalawareness-motion-off-f.md#off-1) | Disables listening for holding hand status changes. |
| [offHoldingHandChanged](arkts-multimodalawareness-motion-offholdinghandchanged-f.md#offholdinghandchanged) | Unsubscribe from the holding hand changed event. |
| [offOperatingHandChanged](arkts-multimodalawareness-motion-offoperatinghandchanged-f.md#offoperatinghandchanged) | Unsubscribe from the operating hand changed event. |
| [on](arkts-multimodalawareness-motion-on-f.md#on) | Subscribes to operating hand change events.  If the device does not support this function, error code 801 is returned. |
| [on](arkts-multimodalawareness-motion-on-f.md#on-1) | Enables listening for holding hand status changes. |
| [onHoldingHandChanged](arkts-multimodalawareness-motion-onholdinghandchanged-f.md#onholdinghandchanged) | Subscribe to detect the holding hand changed event. |
| [onOperatingHandChanged](arkts-multimodalawareness-motion-onoperatinghandchanged-f.md#onoperatinghandchanged) | Subscribe to detect the operating hand changed event. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [offHoverHandChange](arkts-multimodalawareness-motion-offhoverhandchange-f-sys.md#offhoverhandchange) | Unsubscribe to hover hand event. |
| [offPickupChange](arkts-multimodalawareness-motion-offpickupchange-f-sys.md#offpickupchange) | Unsubscribe to pick up sensor event. |
| [offRotateChange](arkts-multimodalawareness-motion-offrotatechange-f-sys.md#offrotatechange) | Unsubscribe to rotate sensor event. |
| [offSmartRotateChange](arkts-multimodalawareness-motion-offsmartrotatechange-f-sys.md#offsmartrotatechange) | Unsubscribe to smart rotate sensor event. |
| [onHoverHandChange](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md#onhoverhandchange) | Subscribes to hover hand events and immediately starts detection for five seconds. |
| [onHoverHandChange](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md#onhoverhandchange-1) | Subscribes to hover hand events and immediately starts detection. |
| [onPickupChange](arkts-multimodalawareness-motion-onpickupchange-f-sys.md#onpickupchange) | Subscribe to pick up sensor event. |
| [onRotateChange](arkts-multimodalawareness-motion-onrotatechange-f-sys.md#onrotatechange) | Subscribe to rotate sensor event. |
| [onSmartRotateChange](arkts-multimodalawareness-motion-onsmartrotatechange-f-sys.md#onsmartrotatechange) | Subscribe to smart rotate sensor event. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | The basic data structure of the hover hand detection area. |
| [SmartRotateEvent](arkts-multimodalawareness-motion-smartrotateevent-i-sys.md) | The basic data structure of the smart rotate sensor event. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md) | Represents the holding hand status. The holding hand status is returned if listening for holding hand status changes is enabled. |
| [OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md) | Defines the status of the operating hand. |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md) | Enum for hover hand actions. |
| [LogicalOrientation](arkts-multimodalawareness-motion-logicalorientation-e-sys.md) | Enum for logical orientation calculated by smart algorithms. |
| [PhysicalOrientation](arkts-multimodalawareness-motion-physicalorientation-e-sys.md) | Enum for physical orientation detected by the sensor. |
| [PickupEvent](arkts-multimodalawareness-motion-pickupevent-e-sys.md) | Enum for pickup event. |
| [RotateEvent](arkts-multimodalawareness-motion-rotateevent-e-sys.md) | Enum for rotate event. |
<!--DelEnd-->

