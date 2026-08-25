# addOsAccountAsync

## 导入模块

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## addOsAccountAsync

```TypeScript
function addOsAccountAsync(admin: Want, name: string, type: osAccount.OsAccountType): Promise<osAccount.OsAccountInfo>
```

后台添加账号。使用Promise异步回调。适用于企业批量创建账号或远程管理场景，无需用户交互即可完成账号创建，提升管理效率。

> **说明：**&gt;
> 创建账号的流程比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| name | string | 是 |
| type | osAccount.OsAccountType | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;osAccount.OsAccountInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9201003](../errorcode-enterpriseDeviceManager.md#9201003-创建账号失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
