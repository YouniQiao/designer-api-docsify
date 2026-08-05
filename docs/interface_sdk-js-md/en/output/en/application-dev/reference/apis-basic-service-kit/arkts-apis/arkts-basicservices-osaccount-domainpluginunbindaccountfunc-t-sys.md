# DomainPluginUnbindAccountFunc (System API)

```TypeScript
type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<void>) => void
```

Unbind the specified domain account.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void--><!--Device-osAccount-type DomainPluginUnbindAccountFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<void>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the domain account information.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Indicates the callback for notifying the unbinding result.  |

