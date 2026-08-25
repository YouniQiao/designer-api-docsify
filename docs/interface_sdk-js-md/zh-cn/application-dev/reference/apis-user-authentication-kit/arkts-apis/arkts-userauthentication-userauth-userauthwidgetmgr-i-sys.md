# UserAuthWidgetMgr（系统接口）

身份认证组件管理器。用于将自定义身份认证控件注册到UserAuthWidgetMgr中进行统一管理和调度。自定义身份认证控件可接收来自用户认证框架的命令并执行相应操作。

**起始版本：** 10

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## off('command')

```TypeScript
off(type: 'command', callback?: IAuthWidgetCallback): void
```

取消订阅来自用户认证框架的命令事件。身份认证控件通过此接口取消对用户认证框架命令的订阅。

**起始版本：** 10

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'command' | 是 |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## on('command')

```TypeScript
on(type: 'command', callback: IAuthWidgetCallback): void
```

订阅来自用户认证框架的命令事件。身份认证控件通过此接口订阅来自用户认证框架的命令，以便根据命令执行相应的认证操作。

**起始版本：** 10

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'command' | 是 |
| callback | [IAuthWidgetCallback](arkts-userauthentication-userauth-iauthwidgetcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
