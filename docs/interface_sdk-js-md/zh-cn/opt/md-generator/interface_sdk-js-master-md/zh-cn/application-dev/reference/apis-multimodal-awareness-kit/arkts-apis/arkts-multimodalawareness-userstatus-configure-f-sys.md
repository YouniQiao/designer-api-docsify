# configure（系统接口）

## configure

```TypeScript
function configure(featureId: UserStatusFeature, detail: string): number
```

配置特性参数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int--><!--Device-userStatus-function configure(featureId: UserStatusFeature, detail: string): int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| featureId | [UserStatusFeature](arkts-multimodalawareness-userstatus-userstatusfeature-e-sys.md) | 是 |
| detail | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [33900001](../../apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
