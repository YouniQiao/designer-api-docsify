# @ohos.web.webview

This module provides the capability to manage web modules.

@namespace webview

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace webview--><!--Device-unnamed-declare namespace webview-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [once_string](arkts-webview-oncestring-f.md#once_string) | Subscribe to a callback of a specified type of web event once. |

### Classes

| Name | Description |
| --- | --- |
| [AdsBlockManager](arkts-webview-adsblockmanager-c.md) | This class is used to set adblock config. |
| [BackForwardCacheOptions](arkts-webview-backforwardcacheoptions-c.md) | This class is used to set back forward cache options. |
| [BackForwardCacheSupportedFeatures](arkts-webview-backforwardcachesupportedfeatures-c.md) | This class is used to enable back forward cache supported features. |
| [GeolocationPermissions](arkts-webview-geolocationpermissions-c.md) | Implements a GeolocationPermissions object. |
| [JsMessageExt](arkts-webview-jsmessageext-c.md) | The message for indicating the of result of JavaScript code execution. |
| [MediaSourceInfo](arkts-webview-mediasourceinfo-c.md) | Implements a **MediaSourceInfo** object to provide the information about the media source. |
| [NativeMediaPlayerSurfaceInfo](arkts-webview-nativemediaplayersurfaceinfo-c.md) | Implements a **NativeMediaPlayerSurfaceInfo** object to provide the surface information used for same-layer rendering [when the application takes over the media playback of the web page] (../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12). |
| [PdfData](arkts-webview-pdfdata-c.md) | Defines the callback of createPdf, related to createPDF method. |
| [PrefetchOptions](arkts-webview-prefetchoptions-c.md) | Defines the PrefetchOptions class. |
| [ProxyConfig](arkts-webview-proxyconfig-c.md) | The ProxyConfig used by applyProxyOverride. |
| [ProxyController](arkts-webview-proxycontroller-c.md) | This class is used for set proxy for ArkWeb. |
| [ProxyRule](arkts-webview-proxyrule-c.md) | The ProxyRule used by insertProxyRule. |
| [UserAgentBrandVersion](arkts-webview-useragentbrandversion-c.md) | Class that holds brand name, major version and full version. Brand name and major version used to generated User-Agent client hints sec-cu-ua. Brand name and full version used to generated user-agent client hint sec-ch-ua-full-version-list. |
| [UserAgentMetadata](arkts-webview-useragentmetadata-c.md) | Holds User-Agent metadata information and uses to generate User-Agent client hints. |
| [WebCookieManager](arkts-webview-webcookiemanager-c.md) | Provides methods for managing the web cookies. |
| [WebDataBase](arkts-webview-webdatabase-c.md) | Implements a **WebDataBase** object. |
| [WebDownloadDelegate](arkts-webview-webdownloaddelegate-c.md) | The download state is notified through this delegate. |
| [WebDownloadItem](arkts-webview-webdownloaditem-c.md) | Represents a download task, You can use this object to operate the corresponding download task. |
| [WebDownloadManager](arkts-webview-webdownloadmanager-c.md) | You can trigger download manually through this interface, or resume failed or canceled downloads. |
| [WebHttpBodyStream](arkts-webview-webhttpbodystream-c.md) | The http body stream of the request. |
| [WebMessageExt](arkts-webview-webmessageext-c.md) | The message received or sent from web message port. |
| [WebResourceHandler](arkts-webview-webresourcehandler-c.md) | Used to intercept url requests. Response headers and body can be sent through WebResourceHandler. |
| [WebSchemeHandler](arkts-webview-webschemehandler-c.md) | This class is used to intercept requests for a specified scheme. |
| [WebSchemeHandlerRequest](arkts-webview-webschemehandlerrequest-c.md) | Defines the Web resource request used for scheme handler. |
| [WebSchemeHandlerResponse](arkts-webview-webschemehandlerresponse-c.md) | Defines the Web resource response used for scheme handler. |
| [WebStorage](arkts-webview-webstorage-c.md) | Implements a **WebStorage** object to manage the Web SQL database and HTML5 Web Storage APIs. All **Web** components in an application share a **WebStorage** object. |
| [WebviewController](arkts-webview-webviewcontroller-c.md) | WebviewController can control various behaviors of Web components (including page navigation, declaring cycle state, JavaScript interaction and so on). A WebviewController object can only control one Web component, and methods on the Webviewcontroller (except static methods) can only be called after the web component is bound to the WebviewController. |

### Interfaces

| Name | Description |
| --- | --- |
| [BackForwardList](arkts-webview-backforwardlist-i.md) | Provides back and forward history list information method. related to [HistoryItem](arkts-webview-historyitem-i.md). |
| [BlanklessFrameInterpolationInfo](arkts-webview-blanklessframeinterpolationinfo-i.md) | Defines the frame interpolation information. |
| [BlanklessInfo](arkts-webview-blanklessinfo-i.md) | Defines the blankless information. |
| [BlanklessLoadingParam](arkts-webview-blanklessloadingparam-i.md) | Defines the blankless loading parameter. |
| [CacheOptions](arkts-webview-cacheoptions-i.md) | Options of generating code cache |
| [HistoryItem](arkts-webview-historyitem-i.md) | Provides information for history item in BackForwardList. |
| [HitTestValue](arkts-webview-hittestvalue-i.md) | Provides element information of the click area. related to [getLastHitTest](arkts-webview-webviewcontroller-c.md#getlasthittest) method. |
| [MediaInfo](arkts-webview-mediainfo-i.md) | Represents a **MediaInfo** object used as a parameter of the [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback) callback. The object contains information about media on the web page. The application may create, based on the information, a player that takes over media playback of the web page. |
| [NativeMediaPlayerBridge](arkts-webview-nativemediaplayerbridge-i.md) | Implements a **CreateNativeMediaPlayerCallback** object to control the player created by the application for taking over the web page media playback. This object is a return value type of the [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback) callback. |
| [NativeMediaPlayerHandler](arkts-webview-nativemediaplayerhandler-i.md) | Implements a **NativeMediaPlayerHandler** object used as a parameter of the [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback) callback. The application uses this object to report the player status to the ArkWeb engine. |
| [OfflineResourceMap](arkts-webview-offlineresourcemap-i.md) | Define offline resource's content and info. |
| [PdfConfiguration](arkts-webview-pdfconfiguration-i.md) | Defines the configuration of creating pdf, related to {@Link createPdf} method. |
| [RectEvent](arkts-webview-rectevent-i.md) | Defines a rectangle. |
| [RequestInfo](arkts-webview-requestinfo-i.md) | Defines the Web's request info. |
| [ScrollOffset](arkts-webview-scrolloffset-i.md) | Defines the scroll offset of the webpage in view port, the unit is virtual pixel. Related to [getScrollOffset](arkts-webview-webviewcontroller-c.md#getscrolloffset) method. |
| [SecurityParams](arkts-webview-securityparams-i.md) | Defines the parameters for enableAdvancedSecurityMode. |
| [SnapshotInfo](arkts-webview-snapshotinfo-i.md) | Defines the snapshot info. |
| [SnapshotResult](arkts-webview-snapshotresult-i.md) | Represents a full drawing result. |
| [WebCustomScheme](arkts-webview-webcustomscheme-i.md) | Defines the configuration of web custom scheme, related to [customizeSchemes](arkts-webview-webviewcontroller-c.md#customizeschemes) method. |
| [WebHeader](arkts-webview-webheader-i.md) | Defines the Web's request/response header. |
| [WebHttpCookie](arkts-webview-webhttpcookie-i.md) | Defines the Web's HTTPCookie. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> The maximum length allowed for each attribute value in a cookie string is 1024. </p> |
| [WebMessagePort](arkts-webview-webmessageport-i.md) | Define html web message port. |
| [WebStorageOrigin](arkts-webview-webstorageorigin-i.md) | Provides usage information of the Web SQL Database. |

### Enums

| Name | Description |
| --- | --- |
| [ArkWebEngineVersion](arkts-webview-arkwebengineversion-e.md) | For details about the ArkWeb kernel version, see [Adaptation Guide for the M114 Kernel on OpenHarmony 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md) |
| [BlanklessFrameInterpolationState](arkts-webview-blanklessframeinterpolationstate-e.md) | Enumerates the frame interpolation states. |
| [ControllerAttachState](arkts-webview-controllerattachstate-e.md) | Enum type supplied to [getAttachState](arkts-webview-webviewcontroller-c.md#getattachstate) for indicating the attach state of controller. |
| [JsMessageType](arkts-webview-jsmessagetype-e.md) | Enum type supplied to [runJavaScriptExt](arkts-webview-webviewcontroller-c.md#runjavascriptext) for indicating the result of JavaScript code execution. @enum {number} |
| [MediaError](arkts-webview-mediaerror-e.md) | Enumerates the error types of the player. |
| [MediaPlaybackState](arkts-webview-mediaplaybackstate-e.md) | Enumerates the playback states on the current web page. |
| [MediaType](arkts-webview-mediatype-e.md) | Enumerates the media types. |
| [NetworkState](arkts-webview-networkstate-e.md) | Enumerates the network statuses of the player. |
| [OfflineResourceType](arkts-webview-offlineresourcetype-e.md) | Enum type supplied to [OfflineResourceMap](arkts-webview-offlineresourcemap-i.md) for indicating the type of resource. @enum {number} |
| [PlaybackStatus](arkts-webview-playbackstatus-e.md) | Enumerates the playback statuses of the player, which is an input parameter of the [handleStatusChanged](../../../reference/apis-arkweb/arkts-apis-webview-NativeMediaPlayerHandler.md#handlestatuschanged) API. |
| [Preload](arkts-webview-preload-e.md) | Enumerates how the player preloads media data. |
| [PressureLevel](arkts-webview-pressurelevel-e.md) | Enumerates the memory pressure levels. When an application clears the cache occupied by the **Web** component, the **Web** kernel releases the cache based on the memory pressure level. |
| [ProxySchemeFilter](arkts-webview-proxyschemefilter-e.md) | Enum type supplied to [insertProxyRule](arkts-webview-proxyconfig-c.md#insertproxyrule) for indicating the scheme filter for proxy. @enum { number } |
| [ReadyState](arkts-webview-readystate-e.md) | Enumerates the cache states of the player. |
| [RenderProcessMode](arkts-webview-renderprocessmode-e.md) | Defines the render process mode. |
| [ScrollbarMode](arkts-webview-scrollbarmode-e.md) | Enum type supplied to [setScrollbarMode](arkts-webview-webviewcontroller-c.md#setscrollbarmode) for indicating the web component scrollbar mode. |
| [ScrollType](arkts-webview-scrolltype-e.md) | Enum type supplied to [setScrollable](arkts-webview-webviewcontroller-c.md#setscrollable) for indicating the type of scroll. |
| [SecureDnsMode](arkts-webview-securednsmode-e.md) | Defines the mode for using HttpDns. @enum {number} |
| [SecurityLevel](arkts-webview-securitylevel-e.md) | Defines the security level for the page. |
| [SiteIsolationMode](arkts-webview-siteisolationmode-e.md) | Indicates the site isolation mode of the application, default value depends on different devices type. @enum {number} |
| [SourceType](arkts-webview-sourcetype-e.md) | Enumerates the media source types. |
| [SuspendType](arkts-webview-suspendtype-e.md) | Enumerates the suspension types of the player. |
| [UserAgentFormFactor](arkts-webview-useragentformfactor-e.md) | The form factors for User-Agent metadata. |
| [WebBlanklessErrorCode](arkts-webview-webblanklesserrorcode-e.md) | Enumerates the error codes of blankless. For details, see [setBlanklessLoadingWithKey](arkts-webview-webviewcontroller-c.md#setblanklessloadingwithkey) or [BlanklessInfo](arkts-webview-blanklessinfo-i.md). |
| [WebDestroyMode](arkts-webview-webdestroymode-e.md) | Enum type supplied to SetWebDestroyMode for indicating the web component destroy mode. @enum { number } |
| [WebDownloadErrorCode](arkts-webview-webdownloaderrorcode-e.md) | Defines the error code for download. @enum {number} |
| [WebDownloadState](arkts-webview-webdownloadstate-e.md) | Defines the state for download. @enum {number} |
| [WebHitTestType](arkts-webview-webhittesttype-e.md) | Enum type supplied to [getHitTest](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#gethittest) for indicating the cursor node HitTest. |
| [WebHttpCookieSameSitePolicy](arkts-webview-webhttpcookiesamesitepolicy-e.md) | Indicates whether to restrict cookies so that only requests sent back to the same site that created them can carry them. |
| [WebMessageType](arkts-webview-webmessagetype-e.md) | Enum type supplied to [onMessageEventExt](arkts-webview-webmessageport-i.md#onmessageeventext) for indicating the type of web message. |
| [WebResourceType](arkts-webview-webresourcetype-e.md) | Defines the resource type of request. @enum {number} |
| [WebSoftKeyboardBehaviorMode](arkts-webview-websoftkeyboardbehaviormode-e.md) | Indicates the keyboard behavior mode of the web component, default value is DEFAULT. @enum {int} |

### Types

| Name | Description |
| --- | --- |
| [CreateNativeMediaPlayerCallback](arkts-webview-createnativemediaplayercallback-t.md) | Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the [onCreateNativeMediaPlayer](../../../reference/apis-arkweb/arkts-apis-webview-WebviewController.md#oncreatenativemediaplayer) callback. This object is used to create a player to take over media playback of the web page. |
| [OneParamFn](arkts-webview-oneparamfn-t.md) | The function with one parameter. |
| [OnProxyConfigChangeCallback](arkts-webview-onproxyconfigchangecallback-t.md) | The callback for proxy changed. |
| [ResumePlayerFn](arkts-webview-resumeplayerfn-t.md) | The function of reusme media play. |
| [SuspendPlayerFn](arkts-webview-suspendplayerfn-t.md) | The function of suspend media play. |
| [UpdateRectFn](arkts-webview-updaterectfn-t.md) | The function of the rect of video tag has changed. |
| [WebMessage](arkts-webview-webmessage-t.md) | WebMessage type supplied to [onMessageEventExt](arkts-webview-webmessageport-i.md#onmessageeventext) for indicating the type of web message. |
| [ZeroParamFn](arkts-webview-zeroparamfn-t.md) | The function with zero parameter. |

