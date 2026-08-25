# getOtaUpdatePolicy

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getOtaUpdatePolicy

```TypeScript
function getOtaUpdatePolicy(admin: Want): OtaUpdatePolicy
```

查询升级策略。适用于需要获取当前设备OTA升级策略配置的场景，用于验证策略是否正确下发，或在进行策略调整前获取当前策略配置。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [OtaUpdatePolicy](arkts-mdm-systemmanager-otaupdatepolicy-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
