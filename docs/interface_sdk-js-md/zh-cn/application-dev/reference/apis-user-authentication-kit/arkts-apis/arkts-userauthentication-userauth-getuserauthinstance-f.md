# getUserAuthInstance

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getUserAuthInstance

```TypeScript
function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance
```

获取[UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md)对象，执行用户身份认证，并支持使用统一用户身份认证控件。该接口用于创建一个用户认证实例，配置认证参数和界面参数后，可通过返回 的实例对象启动认证、订阅认证结果等。

> **说明：**&gt;
> 每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。认证完成后（无论成功或失败），该实例将无法再次使用。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [authParam](arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | 是 |
| [widgetParam](arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500006](../errorcode-useriam.md#12500006-认证信任等级不支持) |
