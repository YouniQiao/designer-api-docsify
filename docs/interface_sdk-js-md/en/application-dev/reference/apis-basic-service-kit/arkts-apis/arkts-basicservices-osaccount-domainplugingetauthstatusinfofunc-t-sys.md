# DomainPluginGetAuthStatusInfoFunc (System API)

```TypeScript
type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,
    callback: AsyncCallback<AuthStatusInfo>) => void
```

Gets the domain authentication property for the specified domain account.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void--><!--Device-osAccount-type DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: DomainAccountInfo,    callback: AsyncCallback<AuthStatusInfo>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the domain account information for authentication.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AuthStatusInfo&gt; | Yes | Indicates the callback for notifying the domain authentication status information.  |

