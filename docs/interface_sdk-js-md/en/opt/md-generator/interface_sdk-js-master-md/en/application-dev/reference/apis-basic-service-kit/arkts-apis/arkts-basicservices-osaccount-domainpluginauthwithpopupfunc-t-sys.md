# DomainPluginAuthWithPopupFunc (System API)

```TypeScript
type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,
    callback: IUserAuthCallback) => void
```

Authenticates the specified domain account with a popup.

**Since:** 23

<!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |
