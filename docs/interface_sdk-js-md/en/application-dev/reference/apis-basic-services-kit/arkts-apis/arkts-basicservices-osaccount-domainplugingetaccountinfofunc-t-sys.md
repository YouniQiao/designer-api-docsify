# DomainPluginGetAccountInfoFunc (System API)

```TypeScript
type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,
    callback: AsyncCallback<DomainAccountInfo>) => void
```

Gets the domain account information with the specified options.

**Since:** 23

<!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void--><!--Device-osAccount-type DomainPluginGetAccountInfoFunc = (options: GetDomainAccountInfoPluginOptions,    callback: AsyncCallback<DomainAccountInfo>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) | Yes | Indicates the options for getting domain account information. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | Yes | Indicates the callback for notifying the domain account information. |

