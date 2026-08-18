# onUserAgeGroupDetected

## 导入模块

```TypeScript
```

## onUserAgeGroupDetected

```TypeScript
function onUserAgeGroupDetected(callback: Callback<UserClassification>): void
```

订阅年龄群组检测功能。

**起始版本：** 23

**废弃版本：** 24

<!--Device-userStatus-function onUserAgeGroupDetected(callback: Callback<UserClassification>): void--><!--Device-userStatus-function onUserAgeGroupDetected(callback: Callback<UserClassification>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserClassification](arkts-multimodalawareness-userstatus-userclassification-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-服务异常) |
| [33900002](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900002-订阅失败) |
