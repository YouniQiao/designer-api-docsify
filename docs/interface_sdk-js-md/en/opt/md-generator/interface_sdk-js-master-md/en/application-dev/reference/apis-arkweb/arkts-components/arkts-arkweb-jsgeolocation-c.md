# JsGeolocation

Defines the js geolocation request.

**Since:** 8

<!--Device-unnamed-declare class JsGeolocation--><!--Device-unnamed-declare class JsGeolocation-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsGeolocation-constructor()--><!--Device-JsGeolocation-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## invoke

```TypeScript
invoke(origin: string, allow: boolean, retain: boolean): void
```

Sets the geolocation permission status of a web page.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-JsGeolocation-invoke(origin: string, allow: boolean, retain: boolean): void--><!--Device-JsGeolocation-invoke(origin: string, allow: boolean, retain: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| origin | string | Yes |
| allow | boolean | Yes |
| retain | boolean | Yes |
