# DomainPluginGetAuthStatusInfoFunc (System API)

```TypeScript
type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<AuthStatusInfo>) => void
```

Gets the domain authentication property for the specified domain account.

**Since:** 23

<!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void--><!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;AuthStatusInfo&gt; | Yes |
