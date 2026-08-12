# queryCapabilities（系统接口）

## queryCapabilities

```TypeScript
function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]
```

查询设备支持的原子能力。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]--><!--Device-userStatus-function queryCapabilities(capabilities: UserStatusAtomicCap[]): UserStatusAtomicCap[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capabilities | [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| [UserStatusAtomicCap](arkts-multimodalawareness-userstatus-userstatusatomiccap-e-sys.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [33900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-userStatus.md#33900001-服务异常) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
