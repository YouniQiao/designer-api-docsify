# setPowerConfig（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## setPowerConfig

```TypeScript
function setPowerConfig(sceneName: string, value: string): void
```

根据场景名称设置电源配置值。例如，在系统电源管理应用中需要动态调整特定场景的电源配置参数时使用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.POWER_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../errorcode-power.md#4900101-连接服务失败) |
| [4900400](../errorcode-power.md#4900400-接口入参无效) |
| [4900601](../errorcode-power.md#4900601-写电源配置值失败) |
