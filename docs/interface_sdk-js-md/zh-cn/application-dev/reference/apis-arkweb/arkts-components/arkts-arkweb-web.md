# Web

定义 Web 组件。
<p><strong>API Note</strong>:
<strong>Performance Note</strong>: <p>For details about how to optimize the compilation, resource loading, and JSBridge performance, see Optimizing Web Page Loading <p>When the white screen duration is long due to complex web page parsing, you can enable [optimizeParserBudget](arkts-arkweb-web-attribute.md#optimizeparserbudget) to reduce the first frame rendering content.</p> </p>

## Web

```TypeScript
Web(value: WebOptions)
```

Sets Value.

> **说明：**&gt;
> - 在HTML5侧，调用console.log或console.info对应ConsoleMessage的信息级别都为MessageLevel.Info。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数:**

| 参数名 | [类型](#类型) | 必填 |
| --- | --- | --- |
| value | [WebOptions](arkts-arkweb-weboptions-i.md) | 是 |

## 汇总

### 接口

| 名称 |
| --- |

### 类型

| 名称 |
| --- |
| [MouseInfoCallback](arkts-arkweb-mouseinfocallback-t.md) |
| [OnAdsBlockedCallback](arkts-arkweb-onadsblockedcallback-t.md) |
| [OnAISessionCallback](arkts-arkweb-onaisessioncallback-t.md) |
| [OnCameraCaptureStateChangeCallback](arkts-arkweb-oncameracapturestatechangecallback-t.md) |
| [OnContextMenuHideCallback](arkts-arkweb-oncontextmenuhidecallback-t.md) |
| [OnCreateAISession](arkts-arkweb-oncreateaisession-t.md) |
| [OnDestroyAISession](arkts-arkweb-ondestroyaisession-t.md) |
| [OnDetectBlankScreenCallback](arkts-arkweb-ondetectblankscreencallback-t.md) |
| [OnExecuteAIAction](arkts-arkweb-onexecuteaiaction-t.md) |
| [OnFirstMeaningfulPaintCallback](arkts-arkweb-onfirstmeaningfulpaintcallback-t.md) |
| [OnFirstScreenPaintCallback](arkts-arkweb-onfirstscreenpaintcallback-t.md) |
| [OnFullScreenEnterCallback](arkts-arkweb-onfullscreenentercallback-t.md) |
| [OnInputmethodAttachedCallback](arkts-arkweb-oninputmethodattachedcallback-t.md) |
| [OnIntelligentTrackingPreventionCallback](arkts-arkweb-onintelligenttrackingpreventioncallback-t.md) |
| [OnLargestContentfulPaintCallback](arkts-arkweb-onlargestcontentfulpaintcallback-t.md) |
| [OnMicrophoneCaptureStateChangeCallback](arkts-arkweb-onmicrophonecapturestatechangecallback-t.md) |
| [OnNativeEmbedObjectParamChangeCallback](arkts-arkweb-onnativeembedobjectparamchangecallback-t.md) |
| [OnNativeEmbedVisibilityChangeCallback](arkts-arkweb-onnativeembedvisibilitychangecallback-t.md) |
| [OnNavigationEntryCommittedCallback](arkts-arkweb-onnavigationentrycommittedcallback-t.md) |
| [OnOverrideErrorPageCallback](arkts-arkweb-onoverrideerrorpagecallback-t.md) |
| [OnOverrideUrlLoadingCallback](arkts-arkweb-onoverrideurlloadingcallback-t.md) |
| [OnRenderProcessNotRespondingCallback](arkts-arkweb-onrenderprocessnotrespondingcallback-t.md) |
| [OnRenderProcessRespondingCallback](arkts-arkweb-onrenderprocessrespondingcallback-t.md) |
| [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) |
| [OnSslErrorEventCallback](arkts-arkweb-onsslerroreventcallback-t.md) |
| [OnVerifyPinCallback](arkts-arkweb-onverifypincallback-t.md) |
| [OnViewportFitChangedCallback](arkts-arkweb-onviewportfitchangedcallback-t.md) |
| [TextSelectionChangeCallback](arkts-arkweb-textselectionchangecallback-t.md) |
| [WebKeyboardCallback](arkts-arkweb-webkeyboardcallback-t.md) |
| [WebviewController](arkts-arkweb-webviewcontroller-t.md) |

### 枚举

| 名称 |
| --- |
