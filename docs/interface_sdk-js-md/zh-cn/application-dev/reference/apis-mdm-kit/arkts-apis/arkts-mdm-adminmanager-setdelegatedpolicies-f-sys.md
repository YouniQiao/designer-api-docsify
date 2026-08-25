# setDelegatedPolicies（系统接口）

## 导入模块

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## setDelegatedPolicies

```TypeScript
function setDelegatedPolicies(bundleName: string, accountId: number, policies: Array<string>): void
```

委托其他应用来设置设备的管控策略。被委托的其他应用需申请委托策略对应接口所需权限。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| accountId | number | 是 |
| policies | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200009](../errorcode-enterpriseDeviceManager.md#9200009-授予应用权限失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
