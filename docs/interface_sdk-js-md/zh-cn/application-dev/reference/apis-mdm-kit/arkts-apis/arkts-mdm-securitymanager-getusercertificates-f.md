# getUserCertificates

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## getUserCertificates

```TypeScript
function getUserCertificates(admin: Want, accountId: number): Array<string>
```

获取指定系统账户下的用户证书信息。企业可通过此接口查询设备上已安装的用户证书列表，用于证书审计、证书有效期管理等场景，确保证书管理的可追溯性。

**起始版本：** 18

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

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
