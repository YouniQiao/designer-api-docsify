# removeOsAccount

## 导入模块

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## removeOsAccount

```TypeScript
function removeOsAccount(admin: Want, accountId: number): Promise<void>
```

移除系统账号。当前仅支持手机、平板设备使用，可以移除使用[createNormalOsAccount](arkts-mdm-accountmanager-createnormalosaccount-f.md)创建的普通系统账号（normal类型）和 [addOsAccountAsync](arkts-mdm-accountmanager-addosaccountasync-f.md)创建的系统账号（admin、normal、guest类型），不可移除默认系统账号（ID为100）。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) |
| [9201041](../errorcode-enterpriseDeviceManager.md#9201041-系统账号类型受限) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [204](../../errorcode-universal.md#204-用户访问控制策略拒绝此访问) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
