# stopSecurityEventCollector（系统接口）

## 导入模块

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## stopSecurityEventCollector

```TypeScript
function stopSecurityEventCollector(rule: CollectorRule): void
```

停止采集事件。

**起始版本：** 12

**需要权限：** ohos.permission.QUERY_SECURITY_EVENT

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | [CollectorRule](arkts-securityguard-securityguard-collectorrule-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
