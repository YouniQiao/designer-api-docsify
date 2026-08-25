# setAutoUnlockAfterReboot

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setAutoUnlockAfterReboot

```TypeScript
function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void
```

设置设备重启自动解锁，仅针对无锁屏密码设备生效。适用于企业无人值守设备或需要快速重启恢复服务的场景，避免因手动解锁导致的设备停机时间，提升设备运维效率和业务连续性。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| isAllowed | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
