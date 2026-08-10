# ProxyConfiguration

```TypeScript
export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy
```

HTTP proxy configuration.system: means that use system proxy configuration.no-proxy: means do not use proxy.object of @type {connection.HttpProxy} means providing custom proxy settings

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy--><!--Device-webSocket-export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy-End-->

**系统能力：** SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'system' |  |
| 'no-proxy' |  |
| HttpProxy |  |

