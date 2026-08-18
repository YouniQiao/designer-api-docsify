# @ohos.multimodalAwareness.userStatus

本模块提供用户状态感知能力，包括年龄群组检测，用户手势识别、人脸位姿识别、手眼协同检测、用户吹气状态检测、用户情绪检测、用户环境音检测等功能。 <br>适用于需要感知用户状态来优化交互体验的场景，能够帮助应用提供更自然、更个性化的用户体验。模块采用订阅/回调机制，通过底层传感器数据采集、 <br>特征提取和状态判断三个阶段实现用户状态检测，开发者可根据业务需求订阅相应的检测功能。

**起始版本：** 23

<!--Device-unnamed-declare namespace userStatus--><!--Device-unnamed-declare namespace userStatus-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [offUserAgeGroupDetected](arkts-multimodalawareness-userstatus-offuseragegroupdetected-f.md#offuseragegroupdetected) |
| [off_userAgeGroupDetected](arkts-multimodalawareness-userstatus-offuseragegroupdetected-f.md#offuseragegroupdetected) |
| [onUserAgeGroupDetected](arkts-multimodalawareness-userstatus-onuseragegroupdetected-f.md#onuseragegroupdetected) |
| [on_userAgeGroupDetected](arkts-multimodalawareness-userstatus-onuseragegroupdetected-f.md#onuseragegroupdetected) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [configure](arkts-multimodalawareness-userstatus-configure-f-sys.md#configure系统接口) |
| [queryCapabilities](arkts-multimodalawareness-userstatus-querycapabilities-f-sys.md#querycapabilities系统接口) |
| [subscribe](arkts-multimodalawareness-userstatus-subscribe-f-sys.md#subscribe系统接口) |
| [unsubscribe](arkts-multimodalawareness-userstatus-unsubscribe-f-sys.md#unsubscribe系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ComfortReminderData](arkts-multimodalawareness-userstatus-comfortreminderdata-i-sys.md) |
| [DeviceInfo](arkts-multimodalawareness-userstatus-deviceinfo-i-sys.md) |
| [UserBlowData](arkts-multimodalawareness-userstatus-userblowdata-i-sys.md) |
| [UserEmotionData](arkts-multimodalawareness-userstatus-useremotiondata-i-sys.md) |
| [UserFaceAngleData](arkts-multimodalawareness-userstatus-userfaceangledata-i-sys.md) |
| [UserFacesData](arkts-multimodalawareness-userstatus-userfacesdata-i-sys.md) |
| [UserGesturesData](arkts-multimodalawareness-userstatus-usergesturesdata-i-sys.md) |
| [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [UserAgeGroup](arkts-multimodalawareness-userstatus-useragegroup-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DeviceType](arkts-multimodalawareness-userstatus-devicetype-e-sys.md) |
| [ReminderLevel](arkts-multimodalawareness-userstatus-reminderlevel-e-sys.md) |
| [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md) |
| [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) |
<!--DelEnd-->
