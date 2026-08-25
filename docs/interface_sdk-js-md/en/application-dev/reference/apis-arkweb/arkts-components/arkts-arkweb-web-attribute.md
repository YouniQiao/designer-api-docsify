# Web properties/events

Defines the Web attribute functions.

**Inheritance/Implementation:** WebAttribute extends CommonMethod<WebAttribute>

**Since:** 8

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## aiSessionOptions

```TypeScript
aiSessionOptions(aiSessions: Array<AISessionEvent>)
```

Configures custom frontend AI sessions for the **Web** component, used to register multiple custom AI sessions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-arkweb-aisessionevent-i.md)&gt; | Yes |

## allowWindowOpenMethod

```TypeScript
allowWindowOpenMethod(flag : boolean)
```

Sets whether to allow a new window to automatically open through JavaScript.

> **NOTE：**&gt;
> - This API takes effect only when [javaScriptAccess](#javascriptaccess) is enabled.&gt;
> - This API opens a new window when [multiWindowAccess](#multiwindowaccess) is enabled, and a
> local window when it is disabled.&gt;
> - The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled**
> system attribute. If this attribute is not set, the default value of **flag** is **false**.&gt;
> - Run the **hdc shell param get persist.web.allowWindowOpenMethod.enabled** command to check whether the system
> attribute **persist.web.allowWindowOpenMethod.enabled** is enabled. If the attribute value is **1**, the system
> attribute is enabled. If the attribute value is **0** or does not exist, the system attribute is disabled. You
> can run the **hdc shell param set persist.web.allowWindowOpenMethod.enabled 1** command to enable the system
> attribute.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | boolean | Yes |

## backToTop

```TypeScript
backToTop(backToTop: boolean)
```

Sets whether to enable the back-to-top feature for the **Web** component when the status bar is touched. When this attribute is not explicitly called, the back-to-top feature for the status bar is enabled by default.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [backToTop](#backtotop) | boolean | Yes |

## bindSelectionMenu

```TypeScript
bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType,
      options?: SelectionMenuOptionsExt)
```

Sets the custom selection menu.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementType | [WebElementType](arkts-arkweb-webelementtype-e.md) | Yes |
| content | [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md) | Yes |
| responseType | [WebResponseType](arkts-arkweb-webresponsetype-e.md) | Yes |
| options | [SelectionMenuOptionsExt](arkts-arkweb-selectionmenuoptionsext-i.md) | No |

## blankScreenDetectionConfig

```TypeScript
blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig)
```

Sets the blank screen detection configuration, such as whether to enable the detection, detection time, and detection policy. When this attribute is not explicitly called, blank screen detection is disabled by default.

> **NOTE：**&gt;
> - Based on the configuration of **detectConfig**,
> [onDetectedBlankScreen](#ondetectedblankscreen) may be triggered when a blank screen or near-
> blank screen is detected after a web page is loaded.&gt;
> - The setting takes effect in the next navigation.&gt;
> - After the user interacts with the web page, the system does not check whether a blank screen occurs.&gt;
> - This feature is not supported when **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-arkweb-blankscreendetectionconfig-i.md) | Yes |

## blockNetwork

```TypeScript
blockNetwork(block: boolean)
```

Sets whether to block online downloads. When this attribute is not explicitly called, online resources can be loaded by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| block | boolean | Yes |

## blurOnKeyboardHideMode

```TypeScript
blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode)
```

Sets the blur mode for **Web** elements when the soft keyboard is dismissed. If this attribute is not explicitly called, the [BlurOnKeyboardHideMode.SILENT](arkts-arkweb-bluronkeyboardhidemode-e.md) mode is used by default.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-arkweb-bluronkeyboardhidemode-e.md) | Yes |

## bypassVsyncCondition

```TypeScript
bypassVsyncCondition(condition: WebBypassVsyncCondition)
```

Sets the rendering process to bypass vsync (vertical synchronization) scheduling and directly trigger drawing when the **scrollBy** API is called to scroll the page. When this attribute is not explicitly called, vsync scheduling is not skipped by default.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-arkweb-webbypassvsynccondition-e.md) | Yes |

## cacheMode

```TypeScript
cacheMode(cacheMode: CacheMode)
```

Sets the cache mode. When this attribute is not explicitly called, the default value **CacheMode.Default** is used.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cacheMode](#cachemode) | [CacheMode](arkts-arkweb-cachemode-e.md) | Yes |

## copyOptions

```TypeScript
copyOptions(value: CopyOptions)
```

Sets the clipboard copy scope option. If this attribute is not explicitly called, pasting across all apps on the current device is supported by default after copying.

> **NOTE：**&gt;
> When this attribute is set to **CopyOptions.None**, the **enablePreviewMenu** configuration item in
> [dataDetectorConfig](#datadetectorconfig) does not take effect. When
> [enableDataDetector](#enabledatadetector) is set to **true** and this attribute is set to
> **CopyOptions.LocalDevice**, the AI menu feature is activated.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](#copyoptions) | Yes |

## darkMode

```TypeScript
darkMode(mode: WebDarkMode)
```

Sets the dark mode of the **Web** component. If this attribute is not explicitly called, dark mode is disabled by default.When dark mode is enabled, the **Web** component enables the dark style defined in the media query **prefers-color-scheme** of the web page. If it is not defined, the web page remains unchanged. To enable forcible dark mode, use this API with [forceDarkAccess](#forcedarkaccess). For details about how to use dark mode, see [Setting Dark Mode](../../../web/web-set-dark-mode.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebDarkMode](arkts-arkweb-webdarkmode-e.md) | Yes |

## databaseAccess

```TypeScript
databaseAccess(databaseAccess: boolean)
```

Sets whether to enable the Web SQL Database storage API permission. If this permission is not explicitly called, it is disabled by default.

> **NOTE：**&gt;
> - After the ArkWeb kernel is upgraded to M132, the API's control over the Web SQL Database becomes invalid
> because the kernel discards Web SQL. For details about the ArkWeb kernel version, see
> [Constraints](../../../web/web-component-overview.md#constraints).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [databaseAccess](#databaseaccess) | boolean | Yes |

## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig)
```

Configures text recognition settings.This API must be used together with [enableDataDetector](#enabledatadetector). It takes effect only when **enableDataDetector** is set to **true**.When entities A and B overlap, the following rules are followed:
1. If A is a subset of B (A ⊂ B), then B is retained; otherwise, A is retained.
2. If A is not a subset of B (A ⊄ B) and B is not a subset of A (B ⊄ A), and if the starting point of A is earlier
than that of B (A.start &lt; B.start), then A is retained; otherwise, B is retained.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textdatadetectorconfig-i.md) | Yes |

## defaultFixedFontSize

```TypeScript
defaultFixedFontSize(size: number)
```

Sets the default fixed font size for the web page. For HTML elements that use the **monospace** font and do not specify **font-size**, the font size is rendered based on this value.When this attribute is not explicitly called, the default fixed font size is **13**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## defaultFontSize

```TypeScript
defaultFontSize(size: number)
```

Sets the default font size for the web page. For HTML elements that use non-monospace fonts and do not specify **font-size**, the font size is rendered based on this value.When this attribute is not explicitly called, the default font size of the web page is **16**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## defaultTextEncodingFormat

```TypeScript
defaultTextEncodingFormat(textEncodingFormat: string)
```

Sets the default text encoding format for the web page. When this attribute is not explicitly called, the default text encoding format of the web page is UTF-8.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| textEncodingFormat | string | Yes |

## domStorageAccess

```TypeScript
domStorageAccess(domStorageAccess: boolean)
```

Sets whether to enable the DOM Storage API permission. If this attribute is not explicitly called, the DOM Storage API permission is disabled by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domStorageAccess](#domstorageaccess) | boolean | Yes |

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions)
```

Sets a custom text selection menu for the **Web** component.

> **NOTE：**&gt;
> This API is similar to **bindSelectionMenu**, with the following differences:&gt;
> - **editMenuOptions**: Adds extension items based on the system default menu style, with the trigger conditions
> unchanged.&gt;
> - [bindSelectionMenu](#bindselectionmenu): Fully customizes the menu style and trigger
> conditions, as defined by the developer.&gt;
> It is not recommended to use both at the same time. Choose based on the degree of customization required.
> You can use this attribute to customize a text menu.
You can use onCreateMenu to modify, add, and delete menu options. If you do not want to display the text menu, return an empty array.You can use onMenuItemClick to customize the callback for menu options. This function is triggered after a menu option is clicked and determines whether to execute the default callback based on the return value. If **true** is returned, the system callback is not executed. If **false** is returned, the system callback is executed.In [onPrepareMenu&lt;sup&gt;20+&lt;/sup&gt;](../../../reference/apis-arkui/arkui-ts/ts-text-common.md#properties-1), this callback is triggered after the text selection area changes and before the menu is displayed. You can modify, add, or delete menu options in the callback to dynamically update the menu.If this method is used together with [selectionMenuOptions&lt;sup&gt;(deprecated)&lt;/sup&gt;](#selectionmenuoptions), the **selectionMenuOptions&lt;sup  
&gt; (deprecated) &lt;/sup&gt;** method does not take effect.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-editmenuoptions-i.md) | Yes |

## enableAutoFill

```TypeScript
enableAutoFill(value: boolean)
```

Sets whether to enable web page autofill. By default, this feature is enabled.<!--RP1-->

> **NOTE：**&gt;
> The autofill feature of this API depends on SmartFill service and Password Autofill Service.
<!--RP1End-->

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean)
```

Sets whether to recognize special entities of web texts, such as emails, phone numbers, and URLs. This API depends on the text recognition capability at the bottom layer of the device. Otherwise, the setting is invalid. When this attribute is not explicitly called, the detector is disabled by default.

> **NOTE：**&gt;
> Attributes such as [dataDetectorConfig](#datadetectorconfig) and
> [enableSelectedDataDetector](#enableselecteddatadetector) take effect only when this attribute
> is enabled.
> If **enableDataDetector** is set to **true** and [dataDetectorConfig](#datadetectorconfig) is
> not set, all types of entities will be recognized, and the **color** and **decoration** attributes of the
> recognized entities will be changed to the following styles:
<!--code_no_check-->When **enableDataDetector** is set to **true** and [copyOptions](#copyoptions) is set to **CopyOptions.LocalDevice**, the AI menu feature is activated. In this case, after text is selected on the web page, the text selection menu can display the corresponding AI menu items, including **url** (open link), **email** (create new email), **phoneNumber** (call), **address** (navigate to the location), and **dateTime** (create new schedule reminder) from [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md).When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md) do not appear at the same time.For details about the application scenario, see [Using Smart Text Data Detector](../../../web/web-data-detector.md).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableDefaultContextMenu

```TypeScript
enableDefaultContextMenu(enable: boolean)
```

Sets whether to enable the default right-click context menu. If this method is not explicitly called, the menu is disabled by default. The default menu supports only the **CUT**, **COPY**, **PASTE**, and **SELECT_ALL** menu items.

> **NOTE：**&gt;
> - When the [onContextMenuShow](#oncontextmenushow) callback is set and returns **true** in the
> callback, the setting of this API does not take effect.&gt;
> - The default menu items are controlled by [editMenuOptions](#editmenuoptions), through which
> you can customize the menu options.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableDrag

```TypeScript
enableDrag(value: boolean)
```

Sets whether to enable the drag function. If this attribute is not explicitly called, the web page drag function is enabled by default.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## enableFollowSystemFontWeight

```TypeScript
enableFollowSystemFontWeight(follow: boolean)
```

Sets whether the **Web** component can change the font weight according to the system settings. When this attribute is not explicitly called, the **Web** component can't change the font weight according to the system settings by default.

> **NOTE：**&gt;
> Currently, only front-end text elements support this capability. The **canvas** element and embedded .docx and
> .pdf texts do not support this capability.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [follow](../../apis-arkui/arkts-components/arkts-arkui-geometrytransitionoptions-i.md) | boolean | Yes |

## enableFullscreenVideoOverlay

```TypeScript
enableFullscreenVideoOverlay(enabled: boolean)
```

Sets whether to enable the overlay fullscreen playback feature for the **Web** component. If this attribute is not explicitly called, this feature is disabled by default.

> **NOTE：**&gt;
> - Currently, only videos in H.264 and H.265 decoding formats are supported.&gt;
> - Only fullscreen requests initiated by video elements are responded to.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean)
```

Sets whether to enable haptic feedback for number-pressed text in the **Web** component. The **ohos.permission.VIBRATE** permission must be declared. When this attribute is not explicitly called, haptic feedback is enabled by default.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## enableImageAnalyzer

```TypeScript
enableImageAnalyzer(enable: boolean)
```

Sets whether to enable AI analysis of web page images. Currently, the image text recognition feature is supported. If this attribute is not explicitly called, this feature is enabled by default.

> **NOTE：**&gt;
> When you number-press or hover the mouse over the image text, AI analyzer is triggered and the text in the image
> can be selected. The specifications of images that can trigger analyzer are as follows:&gt;
> - The original width and height of the image are greater than or equal to 100 pixels.&gt;
> - For [devices](../../../quick-start/module-configuration-file.md#devicetypes) other than 2-in-1 devices, the
> image rendering width must exceed 80% of the web page width.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableMediaNetworkProxy

```TypeScript
enableMediaNetworkProxy(enabled: boolean)
```

Sets whether to enable the media resource network request proxy feature for the **Web** component. If this attribute is not explicitly called, this feature is disabled by default.

> **NOTE：**&gt;
> - Currently, only HLS streaming media videos are supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## enableNativeEmbedMode

```TypeScript
enableNativeEmbedMode(enabled: boolean)
```

Sets whether to enable the same-layer rendering feature. When this method is not explicitly called, the same-layer rendering feature is disabled by default.

> **NOTE：**&gt;
> APIs such as [registerNativeEmbedRule](#registernativeembedrule) and
> [nativeEmbedOptions](#nativeembedoptions) take effect only when this attribute is enabled.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## enableNativeMediaPlayer

```TypeScript
enableNativeMediaPlayer(config: NativeMediaPlayerConfig)
```

Sets whether to enable the [application to take over web page media playback](../../../web/app-takeovers-web-media.md). When this attribute is not explicitly called, the web page media playback takeover feature is disabled by default.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-arkweb-nativemediaplayerconfig-i.md) | Yes |

## enableScrollDirectionalLock

```TypeScript
enableScrollDirectionalLock(value: boolean, type: ScrollDirectionalLockType)
```

Sets the scroll direction lock for the **Web** component to prevent simultaneous horizontal and vertical scrolling when the user swipes diagonally, thereby improving the scrolling experience. If this method is not explicitly called, scroll direction lock is supported by default in nested scrolling scenarios. The **ALL** mode applies to all scenarios where scroll locking is needed, while the **NESTED_SCROLL** mode applies only to nested scrolling scenarios.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
| type | [ScrollDirectionalLockType](arkts-arkweb-scrolldirectionallocktype-e.md) | Yes |

## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean)
```

Sets whether to enable the AI menu feature for text selection menu. After the AI menu feature is enabled, the email, phone number, website, date, and address in the selection can be identified, and the corresponding AI menu items are displayed in the text selection menu. By default, the AI menu feature is enabled.When the AI menu feature is enabled, after text is selected on the web page, the text selection menu can display the corresponding AI menu items, including **url** (open link), **email** (create new email), **phoneNumber** (call), **address** (navigate to the location), and **dateTime** (create new schedule) from [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md).When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md) do not appear at the same time.For details about the application scenario, see [Using Smart Text Data Detector](../../../web/web-data-detector.md).

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## enableWebAVSession

```TypeScript
enableWebAVSession(enabled: boolean)
```

Sets whether to support an application to connect to media controller. If this attribute is not explicitly set, the application can connect to media controller by default.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## fileAccess

```TypeScript
fileAccess(fileAccess: boolean)
```

Sets whether to enable access to the file system in the application. This setting does not affect the access to the files specified through [\$rawfile(filepath/filename)](../../../quick-start/resource-categories-and-access.md#accessing-resources). For API version 11 and earlier versions, access to the file system in the application is enabled by default if this attribute is not explicitly called. Since API version 12, access to the file system in the application is disabled by default if this attribute is not explicitly called.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fileAccess](#fileaccess) | boolean | Yes |

## forceDarkAccess

```TypeScript
forceDarkAccess(access: boolean)
```

Sets whether to enable forcible dark mode for the web page. This API is applicable only when [darkMode](#darkmode) is enabled. When this attribute is not explicitly called, forcible dark mode is disabled for the web page by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| access | boolean | Yes |

## forceDisplayScrollBar

```TypeScript
forceDisplayScrollBar(enabled: boolean)
```

Sets whether the scroll bar is always visible. Under the always-visible settings, when the page size exceeds one page, the scroll bar appears and remains visible. When this attribute is not explicitly called, the scroll bar is not always visible by default.When **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**, the **enabled** parameter is set to **false**.

> **NOTE：**&gt;
> - This interface takes effect globally across all web components in the current application. When multiple web
> components are set with different values, the value set for the first time will be used.&gt;
> - It is recommended that you use
> [setScrollbarMode](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#setscrollbarmode) to set the scrollbar
> mode for all web components currently applied. If the setScrollbarMode interface is invoked at the same time,
> the setting of the forceDisplayScrollBar interface does not take effect.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## forceEnableZoom

```TypeScript
forceEnableZoom(enable: boolean)
```

Sets whether to enable the forcible zoom functionality for the **Web** component.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## geolocationAccess

```TypeScript
geolocationAccess(geolocationAccess: boolean)
```

Sets whether to enable the geolocation permission. If this attribute is not explicitly called, the permission is enabled by default. For details about how to use this feature, see [Managing Location Permissions](../../../web/web-geolocation-permission.md).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [geolocationAccess](#geolocationaccess) | boolean | Yes |

## gestureFocusMode

```TypeScript
gestureFocusMode(mode: GestureFocusMode)
```

Sets the gesture focus mode of the **Web** component, which controls the focus response behavior of the **Web** component. If this attribute is not explicitly called, the default behavior is that any gesture causes the **Web** component to gain focus when the gesture is pressed.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [GestureFocusMode](arkts-arkweb-gesturefocusmode-e.md) | Yes |

## horizontalScrollBarAccess

```TypeScript
horizontalScrollBarAccess(horizontalScrollBar: boolean)
```

Sets whether to display the horizontal scrollbar, including the system default scrollbar and user-defined scrollbars. If this attribute is not explicitly called, the scrollbar is displayed by default.

> **NOTE：**&gt;
> - If an [@State](../../../ui/state-management/arkts-state.md) decorated variable is used to control the
> visibility of the horizontal scrollbar,
> [controller.refresh()](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) must be called for the
> settings to take effect.&gt;
> - When the [@State](../../../ui/state-management/arkts-state.md) decorated variable changes frequently and
> dynamically, it is recommended to maintain a one-to-one correspondence between the toggle variable and the
> **Web** component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| horizontalScrollBar | boolean | Yes |

## imageAccess

```TypeScript
imageAccess(imageAccess: boolean)
```

Sets whether to allow automatic loading of image resources. If this attribute is not explicitly called, automatic loading is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [imageAccess](#imageaccess) | boolean | Yes |

## initialScale

```TypeScript
initialScale(percent: number)
```

Sets the zoom percentage of the entire page. If this attribute is not explicitly called, the default value is **100**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| percent | number | Yes |

## javaScriptAccess

```TypeScript
javaScriptAccess(javaScriptAccess: boolean)
```

Sets whether to allow execution of JavaScript scripts. If this attribute is not explicitly called, execution is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [javaScriptAccess](#javascriptaccess) | boolean | Yes |

## javaScriptOnDocumentEnd

```TypeScript
javaScriptOnDocumentEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**&gt;
> - The script runs after any JavaScript code on the page, and the DOM tree has already been loaded and rendered at
> that point.&gt;
> - The scripts are executed in lexicographic order, not in the order of the array.&gt;
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.&gt;
> - This API does not support [UrlRegexRule](arkts-arkweb-urlregexrule-i.md).&gt;
> - You are advised to use [runJavaScriptOnDocumentEnd](#runjavascriptondocumentend) instead.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes |

## javaScriptOnDocumentStart

```TypeScript
javaScriptOnDocumentStart(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**&gt;
> - The script is injected after the root element (HTML Element) of the web document is created but before any
> other content is loaded.&gt;
> - The scripts are executed in lexicographic order, not in the order of the array. If the original array order is
> required, use the [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart) API instead.&gt;
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.&gt;
> - This API does not support [UrlRegexRule](arkts-arkweb-urlregexrule-i.md).&gt;
> - You are advised to use [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart) instead.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes |

## javaScriptProxy

```TypeScript
javaScriptProxy(javaScriptProxy: JavaScriptProxy)
```

Registers the ArkTS object in **javaScriptProxy** with the **Web** component. The object will be registered in all frames of the web page, including all iframes, using the name specified in **JavaScriptProxy**. This enables JavaScript to call methods of the ArkTS object in **javaScriptProxy**.

> **NOTE：**&gt;
> The **javaScriptProxy** API must be used together with
> [deleteJavaScriptRegister&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#deletejavascriptregister)
> to prevent memory leaks.&gt;
> All parameters of the **javaScriptProxy** object cannot be updated.&gt;
> When registering a **javaScriptProxy** object, at least one of the synchronous or asynchronous method lists must
> be non-empty. Both types of methods can be registered simultaneously.&gt;
> This API supports registering only one object. To register multiple objects, use
> [registerJavaScriptProxy&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#registerjavascriptproxy).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [javaScriptProxy](#javascriptproxy) | [JavaScriptProxy](arkts-arkweb-javascriptproxy-i.md) | Yes |

## keyboardAppearance

```TypeScript
keyboardAppearance(mode: WebKeyboardAppearanceMode)
```

Sets the keyboard appearance mode, which controls the appearance style of the keyboard that pops up for input boxes in the **Web** component, including immersive and non-immersive modes. If this method is not explicitly called, the system immersive mode is followed by default.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-arkweb-webkeyboardappearancemode-e.md) | Yes |

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: WebKeyboardAvoidMode)
```

Sets the custom soft keyboard avoidance mode.If the keyboard avoidance mode set in **UIContext** is [KeyboardAvoidMode.RESIZE](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md), this API does not take effect.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-arkweb-webkeyboardavoidmode-e.md) | Yes |

## layoutMode

```TypeScript
layoutMode(mode: WebLayoutMode)
```

Sets the layout mode of the **Web** component. If this attribute is not explicitly called, the **Web** layout follows the system mode (**WebLayoutMode.NONE**) by default. For common issues, see [Web Component Size Adapting to Page Content Layout](../../../web/web-fit-content.md).

> **NOTE：**&gt;
> Currently, only two **Web** layout modes are supported:&gt;
> - The **Web** layout follows the system mode (**WebLayoutMode.NONE**).&gt;
> - The **Web** component height adapts to the frontend page height (**WebLayoutMode.FIT_CONTENT**).&gt;
> The adaptive layout of the **Web** component height based on the frontend page has the following limitations:&gt;
> - When **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**:&gt;
> - [forceDisplayScrollBar](#forcedisplayscrollbar) does not support persistent display.&gt;
> - [blankScreenDetectionConfig](#blankscreendetectionconfig) does not take effect.&gt;
> - If the width or height of the **Web** component exceeds 7680 px, specify the **RenderMode.SYNC_RENDER** mode
> when creating the **Web** component. Otherwise, the entire screen will be blank.&gt;
> - Dynamic switching of the **layoutMode** mode is not supported after the **Web** component is created.&gt;
> - **Web** component size specifications: When **RenderMode.ASYNC_RENDER** is specified, the width and height must
> not exceed 7680 px respectively.&gt;
> - Frequent changes to the page width and height will trigger re-layout of the **Web** component, affecting the
> user experience.&gt;
> - Waterfall layout web pages (loading more content when scrolling to the bottom) are not supported.&gt;
> - Width adaptation is not supported; only height adaptation is supported.&gt;
> - Because the height adapts to the web page height, you cannot modify the component height by changing the
> component height attribute.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WebLayoutMode](arkts-arkweb-weblayoutmode-e.md) | Yes |

## mediaOptions

```TypeScript
mediaOptions(options: WebMediaOptions)
```

Sets the web-based media playback policy, including the validity period for automatically resuming a paused web audio, and whether the audio of multiple **Web** instances in an application is exclusive. When this attribute is not explicitly set, the web audio cannot be automatically resumed after regaining the focus by default, and the audio of multiple **Web** instances in an application is exclusive.

> **NOTE：**&gt;
> - Audios in the same **Web** instance are considered as the same audio.&gt;
> - The media playback policy controls videos with an audio track.&gt;
> - You are advised to set [audioExclusive](arkts-arkweb-webmediaoptions-i.md) to the same value for all **Web** components.&gt;
> - Audio and video interruption takes effect within an application and between applications, and playback
> resumption takes effect only between applications.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [WebMediaOptions](arkts-arkweb-webmediaoptions-i.md) | Yes |

## mediaPlayGestureAccess

```TypeScript
mediaPlayGestureAccess(access: boolean)
```

Sets whether autoplay of audible videos requires a user tap. Muted video playback is not affected by this API. If this attribute is not explicitly set, a user tap is required by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| access | boolean | Yes |

## metaViewport

```TypeScript
metaViewport(enabled: boolean)
```

Sets whether the **viewport** attribute of the **meta** tag is enabled. When this attribute is not explicitly called, the **viewport** attribute of the **meta** tag is supported by default.

> **NOTE：**&gt;
> - Whether the **viewport** attribute of the **\&lt;meta&gt;** tag in the frontend HTML page is enabled is determined by
> checking whether the User-Agent contains the "Mobile" field. When the User-Agent does not contain the "Mobile"
> field, the **viewport** attribute in the **\&lt;meta&gt;** tag is disabled by default. In this case, you can explicitly
> set the **metaViewport** attribute to **true** to override the disabled state.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## minFontSize

```TypeScript
minFontSize(size: number)
```

Sets the minimum font size for the web page. If the font size of HTML elements is smaller than the value set by this API, the font size is rendered based on the value set by this API.When no attribute is explicitly called, the default minimum font size of the web page is **8**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## minLogicalFontSize

```TypeScript
minLogicalFontSize(size: number)
```

Sets the minimum logical font size for the web page.For HTML elements whose font size is not specified:
1. If the font size of the element is smaller than the value set by this API, the font size is rendered based on the API value.
2. If **minLogicalFontSize** and **minFontSize** are both set, the larger value of the two will be used for elements whose font size is not specified.
When this attribute is not explicitly called, the default minimum logical font size of the web page is **8**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

## mixedMode

```TypeScript
mixedMode(mixedMode: MixedMode)
```

Sets the behavior when a secure source attempts to load resources from an insecure source. When this attribute is not explicitly called, the default value is **MixedMode.None**, which means that secure sources are not allowed to load content from insecure sources.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mixedMode](#mixedmode) | [MixedMode](arkts-arkweb-mixedmode-e.md) | Yes |

## multiWindowAccess

```TypeScript
multiWindowAccess(multiWindow: boolean)
```

Sets whether to enable the multi-window permission. If this attribute is not explicitly called, the permission is disabled by default.Enabling the multi-window permission requires implementation of the **onWindowNew** event. For the sample code, see [onWindowNew](#onwindownew).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| multiWindow | boolean | Yes |

## nativeEmbedOptions

```TypeScript
nativeEmbedOptions(options?: EmbedOptions)
```

Sets the same-layer rendering configuration. This attribute takes effect only when [enableNativeEmbedMode](#enablenativeembedmode) is enabled and cannot be dynamically modified. If this attribute is not explicitly called, the default value **{supportDefaultIntrinsicSize: false}** is used.

**Since:** 16

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [EmbedOptions](arkts-arkweb-embedoptions-i.md) | No |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt)
```

Sets nested scrolling options.

> **NOTE：**&gt;
> - You can set the up, down, left, and right directions, or set the forward and backward nested scrolling modes to
> implement scrolling linkage with the parent component.&gt;
> - Containers that support nested scrolling: Grid, List, Scroll,
> Swiper, Tabs, WaterFlow, Refresh and
> [bindSheet](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindsheet).&gt;
> - Input sources that support nested scrolling: gestures, mouse device, and touchpad.&gt;
> - In nested scrolling scenarios, since the **Web** component's over-scrolling to the edge will trigger the over-
> scroll bounce effect first, it is recommended that you set [overScrollMode](#overscrollmode) to
> **OverScrollMode.NEVER** to avoid undermining user experience.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-arkweb-nestedscrolloptionsext-i.md) | Yes |

## onActivateContent

```TypeScript
onActivateContent(callback: Callback<void>)
```

Triggered to check whether a bound **Web** instance exists based on the name when a web page triggers **window.open(url, name)**. If the instance exists, it receives this callback to notify the application of displaying it on the front end. If it does not exist, the application is notified to create a new **Web** instance through [onWindowNew](#onwindownew).

> **NOTE：**&gt;
> - Binding a **Web** instance by name: Call the **event.handler.setWebController** method in the [onWindowNew] (#
> onwindownew9) callback and transfer the controller of the new **Web** instance.&gt;
> - The name must comply with the regular expression **[a-zA-Z0-9_]+**. When the name is used as the value of the
> **target** attribute of the \&lt;a
&gt; or \&lt;form
&gt; tag, the bound **Web** instance also triggers this callback function.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onAdsBlocked

```TypeScript
onAdsBlocked(callback: OnAdsBlockedCallback)
```

Called after an ad is blocked on the web page to notify the user of detailed information about the blocked ad. To reduce the frequency of notifications and minimize the impact on the page loading process, only the first notification is made when the page is fully loaded. Subsequent blocking events are reported at intervals of 1 second, and no notifications are sent if there is no ad blocked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-arkweb-onadsblockedcallback-t.md) | Yes |

## onAlert

```TypeScript
onAlert(callback: Callback<OnAlertEvent, boolean>)
```

Triggered when **alert()** is invoked to display an alert dialog box on the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handleConfirm](arkts-arkweb-jsresult-c.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnAlertEvent](arkts-arkweb-onalertevent-i.md), boolean&gt; | Yes |

## onAudioStateChanged

```TypeScript
onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent>)
```

Triggered when the audio playback status on the web page changes.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnAudioStateChangedEvent](arkts-arkweb-onaudiostatechangedevent-i.md)&gt; | Yes |

## onBeforeUnload

```TypeScript
onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean>)
```

Called when the page refresh is about to complete or the current page is closed.

> **NOTE：**&gt;
> - If the current **Web** component does not have the focus, **onBeforeUnload** is not triggered when the page is
> refreshed or closed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnBeforeUnloadEvent](arkts-arkweb-onbeforeunloadevent-i.md), boolean&gt; | Yes |

## onCameraCaptureStateChange

```TypeScript
onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback)
```

Triggered to notify the user of the camera state on the current web page, which can be **None**, **Active**, or **Paused**. This API uses an asynchronous callback to return the result.You can use the **startCamera**, **stopCamera**, and **closeCamera** APIs to enable, pause, and stop the camera respectively. For details about how to use them, see [startCamera](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#startcamera).

> **NOTE：**&gt;
> **Active** is returned when the camera is being used on the current web page.&gt;
> **Paused** is returned when the camera is paused on the current web page.&gt;
> **None** is returned when the camera is not being used on the current web page.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-arkweb-oncameracapturestatechangecallback-t.md) | Yes |

## onClientAuthenticationRequest

```TypeScript
onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent>)
```

Triggered when an SSL client certificate request is received.

> **NOTE：**&gt;
> - The **Web** component can respond with
> [ClientAuthenticationHandler.confirm](arkts-arkweb-clientauthenticationhandler-c.md#confirm),
> [ClientAuthenticationHandler.cancel](arkts-arkweb-clientauthenticationhandler-c.md#cancel), or
> [ClientAuthenticationHandler.ignore](arkts-arkweb-clientauthenticationhandler-c.md#ignore).&gt;
> - If **ClientAuthenticationHandler.confirm** or **ClientAuthenticationHandler.cancel** is called, the **Web**
> component stores the authentication result in the memory (within the application lifecycle) and does not call
> **onClientAuthenticationRequest()** again for the same host and port. If **onClientAuthenticationRequest.ignore**
> is called, the **Web** component does not store the authentication result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnClientAuthenticationEvent](arkts-arkweb-onclientauthenticationevent-i.md)&gt; | Yes |

## onConfirm

```TypeScript
onConfirm(callback: Callback<OnConfirmEvent, boolean>)
```

Triggered when **confirm()** is invoked by the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handleConfirm](arkts-arkweb-jsresult-c.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnConfirmEvent](arkts-arkweb-onconfirmevent-i.md), boolean&gt; | Yes |

## onConsole

```TypeScript
onConsole(callback: Callback<OnConsoleEvent, boolean>)
```

Triggered to notify the host application of a JavaScript console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnConsoleEvent](arkts-arkweb-onconsoleevent-i.md), boolean&gt; | Yes |

## onContextMenuHide

```TypeScript
onContextMenuHide(callback: OnContextMenuHideCallback)
```

Triggered when a context menu is hidden after the user clicks the right mouse button or number presses a specific element, such as an image or a link.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-arkweb-oncontextmenuhidecallback-t.md) | Yes |

## onContextMenuShow

```TypeScript
onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean>)
```

Triggered when a context menu is displayed after the user clicks the right mouse button or number presses a specific element, such as an image or a link.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnContextMenuShowEvent](arkts-arkweb-oncontextmenushowevent-i.md), boolean&gt; | Yes |

## onControllerAttached

```TypeScript
onControllerAttached(callback: () => void)
```

Triggered when the controller is successfully bound to the **Web** component. The controller must be **WebviewController**. Do not call APIs related to the **Web** component before this callback event. Otherwise, a js-error exception will be thrown.The web page has not been loaded when the callback is called. Therefore, APIs related to web page operations, such as [zoomIn](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#zoomin), [zoomOut](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#zoomout), cannot be used in the callback. You can use APIs irrelevant to web page operations, such as [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl), [getWebId](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#getwebid).For details about the component lifecycle, see [Lifecycle of the Web Component](../../../web/web-event-sequence.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onDataResubmitted

```TypeScript
onDataResubmitted(callback: Callback<OnDataResubmittedEvent>)
```

Triggered when the web form data can be resubmitted.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnDataResubmittedEvent](arkts-arkweb-ondataresubmittedevent-i.md)&gt; | Yes |

## onDetectedBlankScreen

```TypeScript
onDetectedBlankScreen(callback: OnDetectBlankScreenCallback)
```

Called when the **Web** component detects a blank screen.

> **NOTE：**&gt;
> - This method must be used with [blankScreenDetectionConfig](#blankscreendetectionconfig).
> Otherwise, the blank screen detection is disabled by default, and the callback is not returned when a blank
> screen is detected.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-arkweb-ondetectblankscreencallback-t.md) | Yes |

## onDownloadStart

```TypeScript
onDownloadStart(callback: Callback<OnDownloadStartEvent>)
```

Triggered to instruct the main application to start downloading a file.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnDownloadStartEvent](arkts-arkweb-ondownloadstartevent-i.md)&gt; | Yes |

## onErrorReceive

```TypeScript
onErrorReceive(callback: Callback<OnErrorReceiveEvent>)
```

Triggered when an error occurs during web page loading. The error may occur on the main resource or sub-resource. You can use [isMainFrame](arkts-arkweb-webresourcerequest-c.md#ismainframe) to determine whether the error occurs on the main resource. For performance reasons, simplify the implementation logic in the callback. This API is called when there is no network connection.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnErrorReceiveEvent](arkts-arkweb-onerrorreceiveevent-i.md)&gt; | Yes |

## onFaviconReceived

```TypeScript
onFaviconReceived(callback: Callback<OnFaviconReceivedEvent>)
```

Triggered when this web page receives a new favicon.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnFaviconReceivedEvent](arkts-arkweb-onfaviconreceivedevent-i.md)&gt; | Yes |

## onFileSelectorShow

```TypeScript
onFileSelectorShow(callback: (event?: { callback: Function, fileSelector: object }) => void)
```

Triggered to process an HTML form whose input type is **file**, in response to the tapping of the **Select File** button.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onShowFileSelector](#onshowfileselector)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event?: { callback: Function, fileSelector: object }) = & gt; void | Yes |

## onFirstContentfulPaint

```TypeScript
onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent>)
```

Triggered when the first content paint occurs on the web page.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnFirstContentfulPaintEvent](arkts-arkweb-onfirstcontentfulpaintevent-i.md)&gt; | Yes |

## onFirstMeaningfulPaint

```TypeScript
onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback)
```

Triggered when the first meaningful paint occurs on the web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-arkweb-onfirstmeaningfulpaintcallback-t.md) | Yes |

## onFirstScreenPaint

```TypeScript
onFirstScreenPaint(callback: OnFirstScreenPaintCallback)
```

Triggered when the first screen paint of a web page is complete.

> **NOTE：**&gt;
> - First Screen Paint (FSP) records the time taken to render images, texts, and videos in the viewport. It is a
> core performance metric for measuring the duration from a page's initial load to the completion of rendering.
> When no visible elements within the viewport extend beyond the historical rendering area for a certain period of
> time, the moment when the maximum historical rendering of elements in the viewport is achieved is regarded as the
> completion time of first screen paint.&gt;
> - After the first screen is drawn, the API waits for a period of time and reports the callback when no new
> rendering information needs to be processed. The callback time is different from the first screen paint
> completion time.&gt;
> - If the user performs input operations or scrolls the page while rendering is still in progress, the callback
> function will be reported immediately.&gt;
> - This API is used to obtain the first screen rendering time in instant loading scenarios, but it will not
> deliver the expected results if used in preloading or prerendering scenarios.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-arkweb-onfirstscreenpaintcallback-t.md) | Yes |

## onFullScreenEnter

```TypeScript
onFullScreenEnter(callback: OnFullScreenEnterCallback)
```

Triggered when the **Web** component enters full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-arkweb-onfullscreenentercallback-t.md) | Yes |

## onFullScreenExit

```TypeScript
onFullScreenExit(callback: () => void)
```

Triggered when the **Web** component exits full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onGeolocationHide

```TypeScript
onGeolocationHide(callback: () => void)
```

Triggered to notify the user that the request for obtaining the geolocation information received when [onGeolocationShow](#ongeolocationshow) is called has been canceled.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onGeolocationShow

```TypeScript
onGeolocationShow(callback: Callback<OnGeolocationShowEvent>)
```

Called to notify the user that the geolocation information obtaining request is received. To use this API, the **ohos.permission.LOCATION** and **ohos.permission.APPROXIMATELY_LOCATION** permissions must be configured. This API uses an asynchronous callback to return the result.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnGeolocationShowEvent](arkts-arkweb-ongeolocationshowevent-i.md)&gt; | Yes |

## onHttpAuthRequest

```TypeScript
onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean>)
```

Triggered when an HTTP authentication request is received.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnHttpAuthRequestEvent](arkts-arkweb-onhttpauthrequestevent-i.md), boolean&gt; | Yes |

## onHttpErrorReceive

```TypeScript
onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent>)
```

Called when an HTTP error (the response code is greater than or equal to 400) occurs during web page resource loading.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnHttpErrorReceiveEvent](arkts-arkweb-onhttperrorreceiveevent-i.md)&gt; | Yes |

## onInputmethodAttached

```TypeScript
onInputmethodAttached(callback: OnInputmethodAttachedCallback)
```

The callback is triggered when the inputmethod is attached to the IMF.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-arkweb-oninputmethodattachedcallback-t.md) | Yes |

## onIntelligentTrackingPreventionResult

```TypeScript
onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback)
```

Triggered when the intelligent tracking prevention feature is enabled and the tracker cookie is blocked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-arkweb-onintelligenttrackingpreventioncallback-t.md) | Yes |

## onInterceptKeyboardAttach

```TypeScript
onInterceptKeyboardAttach(callback: WebKeyboardCallback)
```

Triggered before any editable element (such as the **input** tag) on the web page invokes the soft keyboard. The application can use this API to intercept the display of the system's soft keyboard and configure a custom soft keyboard. (With this API, the application can determine whether to use the system's default soft keyboard, a system soft keyboard with a custom Enter key, or a completely application-defined soft keyboard).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-arkweb-webkeyboardcallback-t.md) | Yes |

## onInterceptKeyEvent

```TypeScript
onInterceptKeyEvent(callback: (event: KeyEvent) => boolean)
```

Triggered when the key event is intercepted and before it is consumed by the webview.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event: KeyEvent) = & gt; boolean | Yes |

## onInterceptRequest

```TypeScript
onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse>)
```

Triggered when the **Web** component is about to access a URL. This API is used to block the URL and return the response data. The **onInterceptRequest** API can intercept all redirection requests and return response data, but cannot access POST request body content and obtain buffer data. In this scenario, use [WebSchemeHandler](../arkts-apis/arkts-arkweb-webview-webschemehandler-c.md) based on service requirements.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnInterceptRequestEvent](arkts-arkweb-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-arkweb-webresourceresponse-c.md)&gt; | Yes |

## onLargestContentfulPaint

```TypeScript
onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback)
```

Triggered when the largest content paint occurs on the web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-arkweb-onlargestcontentfulpaintcallback-t.md) | Yes |

## onlineImageAccess

```TypeScript
onlineImageAccess(onlineImageAccess: boolean)
```

Sets whether to allow loading of image resources from the network (resources accessed via HTTP and HTTPS). If this attribute is not explicitly called, loading is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [onlineImageAccess](#onlineimageaccess) | boolean | Yes |

## onLoadFinished

```TypeScript
onLoadFinished(callback: Callback<OnLoadFinishedEvent>)
```

Triggered to notify the host application that the page has been loaded. This method is called only when the main frame loading is complete. For fragment navigations (navigations to **#fragment_id**), **onLoadFinished** is also triggered.

> **NOTE：**&gt;
> - Fragment navigation also triggers **onLoadFinished**, but **onPageEnd** is not triggered.&gt;
> - If the main frame is automatically redirected before the page is fully loaded, **onLoadFinished** is triggered
> only once. **onPageEnd** is triggered each time the main frame is navigated.&gt;
> - When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is
> simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure. &lt;b class="
&gt; + topic/ph hi-d/b " id="b145733136532"&gt;onPageBegin&lt;/b
&gt; will not be simulated.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnLoadFinishedEvent](arkts-arkweb-onloadfinishedevent-i.md)&gt; | Yes |

## onLoadIntercept

```TypeScript
onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean>)
```

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnLoadInterceptEvent](arkts-arkweb-onloadinterceptevent-i.md), boolean&gt; | Yes |

## onLoadStarted

```TypeScript
onLoadStarted(callback: Callback<OnLoadStartedEvent>)
```

Triggered to notify the host application that the page loading starts. This method is called once each time the main frame content is loaded. Therefore, for pages that contain iframes or frameset, **onLoadStarted** is called only once for the main frame. This means that when the content of the embedded frame changes, for example, a link or a fragment navigation in the iframe is clicked (navigation to **#fragment_id**), **onLoadStarted** is not invoked.

> **NOTE：**&gt;
> - When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is
> simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure.
> **onPageBegin** will not be simulated.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnLoadStartedEvent](arkts-arkweb-onloadstartedevent-i.md)&gt; | Yes |

## onMicrophoneCaptureStateChange

```TypeScript
onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback)
```

Triggered to notify the user of the microphone state on the current web page, which can be **None**, **Active**, or **Paused**. This API uses an asynchronous callback to return the result.You can use the **resumeMicrophone**, **pauseMicrophone**, and **stopMicrophone** APIs to resume, pause, and stop the microphone. For details about how to use them, see [resumeMicrophone](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#resumemicrophone).

> **NOTE：**&gt;
> **Active** is returned when the current web page is using the microphone; **Paused** is returned when the
> current web page pauses using the microphone; **None** is returned when the current web page does not use the
> microphone.&gt;
> When the microphone is being used and the **pauseMicrophone** API is called, the microphone pauses capturing
> audio and **Paused** is returned. You can call the **resumeMicrophone** API using ArkWeb to resume the capture.&gt;
> When the microphone is being used and the **stopMicrophone** API is called, the microphone stops capturing audio
> and **None** is returned. Capture cannot be resumed unless the frontend capture is restarted.&gt;
> When the microphone is paused and the **resumeMicrophone** API is called, the microphone continues capturing
> audio and **Active** is returned.&gt;
> When the microphone is paused and the **stopMicrophone** API is called, the microphone stops capturing audio and
> **None** is returned. Capture cannot be resumed unless the frontend capture is restarted.&gt;
> When the microphone is in the **None** state and the **resumeMicrophone** or **pauseMicrophone** API is called,
> the microphone state remains unchanged.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-arkweb-onmicrophonecapturestatechangecallback-t.md) | Yes |

## onNativeEmbedGestureEvent

```TypeScript
onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void)
```

Triggered when a finger touches a same-layer tag.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event: NativeEmbedTouchInfo) = & gt; void | Yes |

## onNativeEmbedLifecycleChange

```TypeScript
onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void)
```

Triggered when the lifecycle of the same-layer tag changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event: NativeEmbedDataInfo) = & gt; void | Yes |

## onNativeEmbedMouseEvent

```TypeScript
onNativeEmbedMouseEvent(callback: MouseInfoCallback)
```

Triggered when the following operations are performed on the same-layer tag:  
- Tapping or holding with the left, middle, or right mouse button.  
- Tapping or holding the left, middle, or right mouse button using the touchpad.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [MouseInfoCallback](arkts-arkweb-mouseinfocallback-t.md) | Yes |

## onNativeEmbedObjectParamChange

```TypeScript
onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback)
```

Called when the **param** element embedded in the same-layer rendering tag **object** changes.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-arkweb-onnativeembedobjectparamchangecallback-t.md) | Yes |

## onNativeEmbedVisibilityChange

```TypeScript
onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback)
```

Triggered when the visibility of a same-layer tag (such as an **\&lt;embed&gt;** tag or an **\&lt;object&gt;** tag) on a web page changes in the viewport. Same-layer tags are invisible by default. If a tag is visible when the page is loaded for the first time, it is reported. If a tag is invisible, it is not reported. Same-layer tags are considered invisible only when they are all invisible. Partially visible or all visible tags are considered visible. To obtain the visible status change caused by the CSS attributes (including visibility, display, and size change) of the same -layer tag, configure [nativeEmbedOptions](#nativeembedoptions) and set **supportCssDisplayChange** in [EmbedOptions](arkts-arkweb-embedoptions-i.md) to **true**.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-arkweb-onnativeembedvisibilitychangecallback-t.md) | Yes |

## onNavigationEntryCommitted

```TypeScript
onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback)
```

Triggered when a web page redirection request is submitted.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-arkweb-onnavigationentrycommittedcallback-t.md) | Yes |

## onOverrideErrorPage

```TypeScript
onOverrideErrorPage(callback: OnOverrideErrorPageCallback)
```

Triggered when an error occurs during web page loading of main resources. You can use this API to customize the error display page.

> **NOTE：**&gt;
> This feature takes effect only after the default error page is enabled by calling the
> [setErrorPageEnabled](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#seterrorpageenabled)
> API.&gt;
> If the error code obtained through [errorPageEvent.error.getErrorCode()](arkts-arkweb-webresourceerror-c.md#geterrorcode) is
> greater than 0, it indicates an HTTP error. If the error code is less than 0, it indicates a network error.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-arkweb-onoverrideerrorpagecallback-t.md) | Yes |

## onOverrideUrlLoading

```TypeScript
onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback)
```

Triggered when the URL is about to be loaded in the current web page, allowing the host application to obtain control and determine whether to prevent the web page from loading the URL.

> **NOTE：**&gt;
> - POST requests do not trigger this callback.&gt;
> - This callback is triggered when the iframe loads a non-HTTP(S) document. It is not triggered for HTTP(S)
> documents, **about:blank**, or for any redirection that is started via **loadUrl(url: string)**.&gt;
> - Do not call **loadUrl(url: string)** with the same URL in the callback and return **true**. Doing so would
> unnecessarily cancel the current loading and start an identical one. To continue loading the current request URL,
> return **false** instead of calling **loadUrl(url: string)**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-arkweb-onoverrideurlloadingcallback-t.md) | Yes |

## onOverScroll

```TypeScript
onOverScroll(callback: Callback<OnOverScrollEvent>)
```

Triggered when the web page is overscrolled. It is used to notify the application of the overscroll offset.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnOverScrollEvent](arkts-arkweb-onoverscrollevent-i.md)&gt; | Yes |

## onPageBegin

```TypeScript
onPageBegin(callback: Callback<OnPageBeginEvent>)
```

Triggered when the web page starts to be loaded. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPageBeginEvent](arkts-arkweb-onpagebeginevent-i.md)&gt; | Yes |

## onPageEnd

```TypeScript
onPageEnd(callback: Callback<OnPageEndEvent>)
```

Triggered when the web page loading is finished. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPageEndEvent](arkts-arkweb-onpageendevent-i.md)&gt; | Yes |

## onPageVisible

```TypeScript
onPageVisible(callback: Callback<OnPageVisibleEvent>)
```

Triggered when the old page is not displayed and the new page is about to be visible.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPageVisibleEvent](arkts-arkweb-onpagevisibleevent-i.md)&gt; | Yes |

## onPdfLoadEvent

```TypeScript
onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>)
```

Called to notify the user of whether the PDF page is successfully loaded.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPdfLoadEvent](arkts-arkweb-onpdfloadevent-i.md)&gt; | Yes |

## onPdfScrollAtBottom

```TypeScript
onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>)
```

Called to notify the user that the PDF page has been scrolled to the bottom.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPdfScrollEvent](arkts-arkweb-onpdfscrollevent-i.md)&gt; | Yes |

## onPermissionRequest

```TypeScript
onPermissionRequest(callback: Callback<OnPermissionRequestEvent>)
```

Triggered when a permission request is received. To call this API, you need to declare the **ohos.permission.CAMERA** and **ohos.permission.MICROPHONE** permissions.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPermissionRequestEvent](arkts-arkweb-onpermissionrequestevent-i.md)&gt; | Yes |

## onProgressChange

```TypeScript
onProgressChange(callback: Callback<OnProgressChangeEvent>)
```

Triggered when the web page loading progress changes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnProgressChangeEvent](arkts-arkweb-onprogresschangeevent-i.md)&gt; | Yes |

## onPrompt

```TypeScript
onPrompt(callback: Callback<OnPromptEvent, boolean>)
```

Triggered when **prompt()** is invoked by the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handlePromptConfirm](arkts-arkweb-jsresult-c.md#handlepromptconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnPromptEvent](arkts-arkweb-onpromptevent-i.md), boolean&gt; | Yes |

## onRefreshAccessedHistory

```TypeScript
onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent>)
```

Triggered for the application to update its access history when the navigation is complete.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnRefreshAccessedHistoryEvent](arkts-arkweb-onrefreshaccessedhistoryevent-i.md)&gt; | Yes |

## onRenderExited

```TypeScript
onRenderExited(callback: Callback<OnRenderExitedEvent>)
```

Triggered when the rendering process exits abnormally.A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.You can call the bound **webviewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) and [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl).For details about the component lifecycle, see [Lifecycle of the Web Components](../../../web/web-event-sequence.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnRenderExitedEvent](arkts-arkweb-onrenderexitedevent-i.md)&gt; | Yes |

## onRenderExited

```TypeScript
onRenderExited(callback: (event?: { detail: object }) => boolean)
```

Triggered when the rendering process exits due to an error or crash.A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.You can call the bound **WebViewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) and [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl).For details, see [Lifecycle of the Web Component](../../../web/web-event-sequence.md).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onRenderExited](#onrenderexited)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event?: { detail: object }) = & gt; boolean | Yes |

## onRenderProcessNotResponding

```TypeScript
onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback)
```

Triggered when the rendering process does not respond. If the **Web** component cannot process the input event or navigate to a new URL within a proper time range, the web page process is considered unresponsive and the callback is triggered.If the web page process does not respond, this callback may be triggered until the web page process responds again. In this case, [onRenderProcessResponding](#onrenderprocessresponding) is triggered.You can terminate the associated rendering process through [terminateRenderProcess](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#terminaterenderprocess), which may affect other **Web** components in the same rendering process.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-arkweb-onrenderprocessnotrespondingcallback-t.md) | Yes |

## onRenderProcessResponding

```TypeScript
onRenderProcessResponding(callback: OnRenderProcessRespondingCallback)
```

Triggered when the rendering process transitions back to a normal operating state from an unresponsive state. This callback indicates that the web page was not actually frozen.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-arkweb-onrenderprocessrespondingcallback-t.md) | Yes |

## onRequestSelected

```TypeScript
onRequestSelected(callback: () => void)
```

Triggered when the **Web** component obtains the focus. If the **Web** component loads a web page in the unfocused state and successfully obtains the focus, the callback is triggered twice.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onResourceLoad

```TypeScript
onResourceLoad(callback: Callback<OnResourceLoadEvent>)
```

Triggered to notify the **Web** component of the URL of the resource file to load.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnResourceLoadEvent](arkts-arkweb-onresourceloadevent-i.md)&gt; | Yes |

## onSafeBrowsingCheckFinish

```TypeScript
onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback)
```

Called when the safe browsing check is complete.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) | Yes |

## onSafeBrowsingCheckResult

```TypeScript
onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback)
```

Called when the safe browsing check result is received.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) | Yes |

## onScaleChange

```TypeScript
onScaleChange(callback: Callback<OnScaleChangeEvent>)
```

Called when the page display scale changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnScaleChangeEvent](arkts-arkweb-onscalechangeevent-i.md)&gt; | Yes |

## onScreenCaptureRequest

```TypeScript
onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent>)
```

Triggered when a screen capture request is received.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnScreenCaptureRequestEvent](arkts-arkweb-onscreencapturerequestevent-i.md)&gt; | Yes |

## onScroll

```TypeScript
onScroll(callback: Callback<OnScrollEvent>)
```

Triggered to notify the global scrolling position of the web page.

> **NOTE：**&gt;
> The change of the partial scrolling position cannot trigger this callback.&gt;
> To determine whether a page is globally scrolled, print **window.pagYOffset** or **window.pagXOffset** before and
> after scrolling.&gt;
> If the web page is scrolled globally, the value of **window.pagYOffset** or **window.pagXOffset** changes after
> the web page is scrolled. Otherwise, the value does not change.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnScrollEvent](arkts-arkweb-onscrollevent-i.md)&gt; | Yes |

## onSearchResultReceive

```TypeScript
onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent>)
```

Triggered to notify the caller of the search result on the web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnSearchResultReceiveEvent](arkts-arkweb-onsearchresultreceiveevent-i.md)&gt; | Yes |

## onShowFileSelector

```TypeScript
onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean>)
```

Triggered to process an HTML form whose input type is **file**. If this function is not called or returns **false**, the **Web** component provides the default **Select file** UI. If it returns **true**, the application can customize the response behavior for **Select file**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnShowFileSelectorEvent](arkts-arkweb-onshowfileselectorevent-i.md), boolean&gt; | Yes |

## onSslErrorEvent

```TypeScript
onSslErrorEvent(callback: OnSslErrorEventCallback)
```

Triggered to notify users when an SSL error occurs during the loading of main-frame or subframe resources. To handle SSL errors for loading the main-frame resources, use the [isMainFrame](arkts-arkweb-webresourcerequest-c.md#ismainframe) field to distinguish.

> **NOTE：**&gt;
> - Main resource: Entry file for the browser to load web pages, which is usually an HTML document.&gt;
> - Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is
> encountered during main resource parsing.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-arkweb-onsslerroreventcallback-t.md) | Yes |

## onSslErrorEventReceive

```TypeScript
onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent>)
```

Triggered to notify the host application when an SSL error occurs while loading the main-frame resource.To support errors for loading subframe resources, use the [OnSslErrorEvent](#onsslerrorevent) API.

> **NOTE：**&gt;
> - Main resource: Entry file for the browser to load web pages, which is usually an HTML document.&gt;
> - Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is
> encountered during main resource parsing.&gt;
> - The application needs to call [handler.handleCancel()](arkts-arkweb-sslerrorhandler-c.md#handlecancel) or
> [handler.handleConfirm()](arkts-arkweb-sslerrorhandler-c.md#handleconfirm) to process the callback. Otherwise, resource
> loading is canceled by default. The behavior of **handleConfirm()** or **handleCancel()** may be recorded to
> respond to future SSL errors.&gt;
> - The application can display a custom error page or silently record the problem.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnSslErrorEventReceiveEvent](arkts-arkweb-onsslerroreventreceiveevent-i.md)&gt; | Yes |

## onSslErrorReceive

```TypeScript
onSslErrorReceive(callback: (event?: { handler: Function, error: object }) => void)
```

Triggered when an SSL error occurs during resource loading.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onSslErrorEventReceive](#onsslerroreventreceive)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event?: { handler: Function, error: object }) = & gt; void | Yes |

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: TextSelectionChangeCallback)
```

