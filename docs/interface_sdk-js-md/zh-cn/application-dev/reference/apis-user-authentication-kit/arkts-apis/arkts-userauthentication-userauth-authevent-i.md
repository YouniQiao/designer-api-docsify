# AuthEvent

认证接口的异步回调对象。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [IAuthCallback](arkts-userauthentication-userauth-iauthcallback-i.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## callback

```TypeScript
callback(result: EventInfo): void
```

通过该回调获取认证结果信息或认证过程中的提示信息。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [onResult](arkts-userauthentication-userauth-iauthcallback-i.md#onresult)(result: UserAuthResult)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [EventInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-update-eventinfo-i-sys.md) | 是 |
