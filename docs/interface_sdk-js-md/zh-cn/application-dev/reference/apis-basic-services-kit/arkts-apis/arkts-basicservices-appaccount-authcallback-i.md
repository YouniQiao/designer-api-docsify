# AuthCallback

认证器回调类。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

## 导入模块

```TypeScript
import { appAccount } from 'kits/@kit.BasicServicesKit';
```

## onRequestContinued

```TypeScript
onRequestContinued?: () => void
```

通知请求被继续处理。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

通知请求被跳转。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onResult

```TypeScript
onResult: (code: number, result?: AuthResult) => void
```

通知请求结果。

**起始版本：** 9

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |
| result | [AuthResult](arkts-basicservices-appaccount-authresult-i.md) | 否 |