Triggered when the text selection of the **Web** component changes. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - The gesture selection, mouse selection, and JS selection are supported.&gt;
> - This callback is triggered when the selection ends.&gt;
> - If the same selection is made using the same method as the previous one, this callback is not triggered. If the
> same selection is made using a different method from the previous one, this callback is triggered.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-arkweb-textselectionchangecallback-t.md) | Yes |

## onTitleReceive

```TypeScript
onTitleReceive(callback: Callback<OnTitleReceiveEvent>)
```

Called when the **\&lt;title&gt;** element of the page document changes. If no title is set on the current page, ArkWeb generates a title based on the page URL and returns it to the application before the loading is complete.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnTitleReceiveEvent](arkts-arkweb-ontitlereceiveevent-i.md)&gt; | Yes |

## onTouchIconUrlReceived

```TypeScript
onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent>)
```

Triggered when an apple-touch-icon URL is received.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnTouchIconUrlReceivedEvent](arkts-arkweb-ontouchiconurlreceivedevent-i.md)&gt; | Yes |

## onUrlLoadIntercept

```TypeScript
onUrlLoadIntercept(callback: (event?: { data: string | WebResourceRequest }) => boolean)
```

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** onLoadIntercept

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event?: { data: string \| WebResourceRequest }) = & gt; boolean | Yes |

