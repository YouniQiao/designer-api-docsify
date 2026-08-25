# getPasswordPolicy（系统接口）

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## getPasswordPolicy

```TypeScript
function getPasswordPolicy(): PasswordPolicy
```

获取设备锁屏口令策略。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
