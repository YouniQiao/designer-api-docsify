# DomainPluginAuthWithTokenFunc（系统接口）

```TypeScript
type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,
    token: Uint8Array, callback: IUserAuthCallback) => void
```

使用授权令牌认证指定的域账号。

**起始版本：** 23

**废弃版本：** -1

<!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| token | Uint8Array | 是 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |
