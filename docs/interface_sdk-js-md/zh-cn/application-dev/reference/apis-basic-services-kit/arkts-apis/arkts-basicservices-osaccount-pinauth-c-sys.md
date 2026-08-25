# PINAuth（系统接口）

PIN码认证基类。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## constructor

```TypeScript
constructor()
```

创建PIN码认证的实例。

**起始版本：** 8

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## registerInputer

```TypeScript
registerInputer(inputer: IInputer): void
```

注册PIN码输入器。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_PIN_AUTH

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputer | [IInputer](arkts-basicservices-osaccount-iinputer-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| [12300103](../errorcode-account.md#12300103-凭据输入器已注册) |

## unregisterInputer

```TypeScript
unregisterInputer(): void
```

解注册PIN码输入器。

**起始版本：** 8

**需要权限：** ohos.permission.ACCESS_PIN_AUTH

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
