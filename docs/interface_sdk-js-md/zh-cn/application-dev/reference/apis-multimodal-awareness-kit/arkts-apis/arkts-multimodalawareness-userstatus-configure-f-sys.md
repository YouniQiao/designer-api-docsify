# configure（系统接口）

## 导入模块

```TypeScript
import { userStatus } from '@kit.MultimodalAwarenessKit';
```

## configure

```TypeScript
function configure(featureId: UserStatusFeature, detail: string): number
```

配置功能参数。调用成功后，将更新指定功能的配置参数，影响后续该功能的检测行为，如检测灵敏度、采样频率、启用的检测项等。建议在subscribe()之前调用configure()配置功能参数， <br>确保配置在订阅时生效。对于需要特定配置的功能（如USER_MOOD的实时/非实时模式），建议先configure()再subscribe()。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33900001](../errorcode-userStatus.md#33900001-服务异常) |
