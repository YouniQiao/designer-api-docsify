# @ohos.multimodalAwareness.userStatus(用户状态感知)

本模块提供用户状态感知能力，包括年龄群组检测，用户手势识别、人脸位姿识别、手眼协同检测、用户吹气状态检测、用户情绪检测、用户环境音检测等功能。 <br>适用于需要感知用户状态来优化交互体验的场景，能够帮助应用提供更自然、更个性化的用户体验。模块采用订阅/回调机制，通过底层传感器数据采集、 <br>特征提取和状态判断三个阶段实现用户状态检测，开发者可根据业务需求订阅相应的检测功能。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

## 导入模块

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [off(用户状态感知)](arkts-multimodalawareness-userstatus-off-f.md#offuseragegroupdetected) |
| [offUserAgeGroupDetected(用户状态感知)](arkts-multimodalawareness-userstatus-offuseragegroupdetected-f.md) |
| [on(用户状态感知)](arkts-multimodalawareness-userstatus-on-f.md#onuseragegroupdetected) |
| [onUserAgeGroupDetected(用户状态感知)](arkts-multimodalawareness-userstatus-onuseragegroupdetected-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [configure(用户状态感知)](arkts-multimodalawareness-userstatus-configure-f-sys.md) |
| [queryCapabilities(用户状态感知)](arkts-multimodalawareness-userstatus-querycapabilities-f-sys.md) |
| [subscribe(用户状态感知)](arkts-multimodalawareness-userstatus-subscribe-f-sys.md) |
| [unsubscribe(用户状态感知)](arkts-multimodalawareness-userstatus-unsubscribe-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [UserClassification(用户状态感知)](arkts-multimodalawareness-userstatus-userclassification-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ComfortReminderData(用户状态感知)](arkts-multimodalawareness-userstatus-comfortreminderdata-i-sys.md) |
| [DeviceInfo(用户状态感知)](arkts-multimodalawareness-userstatus-deviceinfo-i-sys.md) |
| [UserBlowData(用户状态感知)](arkts-multimodalawareness-userstatus-userblowdata-i-sys.md) |
| [UserEmotionData(用户状态感知)](arkts-multimodalawareness-userstatus-useremotiondata-i-sys.md) |
| [UserFaceAngleData(用户状态感知)](arkts-multimodalawareness-userstatus-userfaceangledata-i-sys.md) |
| [UserFacesData(用户状态感知)](arkts-multimodalawareness-userstatus-userfacesdata-i-sys.md) |
| [UserGesturesData(用户状态感知)](arkts-multimodalawareness-userstatus-usergesturesdata-i-sys.md) |
| [UserStatusData(用户状态感知)](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [UserAgeGroup(用户状态感知)](arkts-multimodalawareness-userstatus-useragegroup-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DeviceType(用户状态感知)](arkts-multimodalawareness-userstatus-devicetype-e-sys.md) |
| [ReminderLevel(用户状态感知)](arkts-multimodalawareness-userstatus-reminderlevel-e-sys.md) |
| [UserStatusAtomicCap(用户状态感知)](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md) |
| [UserStatusFeature(用户状态感知)](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) |
<!--DelEnd-->
