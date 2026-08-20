# WebAttribute

Defines the Web attribute functions.

@extends CommonMethod&lt;WebAttribute&gt;

**Inheritance/Implementation:** WebAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface WebAttribute--><!--Device-unnamed-export declare interface WebAttribute-End-->

**System capability:** SystemCapability.Web.Webview.Core

## aiSessionOptions

```TypeScript
aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this--><!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-web-aisessionevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## allowWindowOpenMethod

```TypeScript
allowWindowOpenMethod(flag: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this--><!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flag | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WebAttribute](arkts-web-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## backToTop

```TypeScript
backToTop(backToTop: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this--><!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backToTop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## bindSelectionMenu

```TypeScript
bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this--><!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementType | [WebElementType](arkts-web-webelementtype-e.md) \| undefined | Yes |  |
| content | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | Yes |  |
| responseType | [WebResponseType](arkts-web-webresponsetype-e.md) \| undefined | Yes |  |
| options | [SelectionMenuOptionsExt](arkts-web-selectionmenuoptionsext-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## blankScreenDetectionConfig

```TypeScript
blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this--><!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-web-blankscreendetectionconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## blockNetwork

```TypeScript
blockNetwork(block: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this--><!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| block | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## blurOnKeyboardHideMode

```TypeScript
blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this--><!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-web-bluronkeyboardhidemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## bypassVsyncCondition

```TypeScript
bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this--><!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-web-webbypassvsynccondition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## cacheMode

```TypeScript
cacheMode(cacheMode: CacheMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this--><!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheMode | [CacheMode](arkts-web-cachemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## copyOptions

```TypeScript
copyOptions(value: CopyOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this--><!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## darkMode

```TypeScript
darkMode(mode: WebDarkMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this--><!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebDarkMode](arkts-web-webdarkmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this--><!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## databaseAccess

```TypeScript
databaseAccess(databaseAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this--><!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| databaseAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defaultFixedFontSize

```TypeScript
defaultFixedFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defaultFontSize

```TypeScript
defaultFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-defaultFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## defaultTextEncodingFormat

```TypeScript
defaultTextEncodingFormat(textEncodingFormat: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this--><!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textEncodingFormat | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## domStorageAccess

```TypeScript
domStorageAccess(domStorageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this--><!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domStorageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this--><!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableAutoFill

```TypeScript
enableAutoFill(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this--><!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableDefaultContextMenu

```TypeScript
enableDefaultContextMenu(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableDrag

```TypeScript
enableDrag(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableDrag(value: boolean | undefined): this--><!--Device-WebAttribute-enableDrag(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableFollowSystemFontWeight

```TypeScript
enableFollowSystemFontWeight(follow: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this--><!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| follow | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableFullscreenVideoOverlay

```TypeScript
enableFullscreenVideoOverlay(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableFullscreenVideoOverlay(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableFullscreenVideoOverlay(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableImageAnalyzer

```TypeScript
enableImageAnalyzer(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this--><!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableMediaNetworkProxy

```TypeScript
enableMediaNetworkProxy(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableMediaNetworkProxy(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableMediaNetworkProxy(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableNativeEmbedMode

```TypeScript
enableNativeEmbedMode(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableNativeMediaPlayer

```TypeScript
enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this--><!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-web-nativemediaplayerconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableScrollDirectionalLock

```TypeScript
enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this--><!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |
| type | [ScrollDirectionalLockType](arkts-web-scrolldirectionallocktype-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableWebAVSession

```TypeScript
enableWebAVSession(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## fileAccess

```TypeScript
fileAccess(fileAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this--><!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fileAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## forceDarkAccess

```TypeScript
forceDarkAccess(access: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this--><!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## forceDisplayScrollBar

```TypeScript
forceDisplayScrollBar(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this--><!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## forceEnableZoom

```TypeScript
forceEnableZoom(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this--><!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## geolocationAccess

```TypeScript
geolocationAccess(geolocationAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this--><!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| geolocationAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## gestureFocusMode

```TypeScript
gestureFocusMode(mode: GestureFocusMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this--><!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [GestureFocusMode](arkts-web-gesturefocusmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## horizontalScrollBarAccess

```TypeScript
horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontalScrollBar | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## imageAccess

```TypeScript
imageAccess(imageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this--><!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## initialScale

```TypeScript
initialScale(percent: double | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-initialScale(percent: double | undefined): this--><!--Device-WebAttribute-initialScale(percent: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| percent | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## javaScriptAccess

```TypeScript
javaScriptAccess(javaScriptAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this--><!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## javaScriptOnDocumentEnd

```TypeScript
javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## javaScriptOnDocumentStart

```TypeScript
javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## javaScriptProxy

```TypeScript
javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this--><!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptProxy | [JavaScriptProxy](arkts-web-javascriptproxy-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## keyboardAppearance

```TypeScript
keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this--><!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-web-webkeyboardappearancemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this--><!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-web-webkeyboardavoidmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## layoutMode

```TypeScript
layoutMode(mode: WebLayoutMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this--><!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebLayoutMode](arkts-web-weblayoutmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mediaOptions

```TypeScript
mediaOptions(options: WebMediaOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this--><!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WebMediaOptions](arkts-web-webmediaoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mediaPlayGestureAccess

```TypeScript
mediaPlayGestureAccess(access: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this--><!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## metaViewport

```TypeScript
metaViewport(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this--><!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## minFontSize

```TypeScript
minFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-minFontSize(size: int | undefined): this--><!--Device-WebAttribute-minFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## minLogicalFontSize

```TypeScript
minLogicalFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this--><!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mixedMode

```TypeScript
mixedMode(mixedMode: MixedMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this--><!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mixedMode | [MixedMode](arkts-web-mixedmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## multiWindowAccess

```TypeScript
multiWindowAccess(multiWindow: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this--><!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| multiWindow | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## nativeEmbedOptions

```TypeScript
nativeEmbedOptions(options?: EmbedOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this--><!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EmbedOptions](arkts-web-embedoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this--><!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-web-nestedscrolloptionsext-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onActivateContent

```TypeScript
onActivateContent(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this--><!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onAdsBlocked

```TypeScript
onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this--><!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-onadsblockedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onAlert

```TypeScript
onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this--><!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAlertEvent](arkts-web-onalertevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onAudioStateChanged

```TypeScript
onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this--><!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAudioStateChangedEvent](arkts-web-onaudiostatechangedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onBeforeUnload

```TypeScript
onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this--><!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnBeforeUnloadEvent](arkts-web-onbeforeunloadevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onCameraCaptureStateChange

```TypeScript
onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-oncameracapturestatechangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onClientAuthenticationRequest

```TypeScript
onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this--><!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnClientAuthenticationEvent](arkts-web-onclientauthenticationevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onConfirm

```TypeScript
onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConfirmEvent](arkts-web-onconfirmevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onConsole

```TypeScript
onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConsoleEvent](arkts-web-onconsoleevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onContextMenuHide

```TypeScript
onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this--><!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-oncontextmenuhidecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onContextMenuShow

```TypeScript
onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this--><!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnContextMenuShowEvent](arkts-web-oncontextmenushowevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onControllerAttached

```TypeScript
onControllerAttached(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDataResubmitted

```TypeScript
onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this--><!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDataResubmittedEvent](arkts-web-ondataresubmittedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDetectedBlankScreen

```TypeScript
onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this--><!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-ondetectblankscreencallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDownloadStart

```TypeScript
onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this--><!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDownloadStartEvent](arkts-web-ondownloadstartevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onErrorReceive

```TypeScript
onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnErrorReceiveEvent](arkts-web-onerrorreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFaviconReceived

```TypeScript
onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this--><!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFaviconReceivedEvent](arkts-web-onfaviconreceivedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFirstContentfulPaint

```TypeScript
onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this--><!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFirstContentfulPaintEvent](arkts-web-onfirstcontentfulpaintevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFirstMeaningfulPaint

```TypeScript
onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-onfirstmeaningfulpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFirstScreenPaint

```TypeScript
onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-onfirstscreenpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFullScreenEnter

```TypeScript
onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this--><!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-onfullscreenentercallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onFullScreenExit

```TypeScript
onFullScreenExit(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onGeolocationHide

```TypeScript
onGeolocationHide(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onGeolocationShow

```TypeScript
onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this--><!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnGeolocationShowEvent](arkts-web-ongeolocationshowevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onHttpAuthRequest

```TypeScript
onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this--><!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpAuthRequestEvent](arkts-web-onhttpauthrequestevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onHttpErrorReceive

```TypeScript
onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpErrorReceiveEvent](arkts-web-onhttperrorreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onInputmethodAttached

```TypeScript
onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this--><!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-oninputmethodattachedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onIntelligentTrackingPreventionResult

```TypeScript
onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this--><!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-onintelligenttrackingpreventioncallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onInterceptKeyEvent

```TypeScript
onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this--><!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: KeyEvent) =&gt; boolean) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onInterceptKeyboardAttach

```TypeScript
onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this--><!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-webkeyboardcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onInterceptRequest

```TypeScript
onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this--><!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnInterceptRequestEvent](arkts-web-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-web-webresourceresponse-c.md) \| null&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLargestContentfulPaint

```TypeScript
onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this--><!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-onlargestcontentfulpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLoadFinished

```TypeScript
onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this--><!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadFinishedEvent](arkts-web-onloadfinishedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLoadIntercept

```TypeScript
onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadInterceptEvent](arkts-web-onloadinterceptevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLoadStarted

```TypeScript
onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this--><!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadStartedEvent](arkts-web-onloadstartedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onMicrophoneCaptureStateChange

```TypeScript
onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-onmicrophonecapturestatechangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNativeEmbedGestureEvent

```TypeScript
onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedTouchInfo) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNativeEmbedLifecycleChange

```TypeScript
onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedDataInfo) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNativeEmbedMouseEvent

```TypeScript
onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MouseInfoCallback](arkts-mouseinfocallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNativeEmbedObjectParamChange

```TypeScript
onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-onnativeembedobjectparamchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNativeEmbedVisibilityChange

```TypeScript
onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-onnativeembedvisibilitychangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onNavigationEntryCommitted

```TypeScript
onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this--><!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-onnavigationentrycommittedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onOverScroll

```TypeScript
onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this--><!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnOverScrollEvent](arkts-web-onoverscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onOverrideErrorPage

```TypeScript
onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this--><!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-onoverrideerrorpagecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onOverrideUrlLoading

```TypeScript
onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this--><!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-onoverrideurlloadingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPageBegin

```TypeScript
onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this--><!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageBeginEvent](arkts-web-onpagebeginevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPageEnd

```TypeScript
onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this--><!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageEndEvent](arkts-web-onpageendevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPageVisible

```TypeScript
onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this--><!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageVisibleEvent](arkts-web-onpagevisibleevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPdfLoadEvent

```TypeScript
onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this--><!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfLoadEvent](arkts-web-onpdfloadevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPdfScrollAtBottom

```TypeScript
onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this--><!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfScrollEvent](arkts-web-onpdfscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPermissionRequest

```TypeScript
onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this--><!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPermissionRequestEvent](arkts-web-onpermissionrequestevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onProgressChange

```TypeScript
onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this--><!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnProgressChangeEvent](arkts-web-onprogresschangeevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onPrompt

```TypeScript
onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPromptEvent](arkts-web-onpromptevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRefreshAccessedHistory

```TypeScript
onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this--><!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRefreshAccessedHistoryEvent](arkts-web-onrefreshaccessedhistoryevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRenderExited

```TypeScript
onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this--><!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRenderExitedEvent](arkts-web-onrenderexitedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRenderProcessNotResponding

```TypeScript
onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-onrenderprocessnotrespondingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRenderProcessResponding

```TypeScript
onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-onrenderprocessrespondingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRequestSelected

```TypeScript
onRequestSelected(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onResourceLoad

```TypeScript
onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this--><!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnResourceLoadEvent](arkts-web-onresourceloadevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSafeBrowsingCheckFinish

```TypeScript
onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSafeBrowsingCheckResult

```TypeScript
onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScaleChange

```TypeScript
onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this--><!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScaleChangeEvent](arkts-web-onscalechangeevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScreenCaptureRequest

```TypeScript
onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this--><!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScreenCaptureRequestEvent](arkts-web-onscreencapturerequestevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScroll

```TypeScript
onScroll(callback: Callback<OnScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this--><!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScrollEvent](arkts-web-onscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSearchResultReceive

```TypeScript
onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSearchResultReceiveEvent](arkts-web-onsearchresultreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onShowFileSelector

```TypeScript
onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this--><!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnShowFileSelectorEvent](arkts-web-onshowfileselectorevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSslErrorEvent

```TypeScript
onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this--><!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-onsslerroreventcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onSslErrorEventReceive

```TypeScript
onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSslErrorEventReceiveEvent](arkts-web-onsslerroreventreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this--><!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-textselectionchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onTitleReceive

```TypeScript
onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this--><!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTitleReceiveEvent](arkts-web-ontitlereceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onTouchIconUrlReceived

```TypeScript
onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this--><!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTouchIconUrlReceivedEvent](arkts-web-ontouchiconurlreceivedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onVerifyPin

```TypeScript
onVerifyPin(callback: OnVerifyPinCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this--><!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-onverifypincallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onViewportFitChanged

```TypeScript
onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this--><!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-onviewportfitchangedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onWindowExit

```TypeScript
onWindowExit(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onWindowNew

```TypeScript
onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this--><!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewEvent](arkts-web-onwindownewevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onWindowNewExt

```TypeScript
onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this--><!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewExtEvent](arkts-web-onwindownewextevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onlineImageAccess

```TypeScript
onlineImageAccess(onlineImageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this--><!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onlineImageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## optimizeParserBudget

```TypeScript
optimizeParserBudget(optimizeParserBudget: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this--><!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optimizeParserBudget | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## overScrollMode

```TypeScript
overScrollMode(mode: OverScrollMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this--><!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [OverScrollMode](arkts-web-overscrollmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## overviewModeAccess

```TypeScript
overviewModeAccess(overviewModeAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this--><!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| overviewModeAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## pinchSmooth

```TypeScript
pinchSmooth(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this--><!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## registerNativeEmbedRule

```TypeScript
registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this--><!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string \| undefined | Yes |  |
| type | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## rotateRenderEffect

```TypeScript
rotateRenderEffect(effect: WebRotateEffect | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this--><!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [WebRotateEffect](arkts-web-webrotateeffect-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## runJavaScriptOnDocumentEnd

```TypeScript
runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## runJavaScriptOnDocumentStart

```TypeScript
runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## runJavaScriptOnHeadEnd

```TypeScript
runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollbarLayoutPolicy

```TypeScript
scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this--><!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-web-scrollbarlayoutpolicy-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## textAutosizing

```TypeScript
textAutosizing(textAutosizing: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this--><!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textAutosizing | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## textZoomRatio

```TypeScript
textZoomRatio(textZoomRatio: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this--><!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textZoomRatio | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## verticalScrollBarAccess

```TypeScript
verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| verticalScrollBar | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webCursiveFont

```TypeScript
webCursiveFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webCursiveFont(family: string | undefined): this--><!--Device-WebAttribute-webCursiveFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webFantasyFont

```TypeScript
webFantasyFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webFantasyFont(family: string | undefined): this--><!--Device-WebAttribute-webFantasyFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webFixedFont

```TypeScript
webFixedFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webFixedFont(family: string | undefined): this--><!--Device-WebAttribute-webFixedFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webSansSerifFont

```TypeScript
webSansSerifFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webSerifFont

```TypeScript
webSerifFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSerifFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## webStandardFont

```TypeScript
webStandardFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-webStandardFont(family: string | undefined): this--><!--Device-WebAttribute-webStandardFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## zoomAccess

```TypeScript
zoomAccess(zoomAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## zoomControlAccess

```TypeScript
zoomControlAccess(zoomControlAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomControlAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set whether to enable media network proxy for Web components. When enabled, network requests for media resources are routed through the web components network stack. This attribute takes effect for HLS media, other media formats are unaffected.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebAttribute-default--><!--Device-WebAttribute-default-End-->

**System capability:** SystemCapability.Web.Webview.Core

