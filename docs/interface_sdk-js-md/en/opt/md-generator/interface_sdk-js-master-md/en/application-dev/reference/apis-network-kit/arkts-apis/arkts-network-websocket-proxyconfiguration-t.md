# ProxyConfiguration

```TypeScript
export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy
```

HTTP proxy configuration. system: means that use system proxy configuration. no-proxy: means do not use proxy. object of @type {connection.HttpProxy} means providing custom proxy settings

**Since:** 24

<!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy--><!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy-End-->

**System capability:** SystemCapability.Communication.NetStack

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| 'system' |
| 'no-proxy' |
| [HttpProxy](arkts-network-ethernet-httpproxy-t.md) |
