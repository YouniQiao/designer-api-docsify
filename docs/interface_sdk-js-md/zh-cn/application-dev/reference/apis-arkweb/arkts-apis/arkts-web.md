# web

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [Web](arkts-arkweb-web-web-f.md#web) | Defines Web Component. |

### 类

| 名称 | 说明 |
| --- | --- |
| [ClientAuthenticationHandler](arkts-arkweb-web-clientauthenticationhandler-c.md) | Defines the client certificate request result, related to {@link onClientAuthenticationRequest} method. |
| [ConsoleMessage](arkts-arkweb-web-consolemessage-c.md) | Encompassed message information as parameters to {@link onConsole} method. |
| [ControllerHandler](arkts-arkweb-web-controllerhandler-c.md) | Defines the onWindowNew callback, related to {@link onWindowNew} method. |
| [DataResubmissionHandler](arkts-arkweb-web-dataresubmissionhandler-c.md) | Defines the onDataResubmission callback, related to {@link onDataResubmission} method. |
| [EventResult](arkts-arkweb-web-eventresult-c.md) | Represents the event consumption result sent to the Web component.For details about the supported events, see TouchEvent/MouseEvent.If the application does not consume the event, set this parameter to false,and the event will be consumed by the Web component. If the application has consumed the event,set this parameter to true, and the event will not be consumed by the Web component. |
| [FileSelectorParam](arkts-arkweb-web-fileselectorparam-c.md) | Encompassed message information as parameters to {@link onFileSelectorShow} method. |
| [FileSelectorResult](arkts-arkweb-web-fileselectorresult-c.md) | Defines the file selector result, related to {@link onFileSelectorShow} method. |
| [FullScreenExitHandler](arkts-arkweb-web-fullscreenexithandler-c.md) | Define the handler to exit the full screen mode, related to the {@link onFullScreenEnter} event. |
| [HttpAuthHandler](arkts-arkweb-web-httpauthhandler-c.md) | Defines the http auth request result, related to {@link onHttpAuthRequest} method. |
| [JsGeolocation](arkts-arkweb-web-jsgeolocation-c.md) | Defines the js geolocation request. |
| [JsResult](arkts-arkweb-web-jsresult-c.md) | Defines the js result. |
| [PermissionRequest](arkts-arkweb-web-permissionrequest-c.md) | 权限请求。 |
| [ScreenCaptureHandler](arkts-arkweb-web-screencapturehandler-c.md) | Defines the onScreenCapture callback, related to {@link onScreenCapture} method. |
| [SslErrorHandler](arkts-arkweb-web-sslerrorhandler-c.md) | Defines the ssl error request result, related to {@link onSslErrorEventReceive} method. |
| [VerifyPinHandler](arkts-arkweb-web-verifypinhandler-c.md) | Handle the result of PIN verification. |
| [WebContextMenuParam](arkts-arkweb-web-webcontextmenuparam-c.md) | Defines the context menu param, related to {@link WebContextMenuParam} method. |
| [WebContextMenuResult](arkts-arkweb-web-webcontextmenuresult-c.md) | Defines the context menu result, related to {@link WebContextMenuResult} method. |
| [WebKeyboardController](arkts-arkweb-web-webkeyboardcontroller-c.md) | Define the controller to interact with a custom keyboard, related to the {@link onInterceptKeyboardAttach} event. |
| [WebResourceError](arkts-arkweb-web-webresourceerror-c.md) | Defines the Web resource error. |
| [WebResourceRequest](arkts-arkweb-web-webresourcerequest-c.md) | Defines the Web resource request. |
| [WebResourceResponse](arkts-arkweb-web-webresourceresponse-c.md) | Defines the Web resource response. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AISessionEvent](arkts-arkweb-web-aisessionevent-i.md) | Custom AI session model integration for Web components.Users can define custom AI session behaviors via this interface. |
| [AcceptableFileType](arkts-arkweb-web-acceptablefiletype-i.md) | Define file selection type. |
| [AdsBlockedDetails](arkts-arkweb-web-adsblockeddetails-i.md) | Defines the ads block details. |
| [BlankScreenDetails](arkts-arkweb-web-blankscreendetails-i.md) | The details of this blank screen detection result. |
| [BlankScreenDetectionConfig](arkts-arkweb-web-blankscreendetectionconfig-i.md) | The strategy of blank screen detection. |
| [BlankScreenDetectionEventInfo](arkts-arkweb-web-blankscreendetectioneventinfo-i.md) | Defines the blank screen detection event info. |
| [CameraCaptureStateChangeInfo](arkts-arkweb-web-cameracapturestatechangeinfo-i.md) | Defines the camera capture state change info. |
| [EmbedOptions](arkts-arkweb-web-embedoptions-i.md) | Defines the Embed Options. |
| [FirstMeaningfulPaint](arkts-arkweb-web-firstmeaningfulpaint-i.md) | Provides detailed information about the first meaningful paint. |
| [FirstScreenPaint](arkts-arkweb-web-firstscreenpaint-i.md) | Defines the first screen paint info. |
| [FullScreenEnterEvent](arkts-arkweb-web-fullscreenenterevent-i.md) | Web组件进入全屏回调事件的详情。 |
| [Header](arkts-arkweb-web-header-i.md) | Defines the Web's request/response header. |
| [IntelligentTrackingPreventionDetails](arkts-arkweb-web-intelligenttrackingpreventiondetails-i.md) | Defines the Intelligent Tracking Prevention details. |
| [JavaScriptProxy](arkts-arkweb-web-javascriptproxy-i.md) | Defines the JavaScript object to be injected. |
| [LargestContentfulPaint](arkts-arkweb-web-largestcontentfulpaint-i.md) | Defines the largest content paint rendering of web page. |
| [LoadCommittedDetails](arkts-arkweb-web-loadcommitteddetails-i.md) | Defines the load committed details. |
| [MicrophoneCaptureStateChangeInfo](arkts-arkweb-web-microphonecapturestatechangeinfo-i.md) | Defines the microphone capture state change info. |
| [NativeEmbedDataInfo](arkts-arkweb-web-nativeembeddatainfo-i.md) | Provides detailed information about the changes of the same-layer tag lifecycle. |
| [NativeEmbedInfo](arkts-arkweb-web-nativeembedinfo-i.md) | Defines the embed info. |
| [NativeEmbedMouseInfo](arkts-arkweb-web-nativeembedmouseinfo-i.md) | Defines the user mouse info on embed layer. |
| [NativeEmbedParamDataInfo](arkts-arkweb-web-nativeembedparamdatainfo-i.md) | Defines the param data info. |
| [NativeEmbedParamItem](arkts-arkweb-web-nativeembedparamitem-i.md) | Defines the information of param element. |
| [NativeEmbedTouchInfo](arkts-arkweb-web-nativeembedtouchinfo-i.md) | Defines the user touch info. |
| [NativeEmbedVisibilityInfo](arkts-arkweb-web-nativeembedvisibilityinfo-i.md) | Provides visibility information about the same-layer tag. |
| [NativeMediaPlayerConfig](arkts-arkweb-web-nativemediaplayerconfig-i.md) | 用于  [开启应用接管网页媒体播放功能](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12)的配置信息。 |
| [NestedScrollOptionsExt](arkts-arkweb-web-nestedscrolloptionsext-i.md) | Define nested scroll options |
| [OnAlertEvent](arkts-arkweb-web-onalertevent-i.md) | Defines the triggered function when the web page wants to display a JavaScript alert() dialog. |
| [OnAudioStateChangedEvent](arkts-arkweb-web-onaudiostatechangedevent-i.md) | 定义网页上的音频播放状态发生改变时的回调函数。 |
| [OnBeforeUnloadEvent](arkts-arkweb-web-onbeforeunloadevent-i.md) | Defines the triggered function when the web page wants to confirm navigation from JavaScript onbeforeunload. |
| [OnClientAuthenticationEvent](arkts-arkweb-web-onclientauthenticationevent-i.md) | Defines the triggered callback when needs ssl client certificate from the user. |
| [OnConfirmEvent](arkts-arkweb-web-onconfirmevent-i.md) | Defines the triggered function when the web page wants to display a JavaScript confirm() dialog. |
| [OnConsoleEvent](arkts-arkweb-web-onconsoleevent-i.md) | Defines the triggered function when the web page receives a JavaScript console message. |
| [OnContextMenuShowEvent](arkts-arkweb-web-oncontextmenushowevent-i.md) | Defines the triggered callback when called to allow custom display of the context menu. |
| [OnDataResubmittedEvent](arkts-arkweb-web-ondataresubmittedevent-i.md) | Defines the triggered callback to decision whether resend form data or not. |
| [OnDownloadStartEvent](arkts-arkweb-web-ondownloadstartevent-i.md) | Defines the triggered function when starting to download. |
| [OnErrorReceiveEvent](arkts-arkweb-web-onerrorreceiveevent-i.md) | Defines the triggered function when the web page receives a web resource loading error. |
| [OnFaviconReceivedEvent](arkts-arkweb-web-onfaviconreceivedevent-i.md) | Defines the triggered callback when the application receive a new favicon for the current web page. |
| [OnFirstContentfulPaintEvent](arkts-arkweb-web-onfirstcontentfulpaintevent-i.md) | Defines triggered when the first content rendering of web page. |
| [OnGeolocationShowEvent](arkts-arkweb-web-ongeolocationshowevent-i.md) | Defines the triggered function when requesting to show the geolocation permission. |
| [OnHttpAuthRequestEvent](arkts-arkweb-web-onhttpauthrequestevent-i.md) | Defines the triggered when the browser needs credentials from the user. |
| [OnHttpErrorReceiveEvent](arkts-arkweb-web-onhttperrorreceiveevent-i.md) | Defines the triggered function when the web page receives a web resource loading HTTP error. |
| [OnInterceptRequestEvent](arkts-arkweb-web-oninterceptrequestevent-i.md) | Defines the triggered callback when the resources loading is intercepted. |
| [OnLoadFinishedEvent](arkts-arkweb-web-onloadfinishedevent-i.md) | Defines the triggered function at the end of web page loading. |
| [OnLoadInterceptEvent](arkts-arkweb-web-onloadinterceptevent-i.md) | Defines the triggered callback when the resources loading is intercepted. |
| [OnLoadStartedEvent](arkts-arkweb-web-onloadstartedevent-i.md) | Defines the triggered function at the begin of web page loading. |
| [OnOverScrollEvent](arkts-arkweb-web-onoverscrollevent-i.md) | Defines the function Triggered when the over scrolling. |
| [OnPageBeginEvent](arkts-arkweb-web-onpagebeginevent-i.md) | Defines the triggered function at the begin of web page loading. |
| [OnPageEndEvent](arkts-arkweb-web-onpageendevent-i.md) | Defines the triggered function at the end of web page loading. |
| [OnPageVisibleEvent](arkts-arkweb-web-onpagevisibleevent-i.md) | Defines the triggered callback when previous page will no longer be drawn and next page begin to draw. |
| [OnPdfLoadEvent](arkts-arkweb-web-onpdfloadevent-i.md) | 定义PDF加载成功或失败时触发的函数。 |
| [OnPdfScrollEvent](arkts-arkweb-web-onpdfscrollevent-i.md) | 定义PDF页面滚动到底时触发的回调函数。 |
| [OnPermissionRequestEvent](arkts-arkweb-web-onpermissionrequestevent-i.md) | 定义通知收到获取权限请求。 |
| [OnProgressChangeEvent](arkts-arkweb-web-onprogresschangeevent-i.md) | Defines the triggered function when the page loading progress changes. |
| [OnPromptEvent](arkts-arkweb-web-onpromptevent-i.md) | Defines the triggered function when the web page wants to display a JavaScript prompt() dialog. |
| [OnRefreshAccessedHistoryEvent](arkts-arkweb-web-onrefreshaccessedhistoryevent-i.md) | Defines the triggered callback when the Web page refreshes accessed history. |
| [OnRenderExitedEvent](arkts-arkweb-web-onrenderexitedevent-i.md) | Defines the triggered when the render process exits. |
| [OnResourceLoadEvent](arkts-arkweb-web-onresourceloadevent-i.md) | Defines the triggered when the url loading. |
| [OnScaleChangeEvent](arkts-arkweb-web-onscalechangeevent-i.md) | Defines the triggered when the scale of WebView changed. |
| [OnScreenCaptureRequestEvent](arkts-arkweb-web-onscreencapturerequestevent-i.md) | 定义通知收到屏幕捕获请求。 |
| [OnScrollEvent](arkts-arkweb-web-onscrollevent-i.md) | Defines function Triggered when the scroll bar slides to the specified position. |
| [OnSearchResultReceiveEvent](arkts-arkweb-web-onsearchresultreceiveevent-i.md) | Defines function Triggered when the host application call searchAllAsync. |
| [OnShowFileSelectorEvent](arkts-arkweb-web-onshowfileselectorevent-i.md) | Defines the triggered when the file selector shows. |
| [OnSslErrorEventReceiveEvent](arkts-arkweb-web-onsslerroreventreceiveevent-i.md) | Defines the triggered callback when the Web page receives an ssl Error. |
| [OnTitleReceiveEvent](arkts-arkweb-web-ontitlereceiveevent-i.md) | Defines the triggered function when the title of the main application document changes. |
| [OnTouchIconUrlReceivedEvent](arkts-arkweb-web-ontouchiconurlreceivedevent-i.md) | Defines the triggered callback when the application receive an new url of an apple-touch-icon. |
| [OnWindowNewEvent](arkts-arkweb-web-onwindownewevent-i.md) | Defines the triggered callback when web page requires the user to create a window. |
| [OnWindowNewExtEvent](arkts-arkweb-web-onwindownewextevent-i.md) | Defines the triggered callback when web page requires the user to create a window. |
| [RenderProcessNotRespondingData](arkts-arkweb-web-renderprocessnotrespondingdata-i.md) | Defines the render process not responding info. |
| [ScreenCaptureConfig](arkts-arkweb-web-screencaptureconfig-i.md) | Defines the screen capture configuration. |
| [ScriptItem](arkts-arkweb-web-scriptitem-i.md) | Defines the contents of the JavaScript to be injected. |
| [SelectionMenuOptionsExt](arkts-arkweb-web-selectionmenuoptionsext-i.md) | Defines the selection menu options. |
| [SslErrorEvent](arkts-arkweb-web-sslerrorevent-i.md) | Defines the ssl error event. |
| [UrlRegexRule](arkts-arkweb-web-urlregexrule-i.md) | Defines the regular expression rule. |
| [VerifyPinEvent](arkts-arkweb-web-verifypinevent-i.md) | Defines the event for PIN verification. |
| [WebKeyboardCallbackInfo](arkts-arkweb-web-webkeyboardcallbackinfo-i.md) | Defines the web keyboard callback info related to the {@link onInterceptKeyboardAttach} event. |
| [WebKeyboardOptions](arkts-arkweb-web-webkeyboardoptions-i.md) | Defines the web keyboard options when onInterceptKeyboardAttach event return. |
| [WebMediaOptions](arkts-arkweb-web-webmediaoptions-i.md) | Web媒体策略的配置。 |
| [WebOptions](arkts-arkweb-web-weboptions-i.md) | Defines the Web options. |
| [WindowFeatures](arkts-arkweb-web-windowfeatures-i.md) | Defines the window features info for window.open. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AISessionResultType](arkts-arkweb-web-aisessionresulttype-e.md) | Enum representing the result states for AI session operations. |
| [AISessionType](arkts-arkweb-web-aisessiontype-e.md) | Enum representing the supported types of AI sessions. |
| [AudioSessionType](arkts-arkweb-web-audiosessiontype-e.md) | 应用中Web音频类型。 |
| [BlankScreenDetectionMethod](arkts-arkweb-web-blankscreendetectionmethod-e.md) | The methods can be chosen to detect if current page is blank or nearly blank. |
| [BlurOnKeyboardHideMode](arkts-arkweb-web-bluronkeyboardhidemode-e.md) | Enum type supplied to {@link blurOnKeyboardHideMode} for setting the web blurOnKeyboardHide mode. |
| [CacheMode](arkts-arkweb-web-cachemode-e.md) | Enum type supplied to {@link cacheMode} for setting the Web cache mode. |
| [CameraCaptureState](arkts-arkweb-web-cameracapturestate-e.md) | Indicates current camera capture state of current web page. |
| [ConsoleMessageSource](arkts-arkweb-web-consolemessagesource-e.md) | The source of console message. |
| [ContextMenuDataMediaType](arkts-arkweb-web-contextmenudatamediatype-e.md) | Defines the context menu media type, related to {@link onContextMenuShow} method. |
| [ContextMenuEditStateFlags](arkts-arkweb-web-contextmenueditstateflags-e.md) | Defines the context menu supported event bit flags, related to {@link onContextMenuShow} method. |
| [ContextMenuInputFieldType](arkts-arkweb-web-contextmenuinputfieldtype-e.md) | Defines the context menu input field type, related to {@link onContextMenuShow} method. |
| [ContextMenuMediaType](arkts-arkweb-web-contextmenumediatype-e.md) | Defines the context menu media type, related to {@link onContextMenuShow} method. |
| [ContextMenuSourceType](arkts-arkweb-web-contextmenusourcetype-e.md) | Defines the context menu source type, related to {@link onContextMenuShow} method. |
| [CredentialType](arkts-arkweb-web-credentialtype-e.md) | Enum type supplied to {@link CredentialType} when ClientAuthenticationHandler#confirm being called. |
| [DetectedBlankScreenReason](arkts-arkweb-web-detectedblankscreenreason-e.md) | Enum type supplied to {@link BlankScreenDetectionEventInfo} when onDetectedBlankScreen being called. |
| [FileSelectorMode](arkts-arkweb-web-fileselectormode-e.md) | Enum type supplied to {@link FileSelectorParam} when onFileSelectorShow being called. |
| [GestureFocusMode](arkts-arkweb-web-gesturefocusmode-e.md) | Enum type supplied to {@link gestureFocusMode} for setting the web gesture focus mode. |
| [MessageLevel](arkts-arkweb-web-messagelevel-e.md) | Enum type supplied to {@link getMessageLevel} for receiving the console log level of JavaScript. |
| [MicrophoneCaptureState](arkts-arkweb-web-microphonecapturestate-e.md) | Indicates current microphone capture state of current web page. |
| [MixedMode](arkts-arkweb-web-mixedmode-e.md) | The Web's behavior to load from HTTP or HTTPS. Defaults to MixedMode.None. |
| [NativeEmbedParamStatus](arkts-arkweb-web-nativeembedparamstatus-e.md) | Enum type supplied to {@link NativeEmbedParamItem} when onNativeEmbedObjectParamChange being called. |
| [NativeEmbedStatus](arkts-arkweb-web-nativeembedstatus-e.md) | Defines the lifecycle of the same-layer tag.When the same-layer tag exists on the loaded page,CREATE is triggered. When the same-layer tag is moved or is enlarged,  **UPDATE **is triggered. When the page exits, DESTROY is triggered. |
| [NavigationPolicy](arkts-arkweb-web-navigationpolicy-e.md) | Enum type for navigationPolicy in OnWindowNewExtEvent. |
| [OverScrollMode](arkts-arkweb-web-overscrollmode-e.md) | Enum type supplied to {@link overScrollMode} for setting the web overScroll mode. |
| [PdfLoadResult](arkts-arkweb-web-pdfloadresult-e.md) | 定义PDF页面的加载结果。 |
| [PinVerifyResult](arkts-arkweb-web-pinverifyresult-e.md) | Enum type supplied to {@link PinVerifyResult} when VerifyPinHandler#confirm being called. |
| [ProtectedResourceType](arkts-arkweb-web-protectedresourcetype-e.md) | Defines the accessible resource type, related to {@link onPermissionRequest} method. |
| [RenderExitReason](arkts-arkweb-web-renderexitreason-e.md) | Enum type supplied to {@link renderExitReason} when onRenderExited being called. |
| [RenderMode](arkts-arkweb-web-rendermode-e.md) | Enumerates the rendering mode of Web components. By default, the asynchronous rendering mode is used.The asynchronous rendering mode is recommended because it has better performance and lower power consumption. |
| [RenderProcessNotRespondingReason](arkts-arkweb-web-renderprocessnotrespondingreason-e.md) | Enum type supplied to {@link RenderProcessNotRespondingData} when onRenderProcessNotResponding is called. |
| [ScrollDirectionalLockType](arkts-arkweb-web-scrolldirectionallocktype-e.md) | Enum defining the scope of directional lock behavior in the WebView, used with {@link enableScrollDirectionalLock}. |
| [ScrollbarLayoutPolicy](arkts-arkweb-web-scrollbarlayoutpolicy-e.md) | Defines the layout policy for scrollbars, used with {@link scrollbarLayoutPolicy}. |
| [SslError](arkts-arkweb-web-sslerror-e.md) | Enum type supplied to {@link error} when onSslErrorEventReceive being called. |
| [ThreatType](arkts-arkweb-web-threattype-e.md) | Enum type supplied to {@link threatType} for the website's threat type. |
| [ViewportFit](arkts-arkweb-web-viewportfit-e.md) | Defines the viewport-fit type, related to {@link ViewportFit}. |
| [WebBypassVsyncCondition](arkts-arkweb-web-webbypassvsynccondition-e.md) | Enum type supplied to {@link bypassVsyncCondition} for setting the bypass vsync condition. |
| [WebCaptureMode](arkts-arkweb-web-webcapturemode-e.md) | Web屏幕捕获模式。 |
| [WebDarkMode](arkts-arkweb-web-webdarkmode-e.md) | Enum type supplied to {@link darkMode} for setting the web dark mode. |
| [WebElementType](arkts-arkweb-web-webelementtype-e.md) | Defines Web Elements type. |
| [WebKeyboardAppearanceMode](arkts-arkweb-web-webkeyboardappearancemode-e.md) | Enum type supplied to {@link keyboardAppearance} for setting the web keyboard appearance mode. |
| [WebKeyboardAvoidMode](arkts-arkweb-web-webkeyboardavoidmode-e.md) | Enum type supplied to {@link keyboardAvoidMode} for setting the web keyboard avoid mode. |
| [WebLayoutMode](arkts-arkweb-web-weblayoutmode-e.md) | Enum type supplied to {@link layoutMode} for setting the web layout mode. |
| [WebNavigationType](arkts-arkweb-web-webnavigationtype-e.md) | Enum type supplied to {@link navigationType} for the navigation's type. |
| [WebResponseType](arkts-arkweb-web-webresponsetype-e.md) | ResponseType for contextMenu |
| [WebRotateEffect](arkts-arkweb-web-webrotateeffect-e.md) | Enum type supplied to {@link rotateRenderEffect} for setting the effect of rotation. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [MouseInfoCallback](arkts-arkweb-mouseinfocallback-t.md) | The callback when mouse event is triggered in native embed area |
| [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) | Callback type for AI session operations.Used to report the result of session creation or execution. |
| [OnAdsBlockedCallback](arkts-arkweb-onadsblockedcallback-t.md) | The callback of ads block |
| [OnCameraCaptureStateChangeCallback](arkts-arkweb-oncameracapturestatechangecallback-t.md) | The callback when camera capturing state of current page has been changed. |
| [OnContextMenuHideCallback](arkts-arkweb-oncontextmenuhidecallback-t.md) | The callback of custom hide of the context menu. |
| [OnCreateAISession](arkts-arkweb-oncreateaisession-t.md) | Triggered when an AI session is created.Allows custom model initialization and result handling.Return `true` to bypass the default system behavior;return `false` to proceed with the default logic. |
| [OnDestroyAISession](arkts-arkweb-ondestroyaisession-t.md) | Triggered when an AI session is destroyed.Used for cleaning up resources associated with custom AI models. |
| [OnDetectBlankScreenCallback](arkts-arkweb-ondetectblankscreencallback-t.md) | The callback when web engine detects current page is blank or nearly blank. |
| [OnExecuteAIAction](arkts-arkweb-onexecuteaiaction-t.md) | Triggered when executing an AI session action.Enables custom implementation of AI model execution. |
| [OnFirstMeaningfulPaintCallback](arkts-arkweb-onfirstmeaningfulpaintcallback-t.md) | The callback of firstMeaningfulPaint. |
| [OnFirstScreenPaintCallback](arkts-arkweb-onfirstscreenpaintcallback-t.md) | The callback reports the time required for the first screen painting of the current web page. |
| [OnFullScreenEnterCallback](arkts-arkweb-onfullscreenentercallback-t.md) | Web组件进入全屏时触发的回调。 |
| [OnInputmethodAttachedCallback](arkts-arkweb-oninputmethodattachedcallback-t.md) | The callback will be triggered when inputmethod is attached. |
| [OnIntelligentTrackingPreventionCallback](arkts-arkweb-onintelligenttrackingpreventioncallback-t.md) | The callback of Intelligent Tracking Prevention. |
| [OnLargestContentfulPaintCallback](arkts-arkweb-onlargestcontentfulpaintcallback-t.md) | The callback of largestContentfulPaint. |
| [OnMicrophoneCaptureStateChangeCallback](arkts-arkweb-onmicrophonecapturestatechangecallback-t.md) | The callback when microphone capturing state of current page has been changed. |
| [OnNativeEmbedObjectParamChangeCallback](arkts-arkweb-onnativeembedobjectparamchangecallback-t.md) | The callback when the param element which is a child item of the object element has changed. |
| [OnNativeEmbedVisibilityChangeCallback](arkts-arkweb-onnativeembedvisibilitychangecallback-t.md) | The callback of onNativeEmbedVisibilityChange. |
| [OnNavigationEntryCommittedCallback](arkts-arkweb-onnavigationentrycommittedcallback-t.md) | The callback of load committed. |
| [OnOverrideErrorPageCallback](arkts-arkweb-onoverrideerrorpagecallback-t.md) | The callback of onOverrideErrorPage. |
| [OnOverrideUrlLoadingCallback](arkts-arkweb-onoverrideurlloadingcallback-t.md) | The callback of onOverrideUrlLoading.Should not call WebviewController.loadUrl with the request's URL and then return true. |
| [OnRenderProcessNotRespondingCallback](arkts-arkweb-onrenderprocessnotrespondingcallback-t.md) | The callback of render process not responding. |
| [OnRenderProcessRespondingCallback](arkts-arkweb-onrenderprocessrespondingcallback-t.md) | The callback of render process responding. |
| [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) | The callback of safe browsing check. |
| [OnSslErrorEventCallback](arkts-arkweb-onsslerroreventcallback-t.md) | The callback of ssl error event. |
| [OnVerifyPinCallback](arkts-arkweb-onverifypincallback-t.md) | The callback of verify pin. |
| [OnViewportFitChangedCallback](arkts-arkweb-onviewportfitchangedcallback-t.md) | The callback of ViewportFit Changed. |
| [TextSelectionChangeCallback](arkts-arkweb-textselectionchangecallback-t.md) | Callback with the selected text after the text selection content changes. |
| [WebKeyboardCallback](arkts-arkweb-webkeyboardcallback-t.md) | The callback of onInterceptKeyboardAttach event. |
| [WebviewController](arkts-arkweb-webviewcontroller-t.md) | Provides methods for controlling the web controller. |

