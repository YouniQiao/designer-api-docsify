# shutdown（系统接口）

## 导入模块

```TypeScript
import { deviceControl } from 'kits/@kit.MDMKit';
```

## shutdown

```TypeScript
function shutdown(admin: Want): void
```

使设备关机。

**起始版本：** 11

**废弃版本：** 26.0.0

**替代接口：** [operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md)(admin: Want, operation: Operation, addition?: string)

**需要权限：** ohos.permission.ENTERPRISE_REBOOT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
