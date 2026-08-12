# unsubscribe（系统接口）

## unsubscribe

```TypeScript
function unsubscribe(featureId: UserStatusFeature, callback?: Callback<UserStatusData>): number
```

取消订阅用户状态监测。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userStatus-function unsubscribe(featureId: UserStatusFeature, callback?: Callback<UserStatusData>): int--><!--Device-userStatus-function unsubscribe(featureId: UserStatusFeature, callback?: Callback<UserStatusData>): int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [33900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-服务异常) |
| [33900003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-userStatus.md#33900003-取消订阅失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
