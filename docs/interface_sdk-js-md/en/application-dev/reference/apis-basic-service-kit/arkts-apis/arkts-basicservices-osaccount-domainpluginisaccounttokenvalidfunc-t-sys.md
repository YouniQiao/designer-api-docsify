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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void--><!--Device-osAccount-type DomainPluginIsAccountTokenValidFunc = (    domainAccountInfo: DomainAccountInfo,    token: Uint8Array,    callback: AsyncCallback<boolean>  ) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Indicates the domain account information. |
| token | Uint8Array | Yes | Indicates the account token. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Indicates the callback for notifying the checking result. |

