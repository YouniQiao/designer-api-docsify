# getIpAddressSync

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getIpAddressSync

```TypeScript
function getIpAddressSync(admin: Want, networkInterface: string): string
```

根据网络接口获取设备IP地址。适用于企业网络管理场景，例如网络审计、设备定位、网络连接问题排查、IP地址分配管理，帮助企业IT管理员了解设备网络配置，便于网络管理和故障诊断。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| networkInterface | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
