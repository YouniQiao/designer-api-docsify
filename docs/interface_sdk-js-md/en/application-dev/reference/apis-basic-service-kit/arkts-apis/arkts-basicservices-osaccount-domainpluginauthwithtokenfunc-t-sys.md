# DomainPluginAuthWithTokenFunc (System API)

```TypeScript
type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,
    token: Uint8Array, callback: IUserAuthCallback) => void
```

使用授权令牌认证指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithTokenFunc = (domainAccountInfo: DomainAccountInfo,    token: Uint8Array, callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 表示域账号信息。 |
| token | Uint8Array | Yes | 表示PIN码或生物识别认证成功时生成的授权令牌。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 表示认证结果回调。 |

