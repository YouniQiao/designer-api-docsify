# IUserAuthCallback（系统接口）

表示用户认证回调类。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## onAcquireInfo

```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: Uint8Array) => void
```

身份认证信息获取回调函数。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| module | number | 是 |
| acquire | number | 是 |
| extraInfo | Uint8Array | 是 |

## onResult

```TypeScript
onResult: (result: number, extraInfo: AuthResult) => void
```

身份认证结果回调函数，返回结果码和认证结果信息。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | number | 是 |
| extraInfo | [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | 是 |
