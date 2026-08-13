# DomainPluginBindAccountFunc (System API)

```TypeScript
type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    localId: number, callback: AsyncCallback<void>) => void
```

Binds the specified domain account with an OS account.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,    localId: int, callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,    localId: int, callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |
