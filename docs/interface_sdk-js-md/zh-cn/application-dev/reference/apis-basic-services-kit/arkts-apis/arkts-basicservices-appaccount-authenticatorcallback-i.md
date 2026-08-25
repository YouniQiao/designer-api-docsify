# AuthenticatorCallback

OAuth认证器回调接口。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)

**系统能力：** SystemCapability.Account.AppAccount

## 导入模块

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

通知请求被跳转。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用[onRequestRedirected](arkts-basicservices-appaccount-authcallback-i.md#onrequestredirected)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [onRequestRedirected](arkts-basicservices-appaccount-authcallback-i.md#onrequestredirected)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onResult

```TypeScript
onResult: (code: number, result: { [key: string]: any }) => void
```

通知请求结果。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃。建议使用[onResult](arkts-basicservices-appaccount-authcallback-i.md#onresult)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [onResult](arkts-basicservices-appaccount-authcallback-i.md#onresult)

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| result | { [key: string]: any } | 是 |
