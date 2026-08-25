# deactiveSim

## 导入模块

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## deactiveSim

```TypeScript
function deactiveSim(admin: Want, slotId: number): void
```

停用指定卡槽SIM卡。停用该SIM卡，无法使用该卡槽的SIM卡接打电话，收发短信，上网。例如，企业可在员工休假或设备维护期间，临时停用SIM卡。该接口需要插入SIM卡并关闭飞行模式才能成功调用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| slotId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9201017](../errorcode-enterpriseDeviceManager.md#9201017-启用sim或停用sim卡失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [203](../../errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
