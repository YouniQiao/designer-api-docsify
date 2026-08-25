# getAllNetworkInterfacesSync

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getAllNetworkInterfacesSync

```TypeScript
function getAllNetworkInterfacesSync(admin: Want): Array<string>
```

获取所有激活的有线网络接口。适用于企业网络管理场景，例如查看当前设备可用的网络连接、审计网络接口状态、为后续网络配置操作做准备，帮助企业了解设备网络连接状态，便于集中管理网络资源和排查网络问题。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
