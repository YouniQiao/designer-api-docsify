# DomainPluginAuthWithPopupFunc (System API)

```TypeScript
type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,
    callback: IUserAuthCallback) => void
```

Authenticates the specified domain account with a popup.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | Indicates the domain account information for authentication. |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | Indicates the callback for notifying the authentication result. |

