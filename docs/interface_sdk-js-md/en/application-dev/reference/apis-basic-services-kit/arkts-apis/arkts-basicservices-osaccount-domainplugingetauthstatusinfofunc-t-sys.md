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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Indicates the domain account information for authentication. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;AuthStatusInfo&gt; | Yes | Indicates the callback for notifying the domain authentication status information. |

