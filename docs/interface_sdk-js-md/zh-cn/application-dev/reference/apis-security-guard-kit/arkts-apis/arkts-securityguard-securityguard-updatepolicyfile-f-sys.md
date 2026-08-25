# updatePolicyFile（系统接口）

## 导入模块

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## updatePolicyFile

```TypeScript
function updatePolicyFile(policyFile: PolicyFile): Promise<void>
```

更新配置文件。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_SECURITY_GUARD_CONFIG

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policyFile | [PolicyFile](arkts-securityguard-securityguard-policyfile-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