## onVerifyPin

```TypeScript
onVerifyPin(callback: OnVerifyPinCallback)
```

Triggered to notify the user of PIN verification. This API uses an asynchronous callback to return the result.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-arkweb-onverifypincallback-t.md) | Yes |

## onViewportFitChanged

```TypeScript
onViewportFitChanged(callback: OnViewportFitChangedCallback)
```

Triggered when the **viewport-fit** configuration in the web page's **meta** tag changes. The application can adapt its layout to the viewport within this callback.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-arkweb-onviewportfitchangedcallback-t.md) | Yes |

## onWindowExit

```TypeScript
onWindowExit(callback: () => void)
```

Triggered when this window is closed. This API works in the same way as [onWindowNew](#onwindownew). For security, applications should notify users that the pages they interact with are closed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onWindowNew

```TypeScript
onWindowNew(callback: Callback<OnWindowNewEvent>)
```

Triggered to notify the user of a new window creation request, when **multiWindowAccess** is enabled.If the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is not called, the render process will be blocked.If no new window is created, set this parameter to **null** when invoking the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API to notify the **Web** component that no new window is created.The new window cannot be directly overlaid on the original **Web** component, and its URL (for example, address bar) must be clearly displayed in the same way as the main page to prevent confusion. If visible management of trusted URLs cannot be implemented, consider prohibiting the creation of new windows.Note that the source of a new window request cannot be reliably traced. The request may be initiated by a third- party iframe. By default, the application needs to take defense measures such as sandbox isolation and permission restriction to ensure security.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnWindowNewEvent](arkts-arkweb-onwindownewevent-i.md)&gt; | Yes |

