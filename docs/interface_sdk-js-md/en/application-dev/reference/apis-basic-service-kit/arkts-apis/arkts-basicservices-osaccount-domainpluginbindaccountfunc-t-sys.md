# DomainPluginBindAccountFunc (System API)

```TypeScript
type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    localId: int, callback: AsyncCallback<void>) => void
```

Binds the specified domain account with an OS account.

**Since:** 23

<!--Device-osAccount-type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,    localId: int, callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginBindAccountFunc = (domainAccountInfo: DomainAccountInfo,    localId: int, callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Indicates the domain account information. |
| localId | int | Yes | Indicates the local ID of the OS account. <br>The value should be an integer. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for notifying the binding result. |

