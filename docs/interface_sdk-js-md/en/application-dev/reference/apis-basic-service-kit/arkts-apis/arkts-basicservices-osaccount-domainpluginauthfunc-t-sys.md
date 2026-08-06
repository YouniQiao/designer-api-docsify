# DomainPluginAuthFunc (System API)

```TypeScript
type DomainPluginAuthFunc = (domainAccountInfo: DomainAccountInfo,
    credential: Uint8Array, callback: IUserAuthCallback) => void
```

Authenticates the specified domain account.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginAuthFunc = (domainAccountInfo: DomainAccountInfo,    credential: Uint8Array, callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthFunc = (domainAccountInfo: DomainAccountInfo,    credential: Uint8Array, callback: IUserAuthCallback) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the domain account information for authentication.  |
| credential | Uint8Array | Yes | Indicates the credential for authentication.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the authentication callback.  |

