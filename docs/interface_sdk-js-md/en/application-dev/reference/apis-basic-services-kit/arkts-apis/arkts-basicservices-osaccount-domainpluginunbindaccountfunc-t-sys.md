# DomainPluginUnbindAccountFunc (System API)

```TypeScript
type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<void>) => void
```

Unbind the specified domain account.

**Since:** 23

<!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Indicates the domain account information. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for notifying the unbinding result. |

