# TlsOptions

```TypeScript
export type TlsOptions = 'system' | TlsConfig
```

Defines the TLS configuration.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-http-export type TlsOptions = 'system' | TlsConfig--><!--Device-http-export type TlsOptions = 'system' | TlsConfig-End-->

**System capability:** SystemCapability.Communication.NetStack

| Type | Description |
| --- | --- |
| 'system' | TLS version of the system. This field is defaulted to **system** when the value is not set. |
| TlsConfig | Custom TLS version and cipher suites. |

