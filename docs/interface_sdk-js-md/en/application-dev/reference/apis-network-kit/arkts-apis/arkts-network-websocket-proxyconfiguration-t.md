# ProxyConfiguration

```TypeScript
export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy
```

Represents the HTTP proxy configuration.

**Since:** 23

<!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy--><!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy-End-->

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| 'system' | The default network proxy is used. |
| 'no-proxy' | No network proxy is used. |
| HttpProxy | The specified network proxy is used. |

