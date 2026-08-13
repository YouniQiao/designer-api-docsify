# DomainPluginIsAccountTokenValidFunc (System API)

```TypeScript
type DomainPluginIsAccountTokenValidFunc = (
    domainAccountInfo: DomainAccountInfo,
    token: Uint8Array,
    callback: AsyncCallback<boolean>
  ) => void
```

Checks whether the token of specified domain account is valid.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void--><!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| token | Uint8Array | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
