# getGlobalProxyForAccount

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getGlobalProxyForAccount

```TypeScript
function getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy
```

获取指定用户下的网络代理。适用于企业多用户环境下的网络管理场景，例如审计用户级网络代理配置、验证用户网络访问策略、排查用户网络访问问题，帮助企业检查和验证用户级网络管理策略。

> **说明：**&gt;
> 本接口用于获取通过setGlobalProxyForAccount设置的、指定用户的代理配置。如果需要获取应用于所有用户的全局代理配置，建议使用
> [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md)接口。

**起始版本：** 15

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| connection.HttpProxy |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
