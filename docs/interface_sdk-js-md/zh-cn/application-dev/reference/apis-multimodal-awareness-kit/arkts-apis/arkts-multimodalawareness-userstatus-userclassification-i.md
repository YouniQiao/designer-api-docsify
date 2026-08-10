# UserClassification

Defines the user age group detection result.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**废弃版本：** 24

<!--Device-userStatus-export interface UserClassification--><!--Device-userStatus-export interface UserClassification-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## ageGroup

```TypeScript
ageGroup?: UserAgeGroup
```

User age group, for example, child or adult.

**类型：** [UserAgeGroup](arkts-multimodalawareness-userstatus-useragegroup-e.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**废弃版本：** 24

<!--Device-UserClassification-ageGroup?: UserAgeGroup--><!--Device-UserClassification-ageGroup?: UserAgeGroup-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

## confidence

```TypeScript
confidence?: float
```

Confidence of the detection result. The value is a floating point number ranging from 0 to 1. A larger value indicates a higher confidence.

**类型：** float

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**废弃版本：** 24

<!--Device-UserClassification-confidence?: float--><!--Device-UserClassification-confidence?: float-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

