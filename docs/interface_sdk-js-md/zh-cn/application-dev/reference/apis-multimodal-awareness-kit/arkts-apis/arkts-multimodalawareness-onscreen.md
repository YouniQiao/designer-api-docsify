# @ohos.multimodalAwareness.onScreen

This module provides the onscreen awareness capability.

> **NOTE：**
> 

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace onScreen--><!--Device-unnamed-declare namespace onScreen-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [apperceive](arkts-multimodalawareness-onscreen-apperceive-f-sys.md#apperceive) | Proactively triggers screen content awareness to obtain the screen content for snapshot analysis. |
| [capture](arkts-multimodalawareness-onscreen-capture-f-sys.md#capture) | Proactively triggers screen content awareness to obtain page information. |
| [getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md#getpagecontent) | Obtains the onscreen content when a window is displayed on the screen. |
| [interact](arkts-multimodalawareness-onscreen-interact-f-sys.md#interact) | Proactively triggers screen behavior interaction to identify screen behaviors and return behavior receipts. For &lt;br&gt; example, after a link is clicked, the system accurately jumps to the specified paragraph and &lt;br&gt; highlights the text based on the receipt information. |
| [offReadingScreenPermissionListener](arkts-multimodalawareness-onscreen-offreadingscreenpermissionlistener-f-sys.md#offreadingscreenpermissionlistener) | Disables the screen content access permission monitoring. |
| [onReadingScreenPermissionListener](arkts-multimodalawareness-onscreen-onreadingscreenpermissionlistener-f-sys.md#onreadingscreenpermissionlistener) | Enables the screen content access permission monitoring and returns the permission status in real time. |
| [sendControlEvent](arkts-multimodalawareness-onscreen-sendcontrolevent-f-sys.md#sendcontrolevent) | If the target window is displayed on the screen, you can use this API to send screen control events based on the paragraph information obtained via [onScreen.getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md#getpagecontent). |
| [subscribe](arkts-multimodalawareness-onscreen-subscribe-f-sys.md#subscribe) | Enables proactive awareness on screen content and subscribes to a screen awareness result. |
| [trigger](arkts-multimodalawareness-onscreen-trigger-f-sys.md#trigger) | Proactively triggers screen content awareness and obtains the current screen awareness result. |
| [unsubscribe](arkts-multimodalawareness-onscreen-unsubscribe-f-sys.md#unsubscribe) | Disables proactive awareness on screen content and unsubscribes from a screen awareness result. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AwarenessItem](arkts-multimodalawareness-onscreen-awarenessitem-i-sys.md) | Provides page information, which includes:  * Basic page information, such as page content, links, and screenshots.  * Page entity information, such as the title and body of a page article.  * Page interaction information, such as clicks and scrolling. |
| [ContentOptions](arkts-multimodalawareness-onscreen-contentoptions-i-sys.md) | Defines the options for obtaining the onscreen content. |
| [ControlEvent](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) | Defines a control event. |
| [EntityInfo](arkts-multimodalawareness-onscreen-entityinfo-i-sys.md) | Provides entity information perceived, including content, links, images, and other types of entities. |
| [OnscreenAwarenessCap](arkts-multimodalawareness-onscreen-onscreenawarenesscap-i-sys.md) | Defines onscreen awareness capabilities (including but not limited to awareness in a reading scenario and OCR). |
| [OnscreenAwarenessInfo](arkts-multimodalawareness-onscreen-onscreenawarenessinfo-i-sys.md) | Returns the list of onscreen awareness information. |
| [OnscreenAwarenessOptions](arkts-multimodalawareness-onscreen-onscreenawarenessoptions-i-sys.md) | Defines the list of onscreen awareness parameters, which is used to obtain onscreen information in specific scenarios. For example, a window ID is provided to collect application UI content and links. |
| [PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md) | Defines the onscreen content. |
| [Paragraph](arkts-multimodalawareness-onscreen-paragraph-i-sys.md) | Defines the paragraph information. |
| [ReadingScreenPermissionStatus](arkts-multimodalawareness-onscreen-readingscreenpermissionstatus-i-sys.md) | Returns the status of the permission for reading screen information. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [CollectStrategy](arkts-multimodalawareness-onscreen-collectstrategy-e-sys.md) | Defines a page information collection policy. |
| [EventType](arkts-multimodalawareness-onscreen-eventtype-e-sys.md) | Enumerates the control event types. |
| [Scenario](arkts-multimodalawareness-onscreen-scenario-e-sys.md) | Enumerates the scenarios of the onscreen content. |
<!--DelEnd-->

