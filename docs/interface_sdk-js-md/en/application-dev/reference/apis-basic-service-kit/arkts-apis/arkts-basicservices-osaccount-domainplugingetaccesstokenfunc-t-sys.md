# DomainPluginGetAccessTokenFunc (System API)

```TypeScript
type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,
    callback: AsyncCallback<Uint8Array>) => void
```

Gets the access token based on the specified options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-osAccount-type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,    callback: AsyncCallback<Uint8Array>) => void--><!--Device-osAccount-type DomainPluginGetAccessTokenFunc = (options: GetDomainAccessTokenOptions,    callback: AsyncCallback<Uint8Array>) => void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the options for getting th access token.  |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Uint8Array&gt; | Yes | Indicates the callback for returning the access token.  |

