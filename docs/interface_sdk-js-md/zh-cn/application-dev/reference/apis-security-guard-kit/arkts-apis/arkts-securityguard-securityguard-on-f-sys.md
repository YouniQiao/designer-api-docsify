# on（系统接口）

## 导入模块

```TypeScript
import { securityGuard } from 'kits/@kit.SecurityGuardKit';
```

## on('securityEventOccur')

```TypeScript
function on(type: 'securityEventOccur', securityEventInfo: SecurityEventInfo, callback: Callback<SecurityEvent>): void
```

订阅安全事件。

**起始版本：** 12

**需要权限：** ohos.permission.QUERY_SECURITY_EVENT

**系统能力：** SystemCapability.Security.SecurityGuard

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'securityEventOccur' | 是 |
| securityEventInfo | [SecurityEventInfo](arkts-securityguard-securityguard-securityeventinfo-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityEvent](arkts-securityguard-securityguard-securityevent-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
