# OnBeforeUnloadEvent

Defines the triggered function when the web page wants to confirm navigation from JavaScript onbeforeunload.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface OnBeforeUnloadEvent--><!--Device-unnamed-export declare interface OnBeforeUnloadEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isReload

```TypeScript
isReload?: boolean
```

The isReload parameter is set to true when the page is refreshed; otherwise, it remains false. Default is false.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OnBeforeUnloadEvent-isReload?: boolean--><!--Device-OnBeforeUnloadEvent-isReload?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## message

```TypeScript
message: string
```

The message of confirm dialog.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OnBeforeUnloadEvent-message: string--><!--Device-OnBeforeUnloadEvent-message: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## result

```TypeScript
result: JsResult
```

Handle the user's JavaScript result.

**Type:** [JsResult](arkts-web-jsresult-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OnBeforeUnloadEvent-result: JsResult--><!--Device-OnBeforeUnloadEvent-result: JsResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

The url of the page.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-OnBeforeUnloadEvent-url: string--><!--Device-OnBeforeUnloadEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

