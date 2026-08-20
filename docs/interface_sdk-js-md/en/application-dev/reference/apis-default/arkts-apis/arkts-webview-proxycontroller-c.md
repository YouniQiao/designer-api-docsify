# ProxyController

This class is used for set proxy for ArkWeb.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-class ProxyController--><!--Device-webview-class ProxyController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## applyProxyOverride

```TypeScript
static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void
```

Sets ProxyConfig which will be used by all Webs in the app. URLs that match patterns in the bypass list will connect the server directly. Instead, the request will use the proxy specified by the config. Requests are not guaranteed to use the new proxy immediately; wait for the listener before loading a page. This listener will be called on the UI thread. Note: calling applyProxyOverride will cause any existing system wide setting to be ignored.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ProxyController-static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void--><!--Device-ProxyController-static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxyConfig | [ProxyConfig](arkts-webview-proxyconfig-c.md) | Yes | The proxy config. |
| callback | [OnProxyConfigChangeCallback](arkts-webview-onproxyconfigchangecallback-t.md) | Yes | Called when the proxy has been changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

## removeProxyOverride

```TypeScript
static removeProxyOverride(callback: OnProxyConfigChangeCallback): void
```

Remove the proxy config. Requests are not guaranteed to not use the proxy; Wait for the listener before loading a page. This listener will be called on the UI thread.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ProxyController-static removeProxyOverride(callback: OnProxyConfigChangeCallback): void--><!--Device-ProxyController-static removeProxyOverride(callback: OnProxyConfigChangeCallback): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnProxyConfigChangeCallback](arkts-webview-onproxyconfigchangecallback-t.md) | Yes | Called when the proxy has been changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

