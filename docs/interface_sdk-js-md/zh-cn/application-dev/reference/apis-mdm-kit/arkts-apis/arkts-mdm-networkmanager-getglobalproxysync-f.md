# getGlobalProxySync

## 导入模块

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## getGlobalProxySync

```TypeScript
function getGlobalProxySync(admin: Want): connection.HttpProxy
```

获取网络全局代理。适用于企业网络管理场景，例如审计当前网络代理配置、验证代理策略是否生效、排查网络访问问题，帮助企业检查网络代理设置，确保网络访问策略正确执行。

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
| connection.HttpProxy |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
