# @ohos.web.webview

This module provides the capability to manage web modules.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare namespace webview--><!--Device-unnamed-declare namespace webview-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [once](arkts-arkweb-webview-once-f.md#once) | Subscribe to a callback of a specified type of web event once. |

### Classes

| Name | Description |
| --- | --- |
| [AdsBlockManager](arkts-arkweb-webview-adsblockmanager-c.md) | This class is used to set adblock config. |
| [BackForwardCacheOptions](arkts-arkweb-webview-backforwardcacheoptions-c.md) | This class is used to set back forward cache options. |
| [BackForwardCacheSupportedFeatures](arkts-arkweb-webview-backforwardcachesupportedfeatures-c.md) | This class is used to enable back forward cache supported features. |
| [GeolocationPermissions](arkts-arkweb-webview-geolocationpermissions-c.md) | Implements a GeolocationPermissions object.  &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;You must load the Web component before calling the APIs in GeolocationPermissions.&lt;/p&gt; |
| [JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md) | The message for indicating the of result of JavaScript code execution. |
| [MediaSourceInfo](arkts-arkweb-webview-mediasourceinfo-c.md) | Implements a **MediaSourceInfo** object to provide the information about the media source.  > **NOTE：** >  > - The sample effect is subject to the actual device. |
| [NativeMediaPlayerSurfaceInfo](arkts-arkweb-webview-nativemediaplayersurfaceinfo-c.md) | Implements a **NativeMediaPlayerSurfaceInfo** object to provide the surface information used for same-layer rendering [when the application takes over the media playback of the web page](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12).  > **NOTE：** >  > - The sample effect is subject to the actual device. |
| [PdfData](arkts-arkweb-webview-pdfdata-c.md) | Defines the callback of createPdf, related to {@link createPDF} method. |
| [PrefetchOptions](arkts-arkweb-webview-prefetchoptions-c.md) | Defines the PrefetchOptions class. |
| [ProxyConfig](arkts-arkweb-webview-proxyconfig-c.md) | The ProxyConfig used by applyProxyOverride. |
| [ProxyController](arkts-arkweb-webview-proxycontroller-c.md) | This class is used for set proxy for ArkWeb. |
| [ProxyRule](arkts-arkweb-webview-proxyrule-c.md) | The ProxyRule used by insertProxyRule. |
| [UserAgentBrandVersion](arkts-arkweb-webview-useragentbrandversion-c.md) | Class that holds brand name, major version and full version. Brand name and major version used to generated User-Agent client hints sec-cu-ua. Brand name and full version used to generated user-agent client hint sec-ch-ua-full-version-list. |
| [UserAgentMetadata](arkts-arkweb-webview-useragentmetadata-c.md) | Holds User-Agent metadata information and uses to generate User-Agent client hints. |
| [WebCookieManager](arkts-arkweb-webview-webcookiemanager-c.md) | Provides methods for managing the web cookies. |
| [WebDataBase](arkts-arkweb-webview-webdatabase-c.md) | Implements a **WebDataBase** object.  > **NOTE：** >  > - The sample effect is subject to the actual device. >  > - You must load the **Web** component before calling the APIs in **WebDataBase**. |
| [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md) | The download state is notified through this delegate. |
| [WebDownloadItem](arkts-arkweb-webview-webdownloaditem-c.md) | Represents a download task, You can use this object to operate the corresponding download task. |
| [WebDownloadManager](arkts-arkweb-webview-webdownloadmanager-c.md) | You can trigger download manually through this interface, or resume failed or canceled downloads. |
| [WebHttpBodyStream](arkts-arkweb-webview-webhttpbodystream-c.md) | The http body stream of the request. |
| [WebMessageExt](arkts-arkweb-webview-webmessageext-c.md) | The message received or sent from web message port. |
| [WebResourceHandler](arkts-arkweb-webview-webresourcehandler-c.md) | Used to intercept url requests. Response headers and body can be sent through WebResourceHandler. |
| [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | This class is used to intercept requests for a specified scheme. |
| [WebSchemeHandlerRequest](arkts-arkweb-webview-webschemehandlerrequest-c.md) | Defines the Web resource request used for scheme handler. |
| [WebSchemeHandlerResponse](arkts-arkweb-webview-webschemehandlerresponse-c.md) | Defines the Web resource response used for scheme handler. |
| [WebStorage](arkts-arkweb-webview-webstorage-c.md) | Implements a **WebStorage** object to manage the Web SQL database and HTML5 Web Storage APIs. All **Web**components in an application share a **WebStorage** object.  > **NOTE：** >  > - The sample effect is subject to the actual device. >  > - You must load the **Web** component before calling the APIs in **WebStorage**. >  > - After the ArkWeb kernel is upgraded to M132, the Web SQL database management becomes invalid because the > kernel discards Web SQL. For details about the ArkWeb kernel version, see > [Constraints](../../../web/web-component-overview.md#constraints). |
| [WebviewController](arkts-arkweb-webview-webviewcontroller-c.md) | WebviewController can control various behaviors of Web components(including page navigation, declaring cycle state, JavaScript interaction and so on).A WebviewController object can only control one Web component,and methods on the Webviewcontroller (except static methods) can only be called after the web component is bound to the WebviewController. |

### Interfaces

| Name | Description |
| --- | --- |
| [BackForwardList](arkts-arkweb-webview-backforwardlist-i.md) | Provides back and forward history list information method. related to {@link HistoryItem}. |
| [BlanklessFrameInterpolationInfo](arkts-arkweb-webview-blanklessframeinterpolationinfo-i.md) | Defines the frame interpolation information.  Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned. |
| [BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md) | Defines the blankless information. |
| [BlanklessLoadingParam](arkts-arkweb-webview-blanklessloadingparam-i.md) | Defines the blankless loading parameter.  Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned. |
| [CacheOptions](arkts-arkweb-webview-cacheoptions-i.md) | Options of generating code cache |
| [HistoryItem](arkts-arkweb-webview-historyitem-i.md) | Provides information for history item in BackForwardList. |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) | Provides element information of the click area. related to {@link getLastHitTest} method. |
| [MediaInfo](arkts-arkweb-webview-mediainfo-i.md) | Represents a **MediaInfo** object used as a parameter of the  [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback12)callback. The object contains information about media on the web page. The application may create, based on the information, a player that takes over media playback of the web page. |
| [NativeMediaPlayerBridge](arkts-arkweb-webview-nativemediaplayerbridge-i.md) | Implements a **CreateNativeMediaPlayerCallback** object to control the player created by the application for taking over the web page media playback. This object is a return value type of the  [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback12)callback.  > **NOTE：** >  > - The sample effect is subject to the actual device. |
| [NativeMediaPlayerHandler](arkts-arkweb-webview-nativemediaplayerhandler-i.md) | Implements a **NativeMediaPlayerHandler** object used as a parameter of the  [CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback12)callback. The application uses this object to report the player status to the ArkWeb engine.  > **NOTE：** >  > - The sample effect is subject to the actual device. |
| [OfflineResourceMap](arkts-arkweb-webview-offlineresourcemap-i.md) | Define offline resource's content and info. |
| [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | Defines the configuration of creating pdf, related to {@Link createPdf} method. |
| [RectEvent](arkts-arkweb-webview-rectevent-i.md) | Defines a rectangle. |
| [RequestInfo](arkts-arkweb-webview-requestinfo-i.md) | Defines the Web's request info. |
| [ScrollOffset](arkts-arkweb-webview-scrolloffset-i.md) | Defines the scroll offset of the webpage in view port, the unit is virtual pixel.Related to {@link getScrollOffset} method. |
| [SecurityParams](arkts-arkweb-webview-securityparams-i.md) | Defines the parameters for enableAdvancedSecurityMode. |
| [SnapshotInfo](arkts-arkweb-webview-snapshotinfo-i.md) | Defines the snapshot info. |
| [SnapshotResult](arkts-arkweb-webview-snapshotresult-i.md) | Represents a full drawing result. |
| [WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md) | Defines the configuration of web custom scheme, related to {@link customizeSchemes} method. |
| [WebHeader](arkts-arkweb-webview-webheader-i.md) | Defines the Web's request/response header. |
| [WebHttpCookie](arkts-arkweb-webview-webhttpcookie-i.md) | Defines the Web's HTTPCookie.&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;The maximum length allowed for each attribute value in a cookie string is 1024.&lt;/p&gt; |
| [WebMessagePort](arkts-arkweb-webview-webmessageport-i.md) | Define html web message port. |
| [WebStorageOrigin](arkts-arkweb-webview-webstorageorigin-i.md) | Provides usage information of the Web SQL Database. |

### Enums

| Name | Description |
| --- | --- |
| [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) | For details about the ArkWeb kernel version, see  [Adaptation Guide for the M114 Kernel on OpenHarmony 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md) |
| [BlanklessFrameInterpolationState](arkts-arkweb-webview-blanklessframeinterpolationstate-e.md) | Enumerates the frame interpolation states.  &lt;strong&gt;ArkWeb Dual Web Engine Versioning Convention&lt;/strong&gt;:&lt;p&gt;See [ArkWeb Dual Web Engine Versioning Convention] for switching between Legacy and Evergreen Web Engine.  Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned. |
| [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md) | Enum type supplied to {@link getAttachState} for indicating the attach state of controller. |
| [JsMessageType](arkts-arkweb-webview-jsmessagetype-e.md) | Enum type supplied to {@link runJavaScriptExt} for indicating the result of JavaScript code execution. |
| [MediaError](arkts-arkweb-webview-mediaerror-e.md) | Enumerates the error types of the player. |
| [MediaPlaybackState](arkts-arkweb-webview-mediaplaybackstate-e.md) | Enumerates the playback states on the current web page. |
| [MediaType](arkts-arkweb-webview-mediatype-e.md) | Enumerates the media types. |
| [NetworkState](arkts-arkweb-webview-networkstate-e.md) | Enumerates the network statuses of the player. |
| [OfflineResourceType](arkts-arkweb-webview-offlineresourcetype-e.md) | Enum type supplied to {@link OfflineResourceMap} for indicating the type of resource. |
| [PlaybackStatus](arkts-arkweb-webview-playbackstatus-e.md) | Enumerates the playback statuses of the player, which is an input parameter of the  [handleStatusChanged](../../../reference/apis-arkweb/arkts-apis-webview-NativeMediaPlayerHandler.md#handlestatuschanged12)API. |
| [Preload](arkts-arkweb-webview-preload-e.md) | Enumerates how the player preloads media data. |
| [PressureLevel](arkts-arkweb-webview-pressurelevel-e.md) | Enumerates the memory pressure levels. When an application clears the cache occupied by the **Web** component,the **Web** kernel releases the cache based on the memory pressure level. |
| [ProxySchemeFilter](arkts-arkweb-webview-proxyschemefilter-e.md) | Enum type supplied to {@link insertProxyRule} for indicating the scheme filter for proxy. |
| [ReadyState](arkts-arkweb-webview-readystate-e.md) | Enumerates the cache states of the player. |
| [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) | Defines the render process mode. |
| [ScrollType](arkts-arkweb-webview-scrolltype-e.md) | Enum type supplied to {@link setScrollable} for indicating the type of scroll. |
| [ScrollbarMode](arkts-arkweb-webview-scrollbarmode-e.md) | Enum type supplied to {@link setScrollbarMode} for indicating the web component scrollbar mode. |
| [SecureDnsMode](arkts-arkweb-webview-securednsmode-e.md) | Defines the mode for using HttpDns. |
| [SecurityLevel](arkts-arkweb-webview-securitylevel-e.md) | Defines the security level for the page. |
| [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) | Indicates the site isolation mode of the application, default value depends on different devices type. |
| [SourceType](arkts-arkweb-webview-sourcetype-e.md) | Enumerates the media source types. |
| [SuspendType](arkts-arkweb-webview-suspendtype-e.md) | Enumerates the suspension types of the player. |
| [UserAgentFormFactor](arkts-arkweb-webview-useragentformfactor-e.md) | The form factors for User-Agent metadata. |
| [WebBlanklessErrorCode](arkts-arkweb-webview-webblanklesserrorcode-e.md) | Enumerates the error codes of blankless. For details, see {@link setBlanklessLoadingWithKey} or {@link BlanklessInfo}. |
| [WebDestroyMode](arkts-arkweb-webview-webdestroymode-e.md) | Enum type supplied to {@link SetWebDestroyMode} for indicating the web component destroy mode. |
| [WebDownloadErrorCode](arkts-arkweb-webview-webdownloaderrorcode-e.md) | Defines the error code for download. |
| [WebDownloadState](arkts-arkweb-webview-webdownloadstate-e.md) | Defines the state for download. |
| [WebHitTestType](arkts-arkweb-webview-webhittesttype-e.md) | Enum type supplied to {@link getHitTest} for indicating the cursor node HitTest. |
| [WebHttpCookieSameSitePolicy](arkts-arkweb-webview-webhttpcookiesamesitepolicy-e.md) | Indicates whether to restrict cookies so that only requests sent back to the same site that created them can carry them. |
| [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md) | Enum type supplied to {@link onMessageEventExt} for indicating the type of web message. |
| [WebResourceType](arkts-arkweb-webview-webresourcetype-e.md) | Defines the resource type of request. |
| [WebSoftKeyboardBehaviorMode](arkts-arkweb-webview-websoftkeyboardbehaviormode-e.md) | Indicates the keyboard behavior mode of the web component, default value is DEFAULT. |

### Types

| Name | Description |
| --- | --- |
| [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md) | Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the  [onCreateNativeMediaPlayer](../../../reference/apis-arkweb/arkts-apis-webview-WebviewController.md#oncreatenativemediaplayer12)callback. This object is used to create a player to take over media playback of the web page. |
| [OnProxyConfigChangeCallback](arkts-arkweb-webview-onproxyconfigchangecallback-t.md) | The callback for proxy changed. |
| [OneParamFn](arkts-arkweb-webview-oneparamfn-t.md) | The function with one parameter. |
| [ResumePlayerFn](arkts-arkweb-webview-resumeplayerfn-t.md) | The function of reusme media play. |
| [SuspendPlayerFn](arkts-arkweb-webview-suspendplayerfn-t.md) | The function of suspend media play. |
| [UpdateRectFn](arkts-arkweb-webview-updaterectfn-t.md) | The function of the rect of video tag has changed. |
| [WebMessage](arkts-arkweb-webview-webmessage-t.md) | WebMessage type supplied to {@link onMessageEventExt} for indicating the type of web message. |
| [ZeroParamFn](arkts-arkweb-webview-zeroparamfn-t.md) | The function with zero parameter. |

