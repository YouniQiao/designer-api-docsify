# DomainPluginUnbindAccountFunc (System API)

```TypeScript
type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<void>) => void
```

Unbind the specified domain account.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
