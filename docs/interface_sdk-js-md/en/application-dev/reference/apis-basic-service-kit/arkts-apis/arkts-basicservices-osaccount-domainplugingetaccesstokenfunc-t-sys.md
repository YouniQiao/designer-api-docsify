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
| options | [GetDomainAccessTokenOptions](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Yes | Indicates the options for getting th access token. |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;Uint8Array&gt; | Yes | Indicates the callback for returning the access token. |

