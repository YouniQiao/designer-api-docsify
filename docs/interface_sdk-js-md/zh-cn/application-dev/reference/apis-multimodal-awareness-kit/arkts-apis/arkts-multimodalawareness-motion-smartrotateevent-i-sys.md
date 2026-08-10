# SmartRotateEvent（系统接口）

The basic data structure of the smart rotate sensor event.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-motion-interface SmartRotateEvent--><!--Device-motion-interface SmartRotateEvent-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { motion } from 'kits/@kit.MultimodalAwarenessKit';
```

## logicalOrientation

```TypeScript
logicalOrientation?: LogicalOrientation
```

The logical orientation adjusted by smart algorithms.

**类型：** [LogicalOrientation](arkts-multimodalawareness-motion-logicalorientation-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SmartRotateEvent-logicalOrientation?: LogicalOrientation--><!--Device-SmartRotateEvent-logicalOrientation?: LogicalOrientation-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

## physicalOrientation

```TypeScript
physicalOrientation: PhysicalOrientation
```

The physical orientation reported by the gravity sensor.

**类型：** [PhysicalOrientation](arkts-multimodalawareness-motion-physicalorientation-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SmartRotateEvent-physicalOrientation: PhysicalOrientation--><!--Device-SmartRotateEvent-physicalOrientation: PhysicalOrientation-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

