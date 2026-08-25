# @ohos.multimodalAwareness.motion(动作感知能力)

**motion**本模块提供对用户手势识别、设备姿态监听等感知能力，适用于需要根据用户手势或动作进行响应的交互场景，如握持手、设备拾起等，帮助应用提供更自然的交互体验和精准的场景感知。

**起始版本：** 15

**系统能力：** SystemCapability.MultimodalAwareness.Motion

## 导入模块

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getRecentOperatingHandStatus(动作感知能力)](arkts-multimodalawareness-motion-getrecentoperatinghandstatus-f.md) |
| [off(动作感知能力)](arkts-multimodalawareness-motion-off-f.md#offoperatinghandchanged) |
| [off(动作感知能力)](arkts-multimodalawareness-motion-off-f.md#offholdinghandchanged) |
| [on(动作感知能力)](arkts-multimodalawareness-motion-on-f.md#onoperatinghandchanged) |
| [on(动作感知能力)](arkts-multimodalawareness-motion-on-f.md#onholdinghandchanged) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [offHoverHandChange(动作感知能力)](arkts-multimodalawareness-motion-offhoverhandchange-f-sys.md) |
| [offPickupChange(动作感知能力)](arkts-multimodalawareness-motion-offpickupchange-f-sys.md) |
| [offRotateChange(动作感知能力)](arkts-multimodalawareness-motion-offrotatechange-f-sys.md) |
| [offSmartRotateChange(动作感知能力)](arkts-multimodalawareness-motion-offsmartrotatechange-f-sys.md) |
| [onHoverHandChange(动作感知能力)](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md) |
| [onHoverHandChange(动作感知能力)](arkts-multimodalawareness-motion-onhoverhandchange-f-sys.md) |
| [onPickupChange(动作感知能力)](arkts-multimodalawareness-motion-onpickupchange-f-sys.md) |
| [onRotateChange(动作感知能力)](arkts-multimodalawareness-motion-onrotatechange-f-sys.md) |
| [onSmartRotateChange(动作感知能力)](arkts-multimodalawareness-motion-onsmartrotatechange-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [HoverHandDetectionArea(动作感知能力)](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) |
| [SmartRotateEvent(动作感知能力)](arkts-multimodalawareness-motion-smartrotateevent-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [HoldingHandStatus(动作感知能力)](arkts-multimodalawareness-motion-holdinghandstatus-e.md) |
| [OperatingHandStatus(动作感知能力)](arkts-multimodalawareness-motion-operatinghandstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [HoverHandAction(动作感知能力)](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md) |
| [LogicalOrientation(动作感知能力)](arkts-multimodalawareness-motion-logicalorientation-e-sys.md) |
| [PhysicalOrientation(动作感知能力)](arkts-multimodalawareness-motion-physicalorientation-e-sys.md) |
| [PickupEvent(动作感知能力)](arkts-multimodalawareness-motion-pickupevent-e-sys.md) |
| [RotateEvent(动作感知能力)](arkts-multimodalawareness-motion-rotateevent-e-sys.md) |
<!--DelEnd-->
