# IInputData（系统接口）

密码数据回调。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## onSetData

```TypeScript
onSetData(authSubType: AuthSubType, data: Uint8Array): void
```

通知设置数据。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authSubType | [AuthSubType](arkts-basicservices-osaccount-authsubtype-e-sys.md) | 是 |
| data | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
