# JsGeolocation

JsGeolocation is the authorization response object provided to the app when the Web component receives a web page geolocation permission request. When a web page requests device location information through JavaScript geolocation APIs (such as navigator.geolocation), the app needs to decide whether to authorize the request. Through the invoke method, JsGeolocation allows the app to grant or deny the geolocation permission for web pages of a specified origin, and optionally save the permission decision to the system to avoid repeated authorization prompts when the same origin requests again.JsGeolocation is applicable to scenarios where web pages in the Web component actively request geolocation permission. The app must first register the [onGeolocationShow event](arkts-arkweb-web-attribute.md#ongeolocationshow). When a web page initiates a geolocation permission request, the event callback passes the JsGeolocation object to the app, and the app calls the invoke method in the callback to complete the authorization response. The "ohos.permission.LOCATION" and "ohos.permission.APPROXIMATELY_LOCATION" permissions must also be configured.

**Since:** 8

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor of JsGeolocation. The constructor itself is not directly called by the app. The JsGeolocation instance is typically obtained through the [onGeolocationShow event](arkts-arkweb-web-attribute.md#ongeolocationshow) callback.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## invoke

```TypeScript
invoke(origin: string, allow: boolean, retain: boolean): void
```

Sets the geolocation permission status of a web page. This method must be called in the [onGeolocationShow event](arkts-arkweb-web-attribute.md#ongeolocationshow) callback to respond to the authorization request from the web page that initiated the geolocation permission request.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| allow | boolean | Yes |
| retain | boolean | Yes |