## onWindowNewExt

```TypeScript
onWindowNewExt(callback: Callback<OnWindowNewExtEvent>)
```

Triggered to notify the user of a new window creation request when [multiWindowAccess](#multiwindowaccess) is enabled.

> **NOTE：**&gt;
> - If the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is not called, the render process will
> be blocked.&gt;
> - If no new window is created, the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is called and
> set to **null**, notifying the web page that no new window is created.&gt;
> - The new window cannot be directly overlaid on the original **Web** component, and its URL (for example, address
> bar) must be clearly displayed in the same way as the main page to prevent confusion. If the URL display and
> verification mechanism cannot be ensured to be reliable, you need to disable the creation of new windows.&gt;
> - The source of a new window request cannot be reliably traced. The request may be initiated by a third-party
> iframe. By default, the application needs to take defense measures such as sandbox isolation and permission
> restriction to ensure security.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[OnWindowNewExtEvent](arkts-arkweb-onwindownewextevent-i.md)&gt; | Yes |

## optimizeParserBudget

```TypeScript
optimizeParserBudget(optimizeParserBudget: boolean)
```

Sets whether to enable segment-based HTML parsing optimization. If no attribute is explicitly called, the parsing time is used as the segment point by default.To avoid occupying too many main thread resources and enable progressive loading of web pages, the ArkWeb kernel uses the segment-based parsing policy when parsing the HTML files. By default, the ArkWeb kernel uses the parsing time as the segment point. When the parsing time exceeds the threshold, the parsing is interrupted and then the layout and rendering operations are performed.After optimization is enabled, the ArkWeb kernel not only checks whether the parsing time exceeds the limit, but also additionally determines whether the number of parsed tokens (the smallest parsing units of an HTML document, such as `&lt;div&gt;`, `attr="xxx"`, etc.) exceeds the threshold specified by the kernel, and lowers this threshold. When the FCP (First Contentful Paint) of the page is triggered, the default interrupt judgment logic is restored. This makes the parsing operations before FCP more frequent, thereby increasing the possibility that the first-frame content is parsed and enters the rendering phase earlier, while effectively reducing the rendering workload of the first frame, ultimately advancing the FCP time.When the FCP of a page is triggered, the default segment parsing logic is restored. Therefore, the segment-based HTML parsing optimization takes effect only for the first page loaded by each **Web** component.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [optimizeParserBudget](#optimizeparserbudget) | boolean | Yes |

## overScrollMode

```TypeScript
overScrollMode(mode: OverScrollMode)
```

Sets the over-scroll mode of the **Web** component. When enabled, if the user scrolls to the edge of the root web page, the **Web** component bounces back with an elastic animation, and inner pages on the root page do not trigger the bounce effect. If this attribute is not explicitly called, the over-scroll mode is disabled by default.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [OverScrollMode](arkts-arkweb-overscrollmode-e.md) | Yes |

## overviewModeAccess

```TypeScript
overviewModeAccess(overviewModeAccess: boolean)
```

Sets whether to load web pages by using the overview mode. That is, zoom out the content to fit the screen width. When this attribute is not explicitly called, web pages can be loaded in overview mode by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [overviewModeAccess](#overviewmodeaccess) | boolean | Yes |

## password

```TypeScript
password(password: boolean)
```

Sets whether to save the password. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** enableAutofill

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [password](#password) | boolean | Yes |

## pinchSmooth

```TypeScript
pinchSmooth(isEnabled: boolean)
```

Sets whether to enable pinch smooth mode for the web page. When this attribute is not explicitly called, pinch smooth mode is disabled by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | boolean | Yes |

## registerNativeEmbedRule

```TypeScript
registerNativeEmbedRule(tag: string, type:string)
```

Registers the HTML tag name and type for same-layer rendering. The tag name only supports &lt;object\&gt; and &lt;embed\&gt;. The tag type only supports visible ASCII characters.If the specified type is the same as the W3C standard &lt;object\&gt; or &lt;embed\&gt; type, the ArkWeb kernel identifies the type as a non-same-layer tag.This API is also controlled by **enableNativeEmbedMode** and does not take effect when same-layer rendering is disabled. When this API is not used, the ArkWeb kernel recognizes the &lt;embed\&gt; tags with the "native/" prefix as same-layer tags.For details, see [Using Same-Layer Rendering](../../../web/web-same-layer.md#rendering-text-boxes-at-the-same-layer-on-web-pages).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tag | string | Yes |
| type | string | Yes |

## rotateRenderEffect

```TypeScript
rotateRenderEffect(effect: WebRotateEffect)
```

Sets how the final state of the **Web** component's content is rendered during its width and height animation process when the component rotates. If this attribute is not explicitly called, by default, the component's content stays at the final size and always aligned with the upper left corner of the component.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [WebRotateEffect](arkts-arkweb-webrotateeffect-e.md) | Yes |

## runJavaScriptOnDocumentEnd

```TypeScript
runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**&gt;
> - The script runs after any JavaScript code on the page, and the DOM tree has already been loaded and rendered at
> that point.&gt;
> - The scripts are executed in the order of the array.&gt;
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes |

## runJavaScriptOnDocumentStart

```TypeScript
runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**&gt;
> - The script is injected after the root element (HTML Element) of the web document is created but before any
> other content is loaded.&gt;
> - The scripts are executed in the order of the array.&gt;
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes |

## runJavaScriptOnHeadEnd

```TypeScript
runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the **head** tag of the DOM tree is parsed, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**&gt;
> - This script is executed in the array order.&gt;
> - If a script with the same content is injected for multiple times, the script is silently deduplicated, not
> displayed, and no notification is displayed. The **scriptRules** of the first injection is used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes |

## scrollbarLayoutPolicy

```TypeScript
scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy)
```

Selects the layout mode of the vertical scrollbar within the **Web** component, used to adapt to the writing direction of different languages. The **CONTENT** mode is suitable for scenarios where the web page CSS **direction** attribute needs to be followed, while the **SYSTEM** mode is suitable for scenarios in multilingual apps where the system language direction needs to be followed, such as for right-to-left languages like Arabic and Hebrew.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-arkweb-scrollbarlayoutpolicy-e.md) | Yes |

## selectionMenuOptions

```TypeScript
selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>)
```

Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.The API only supports the selection of plain text; if the selected content contains images or other non-text elements, the **action** information may display garbled content.

> **NOTE：**&gt;
> When used together with [editMenuOptions](#editmenuoptions), this API does not take effect.

**Since:** 12

**Deprecated since:** 20

**Substitutes:** editMenuOptions

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [expandedMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-selectionmenu-selectionmenuoptions-i.md) | Array&lt;[ExpandedMenuItemOptions](arkts-arkweb-expandedmenuitemoptions-i.md)&gt; | Yes |

## tableData

```TypeScript
tableData(tableData: boolean)
```

Sets whether to save form data. When this attribute is not explicitly called, the **Web** component is allowed to save form data by default. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** enableAutofill

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tableData](#tabledata) | boolean | Yes |

## textAutosizing

```TypeScript
textAutosizing(textAutosizing: boolean)
```

Sets whether to enable automatic font sizing for the **Web** component. When no attribute is explicitly called, automatic font sizing is enabled for the **Web** component by default.After automatic font sizing takes effect, any text smaller than 16 px is enlarged to fall between 16 px and 32 px. This eliminates readability issues on narrow screens (viewport &lt; 980 px) where mobile-specific layouts are absent.

&gt; **NOTE：**&gt;
> - The preconditions for automatic font sizing to take effect are as follows:&gt;
> - The device type should be phone, tablet, wearable, or TV.&gt;
> - The viewport width of the **Web** component is less than 980 px.&gt;
> - The page is text-heavy: font size (px) × character count ≥ 3920.&gt;
> - **metaViewport** is not set on the frontend, or the **metaViewport** does not contain the **width** and
> **initial-scale** attributes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textAutosizing](#textautosizing) | boolean | Yes |

## textZoomAtio

```TypeScript
textZoomAtio(textZoomAtio: number)
```

Sets the text zoom ratio of the page.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [textZoomRatio](#textzoomratio)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textZoomAtio](#textzoomatio) | number | Yes |

## textZoomRatio

```TypeScript
textZoomRatio(textZoomRatio: number)
```

Sets the text zoom ratio of the page. When this attribute is not explicitly called, the default zoom ratio is 100%.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [textZoomRatio](#textzoomratio) | number | Yes |

## userAgent

```TypeScript
userAgent(userAgent: string)
```

Sets the user agent.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** setCustomUserAgent

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [userAgent](#useragent) | string | Yes |

## verticalScrollBarAccess

```TypeScript
verticalScrollBarAccess(verticalScrollBar: boolean)
```

Sets whether to display the vertical scrollbar, including the system default scrollbar and user-defined scrollbars. If this attribute is not explicitly called, the scrollbar is displayed by default.

> **NOTE：**&gt;
> - If an @State decorated variable is used to control the vertical scrollbar visibility, **controller.refresh()**
> must be called for the settings to take effect.&gt;
> - If the vertical scrollbar visibility changes frequently through an @State decorated variable, it is recommended
> that the variable correspond to the **Web** component one by one.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| verticalScrollBar | boolean | Yes |

## webCursiveFont

```TypeScript
webCursiveFont(family: string)
```

Sets the cursive font family of the web page to render HTML elements that use the **cursive** font.When this attribute is not explicitly called, the default cursive font family of the web page is **cursive**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## webFantasyFont

```TypeScript
webFantasyFont(family: string)
```

Sets the fantasy font family of the web page to render HTML elements that use the **fantasy** font.When this attribute is not explicitly called, the default fantasy font family of the web page is **fantasy**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## webFixedFont

```TypeScript
webFixedFont(family: string)
```

Sets the fixed font family of the web page to render HTML elements that use the **monospace** font.When this attribute is not explicitly called, the default fixed font family of the web page is **monospace**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## webSansSerifFont

```TypeScript
webSansSerifFont(family: string)
```

Sets the sans-serif font family of the web page to render HTML elements that use the **sans-serif** font.When this attribute is not explicitly called, the sans-serif font family of the web page is **sans-serif** by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## webSerifFont

```TypeScript
webSerifFont(family: string)
```

Sets the serif font family of the web page to render HTML elements that use the **serif** font.When this attribute is not explicitly called, the default serif font family of the web page is **serif**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## webStandardFont

```TypeScript
webStandardFont(family: string)
```

Sets the standard font family of the web page to render HTML elements whose font style is not specified.When this attribute is not explicitly called, the default standard font family of the web page is **sans-serif**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| family | string | Yes |

## wideViewModeAccess

```TypeScript
wideViewModeAccess(wideViewModeAccess: boolean)
```

Sets whether to support the **viewport** attribute of the HTML **\&lt;meta&gt;** tag. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** [metaViewport](#metaviewport)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [wideViewModeAccess](#wideviewmodeaccess) | boolean | Yes |

## zoomAccess

```TypeScript
zoomAccess(zoomAccess: boolean)
```

Sets whether to support zoom gestures. If this attribute is not explicitly called, zoom gestures are supported by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [zoomAccess](#zoomaccess) | boolean | Yes |

## zoomControlAccess

```TypeScript
zoomControlAccess(zoomControlAccess: boolean)
```

Sets whether to allow zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad.If this attribute is not explicitly called, zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad is allowed by default.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [zoomControlAccess](#zoomcontrolaccess) | boolean | Yes |
