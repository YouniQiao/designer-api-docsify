# setOtaUpdateNonceEnable

## 导入模块

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setOtaUpdateNonceEnable

```TypeScript
function setOtaUpdateNonceEnable(admin: Want, isEnable: boolean): void
```

设置OTA更新时Nonce的启用状态（默认为启用状态）。启用后，系统将在OTA更新过程中校验Nonce的有效性，从而防止重放攻击，提升系统安全性。

> **说明：**&gt;
> 为保障系统安全，若非内网升级等特殊业务需求，不建议禁用Nonce校验。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| isEnable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) |
