# setOtaUpdatePolicy

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setOtaUpdatePolicy

```TypeScript
function setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void
```

设置升级策略。设置成功后，系统将按照指定的策略类型进行OTA升级处理，不同策略类型对应不同的升级行为。内网升级场景下，需要先调用 [systemManager.notifyUpdatePackages](arkts-mdm-systemmanager-notifyupdatepackages-f.md)接口通知系统更新包，再调用该接口设置升级策略。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| policy | [OtaUpdatePolicy](arkts-mdm-systemmanager-otaupdatepolicy-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
