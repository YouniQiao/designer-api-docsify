# getUserAuthWidgetMgr（系统接口）

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getUserAuthWidgetMgr

```TypeScript
function getUserAuthWidgetMgr(version: number): UserAuthWidgetMgr
```

获取身份认证组件管理器对象。用于获取UserAuthWidgetMgr实例，通过该实例可将自定义身份认证控件注册到系统进行统一管理。

> **说明：**&gt;
> 每个UserAuthWidgetMgr实例可管理一个身份认证控件，若需要管理多个控件则需获取多个实例。

**起始版本：** 10

**需要权限：** ohos.permission.SUPPORT_USER_AUTH

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| version | number | 是 |

**返回值：**

| 类型 |
| --- |
| [UserAuthWidgetMgr](arkts-userauthentication-userauth-userauthwidgetmgr-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
