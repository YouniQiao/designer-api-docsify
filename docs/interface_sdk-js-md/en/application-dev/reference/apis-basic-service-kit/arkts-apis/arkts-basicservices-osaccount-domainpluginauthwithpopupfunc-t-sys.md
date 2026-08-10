# DomainPluginAuthWithPopupFunc (System API)

```TypeScript
type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,
    callback: IUserAuthCallback) => void
```

弹窗认证指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 表示域账号信息。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 表示认证结果回调。 |

