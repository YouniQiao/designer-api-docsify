# WebAttribute

Defines the Web attribute functions.

@extends CommonMethod&lt;WebAttribute&gt;

**继承/实现关系：** WebAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface WebAttribute--><!--Device-unnamed-export declare interface WebAttribute-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## aiSessionOptions

```TypeScript
aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this--><!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-web-aisessionevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## allowWindowOpenMethod

```TypeScript
allowWindowOpenMethod(flag: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this--><!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WebAttribute](arkts-web-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## backToTop

```TypeScript
backToTop(backToTop: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this--><!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backToTop | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## bindSelectionMenu

```TypeScript
bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this--><!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementType | [WebElementType](arkts-web-webelementtype-e.md) \| undefined | 是 |  |
| content | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | 是 |  |
| responseType | [WebResponseType](arkts-web-webresponsetype-e.md) \| undefined | 是 |  |
| options | [SelectionMenuOptionsExt](arkts-web-selectionmenuoptionsext-i.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## blankScreenDetectionConfig

```TypeScript
blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this--><!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-web-blankscreendetectionconfig-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## blockNetwork

```TypeScript
blockNetwork(block: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this--><!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| block | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## blurOnKeyboardHideMode

```TypeScript
blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this--><!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-web-bluronkeyboardhidemode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## bypassVsyncCondition

```TypeScript
bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this--><!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-web-webbypassvsynccondition-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## cacheMode

```TypeScript
cacheMode(cacheMode: CacheMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this--><!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheMode | [CacheMode](arkts-web-cachemode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## copyOptions

```TypeScript
copyOptions(value: CopyOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this--><!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## darkMode

```TypeScript
darkMode(mode: WebDarkMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this--><!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebDarkMode](arkts-web-webdarkmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this--><!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## databaseAccess

```TypeScript
databaseAccess(databaseAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this--><!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| databaseAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## defaultFixedFontSize

```TypeScript
defaultFixedFontSize(size: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## defaultFontSize

```TypeScript
defaultFontSize(size: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-defaultFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFontSize(size: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## defaultTextEncodingFormat

```TypeScript
defaultTextEncodingFormat(textEncodingFormat: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this--><!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textEncodingFormat | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## domStorageAccess

```TypeScript
domStorageAccess(domStorageAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this--><!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domStorageAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this--><!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableAutoFill

```TypeScript
enableAutoFill(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this--><!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableDefaultContextMenu

```TypeScript
enableDefaultContextMenu(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableDrag

```TypeScript
enableDrag(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableDrag(value: boolean | undefined): this--><!--Device-WebAttribute-enableDrag(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableFollowSystemFontWeight

```TypeScript
enableFollowSystemFontWeight(follow: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this--><!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| follow | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableImageAnalyzer

```TypeScript
enableImageAnalyzer(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this--><!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableNativeEmbedMode

```TypeScript
enableNativeEmbedMode(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableNativeMediaPlayer

```TypeScript
enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this--><!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-web-nativemediaplayerconfig-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableScrollDirectionalLock

```TypeScript
enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this--><!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |
| type | [ScrollDirectionalLockType](arkts-web-scrolldirectionallocktype-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableWebAVSession

```TypeScript
enableWebAVSession(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fileAccess

```TypeScript
fileAccess(fileAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this--><!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## forceDarkAccess

```TypeScript
forceDarkAccess(access: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this--><!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## forceDisplayScrollBar

```TypeScript
forceDisplayScrollBar(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this--><!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## forceEnableZoom

```TypeScript
forceEnableZoom(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this--><!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## geolocationAccess

```TypeScript
geolocationAccess(geolocationAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this--><!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| geolocationAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## gestureFocusMode

```TypeScript
gestureFocusMode(mode: GestureFocusMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this--><!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [GestureFocusMode](arkts-web-gesturefocusmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## horizontalScrollBarAccess

```TypeScript
horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| horizontalScrollBar | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## imageAccess

```TypeScript
imageAccess(imageAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this--><!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## initialScale

```TypeScript
initialScale(percent: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-initialScale(percent: double | undefined): this--><!--Device-WebAttribute-initialScale(percent: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| percent | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## javaScriptAccess

```TypeScript
javaScriptAccess(javaScriptAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this--><!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| javaScriptAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## javaScriptOnDocumentEnd

```TypeScript
javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## javaScriptOnDocumentStart

```TypeScript
javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## javaScriptProxy

```TypeScript
javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this--><!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| javaScriptProxy | [JavaScriptProxy](arkts-web-javascriptproxy-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## keyboardAppearance

```TypeScript
keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this--><!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-web-webkeyboardappearancemode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this--><!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-web-webkeyboardavoidmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## layoutMode

```TypeScript
layoutMode(mode: WebLayoutMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this--><!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WebLayoutMode](arkts-web-weblayoutmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## mediaOptions

```TypeScript
mediaOptions(options: WebMediaOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this--><!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WebMediaOptions](arkts-web-webmediaoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## mediaPlayGestureAccess

```TypeScript
mediaPlayGestureAccess(access: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this--><!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## metaViewport

```TypeScript
metaViewport(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this--><!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## minFontSize

```TypeScript
minFontSize(size: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-minFontSize(size: int | undefined): this--><!--Device-WebAttribute-minFontSize(size: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## minLogicalFontSize

```TypeScript
minLogicalFontSize(size: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this--><!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## mixedMode

```TypeScript
mixedMode(mixedMode: MixedMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this--><!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mixedMode | [MixedMode](arkts-web-mixedmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## multiWindowAccess

```TypeScript
multiWindowAccess(multiWindow: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this--><!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multiWindow | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## nativeEmbedOptions

```TypeScript
nativeEmbedOptions(options?: EmbedOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this--><!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EmbedOptions](arkts-web-embedoptions-i.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this--><!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-web-nestedscrolloptionsext-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onActivateContent

```TypeScript
onActivateContent(callback: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this--><!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onAdsBlocked

```TypeScript
onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this--><!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-onadsblockedcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onAlert

```TypeScript
onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this--><!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAlertEvent](arkts-web-onalertevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onAudioStateChanged

```TypeScript
onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this--><!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAudioStateChangedEvent](arkts-web-onaudiostatechangedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onBeforeUnload

```TypeScript
onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this--><!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnBeforeUnloadEvent](arkts-web-onbeforeunloadevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onCameraCaptureStateChange

```TypeScript
onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-oncameracapturestatechangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onClientAuthenticationRequest

```TypeScript
onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this--><!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnClientAuthenticationEvent](arkts-web-onclientauthenticationevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onConfirm

```TypeScript
onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConfirmEvent](arkts-web-onconfirmevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onConsole

```TypeScript
onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConsoleEvent](arkts-web-onconsoleevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onContextMenuHide

```TypeScript
onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this--><!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-oncontextmenuhidecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onContextMenuShow

```TypeScript
onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this--><!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnContextMenuShowEvent](arkts-web-oncontextmenushowevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onControllerAttached

```TypeScript
onControllerAttached(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDataResubmitted

```TypeScript
onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this--><!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDataResubmittedEvent](arkts-web-ondataresubmittedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDetectedBlankScreen

```TypeScript
onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this--><!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-ondetectblankscreencallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDownloadStart

```TypeScript
onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this--><!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDownloadStartEvent](arkts-web-ondownloadstartevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onErrorReceive

```TypeScript
onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnErrorReceiveEvent](arkts-web-onerrorreceiveevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFaviconReceived

```TypeScript
onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this--><!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFaviconReceivedEvent](arkts-web-onfaviconreceivedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFirstContentfulPaint

```TypeScript
onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this--><!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFirstContentfulPaintEvent](arkts-web-onfirstcontentfulpaintevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFirstMeaningfulPaint

```TypeScript
onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-onfirstmeaningfulpaintcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFirstScreenPaint

```TypeScript
onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-onfirstscreenpaintcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFullScreenEnter

```TypeScript
onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this--><!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-onfullscreenentercallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFullScreenExit

```TypeScript
onFullScreenExit(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onGeolocationHide

```TypeScript
onGeolocationHide(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onGeolocationShow

```TypeScript
onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this--><!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnGeolocationShowEvent](arkts-web-ongeolocationshowevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onHttpAuthRequest

```TypeScript
onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this--><!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpAuthRequestEvent](arkts-web-onhttpauthrequestevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onHttpErrorReceive

```TypeScript
onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpErrorReceiveEvent](arkts-web-onhttperrorreceiveevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onInputmethodAttached

```TypeScript
onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this--><!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-oninputmethodattachedcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onIntelligentTrackingPreventionResult

```TypeScript
onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this--><!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-onintelligenttrackingpreventioncallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onInterceptKeyEvent

```TypeScript
onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this--><!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((event: KeyEvent) =&gt; boolean) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onInterceptKeyboardAttach

```TypeScript
onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this--><!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-webkeyboardcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onInterceptRequest

```TypeScript
onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this--><!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnInterceptRequestEvent](arkts-web-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-web-webresourceresponse-c.md) \| null&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onLargestContentfulPaint

```TypeScript
onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this--><!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-onlargestcontentfulpaintcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onLoadFinished

```TypeScript
onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this--><!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadFinishedEvent](arkts-web-onloadfinishedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onLoadIntercept

```TypeScript
onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadInterceptEvent](arkts-web-onloadinterceptevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onLoadStarted

```TypeScript
onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this--><!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadStartedEvent](arkts-web-onloadstartedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onMicrophoneCaptureStateChange

```TypeScript
onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-onmicrophonecapturestatechangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNativeEmbedGestureEvent

```TypeScript
onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedTouchInfo) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNativeEmbedLifecycleChange

```TypeScript
onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedDataInfo) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNativeEmbedMouseEvent

```TypeScript
onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MouseInfoCallback](arkts-mouseinfocallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNativeEmbedObjectParamChange

```TypeScript
onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-onnativeembedobjectparamchangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNativeEmbedVisibilityChange

```TypeScript
onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-onnativeembedvisibilitychangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onNavigationEntryCommitted

```TypeScript
onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this--><!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-onnavigationentrycommittedcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onOverScroll

```TypeScript
onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this--><!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnOverScrollEvent](arkts-web-onoverscrollevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onOverrideErrorPage

```TypeScript
onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this--><!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-onoverrideerrorpagecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onOverrideUrlLoading

```TypeScript
onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this--><!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-onoverrideurlloadingcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPageBegin

```TypeScript
onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this--><!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageBeginEvent](arkts-web-onpagebeginevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPageEnd

```TypeScript
onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this--><!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageEndEvent](arkts-web-onpageendevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPageVisible

```TypeScript
onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this--><!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageVisibleEvent](arkts-web-onpagevisibleevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPdfLoadEvent

```TypeScript
onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this--><!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfLoadEvent](arkts-web-onpdfloadevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPdfScrollAtBottom

```TypeScript
onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this--><!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfScrollEvent](arkts-web-onpdfscrollevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPermissionRequest

```TypeScript
onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this--><!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPermissionRequestEvent](arkts-web-onpermissionrequestevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onProgressChange

```TypeScript
onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this--><!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnProgressChangeEvent](arkts-web-onprogresschangeevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onPrompt

```TypeScript
onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPromptEvent](arkts-web-onpromptevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRefreshAccessedHistory

```TypeScript
onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this--><!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRefreshAccessedHistoryEvent](arkts-web-onrefreshaccessedhistoryevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRenderExited

```TypeScript
onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this--><!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRenderExitedEvent](arkts-web-onrenderexitedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRenderProcessNotResponding

```TypeScript
onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-onrenderprocessnotrespondingcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRenderProcessResponding

```TypeScript
onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-onrenderprocessrespondingcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRequestSelected

```TypeScript
onRequestSelected(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onResourceLoad

```TypeScript
onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this--><!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnResourceLoadEvent](arkts-web-onresourceloadevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSafeBrowsingCheckFinish

```TypeScript
onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSafeBrowsingCheckResult

```TypeScript
onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScaleChange

```TypeScript
onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this--><!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScaleChangeEvent](arkts-web-onscalechangeevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScreenCaptureRequest

```TypeScript
onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this--><!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScreenCaptureRequestEvent](arkts-web-onscreencapturerequestevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScroll

```TypeScript
onScroll(callback: Callback<OnScrollEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this--><!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScrollEvent](arkts-web-onscrollevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSearchResultReceive

```TypeScript
onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSearchResultReceiveEvent](arkts-web-onsearchresultreceiveevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onShowFileSelector

```TypeScript
onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this--><!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnShowFileSelectorEvent](arkts-web-onshowfileselectorevent-i.md), boolean&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSslErrorEvent

```TypeScript
onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this--><!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-onsslerroreventcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onSslErrorEventReceive

```TypeScript
onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSslErrorEventReceiveEvent](arkts-web-onsslerroreventreceiveevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this--><!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-textselectionchangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onTitleReceive

```TypeScript
onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this--><!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTitleReceiveEvent](arkts-web-ontitlereceiveevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onTouchIconUrlReceived

```TypeScript
onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this--><!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTouchIconUrlReceivedEvent](arkts-web-ontouchiconurlreceivedevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onVerifyPin

```TypeScript
onVerifyPin(callback: OnVerifyPinCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this--><!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-onverifypincallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onViewportFitChanged

```TypeScript
onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this--><!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-onviewportfitchangedcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWindowExit

```TypeScript
onWindowExit(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWindowNew

```TypeScript
onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this--><!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewEvent](arkts-web-onwindownewevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWindowNewExt

```TypeScript
onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this--><!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewExtEvent](arkts-web-onwindownewextevent-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onlineImageAccess

```TypeScript
onlineImageAccess(onlineImageAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this--><!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onlineImageAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## optimizeParserBudget

```TypeScript
optimizeParserBudget(optimizeParserBudget: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this--><!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| optimizeParserBudget | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## overScrollMode

```TypeScript
overScrollMode(mode: OverScrollMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this--><!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [OverScrollMode](arkts-web-overscrollmode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## overviewModeAccess

```TypeScript
overviewModeAccess(overviewModeAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this--><!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| overviewModeAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pinchSmooth

```TypeScript
pinchSmooth(isEnabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this--><!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## registerNativeEmbedRule

```TypeScript
registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this--><!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tag | string \| undefined | 是 |  |
| type | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## rotateRenderEffect

```TypeScript
rotateRenderEffect(effect: WebRotateEffect | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this--><!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [WebRotateEffect](arkts-web-webrotateeffect-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## runJavaScriptOnDocumentEnd

```TypeScript
runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## runJavaScriptOnDocumentStart

```TypeScript
runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## runJavaScriptOnHeadEnd

```TypeScript
runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollbarLayoutPolicy

```TypeScript
scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this--><!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-web-scrollbarlayoutpolicy-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textAutosizing

```TypeScript
textAutosizing(textAutosizing: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this--><!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textAutosizing | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textZoomRatio

```TypeScript
textZoomRatio(textZoomRatio: int | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this--><!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textZoomRatio | int \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## verticalScrollBarAccess

```TypeScript
verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verticalScrollBar | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webCursiveFont

```TypeScript
webCursiveFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webCursiveFont(family: string | undefined): this--><!--Device-WebAttribute-webCursiveFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webFantasyFont

```TypeScript
webFantasyFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webFantasyFont(family: string | undefined): this--><!--Device-WebAttribute-webFantasyFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webFixedFont

```TypeScript
webFixedFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webFixedFont(family: string | undefined): this--><!--Device-WebAttribute-webFixedFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webSansSerifFont

```TypeScript
webSansSerifFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webSerifFont

```TypeScript
webSerifFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSerifFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## webStandardFont

```TypeScript
webStandardFont(family: string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-webStandardFont(family: string | undefined): this--><!--Device-WebAttribute-webStandardFont(family: string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| family | string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## zoomAccess

```TypeScript
zoomAccess(zoomAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## zoomControlAccess

```TypeScript
zoomControlAccess(zoomControlAccess: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomControlAccess | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

The callback is triggered when the inputmethod is attached to the IMF.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebAttribute-default--><!--Device-WebAttribute-default-End-->

**系统能力：** SystemCapability.Web.Webview.Core

