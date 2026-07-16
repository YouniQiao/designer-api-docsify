# SecureDnsMode

Defines the mode for using HttpDns.

**Since:** 10

<!--Device-webview-enum SecureDnsMode--><!--Device-webview-enum SecureDnsMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## OFF

```TypeScript
OFF = 0
```

Do not use HttpDns, can be used to revoke previously used HttpDns configuration.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecureDnsMode-OFF = 0--><!--Device-SecureDnsMode-OFF = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## AUTO

```TypeScript
AUTO = 1
```

By default, the user-settings of HttpDns is used for dns resolution, and if it fails,the system dns is used for resolution.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecureDnsMode-AUTO = 1--><!--Device-SecureDnsMode-AUTO = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SECURE_ONLY

```TypeScript
SECURE_ONLY = 2
```

Use the user-settings of HttpDns for dns resolution. If it fails, it will not fall back to the system dns, which will directly cause the page to fail to load.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SecureDnsMode-SECURE_ONLY = 2--><!--Device-SecureDnsMode-SECURE_ONLY = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

