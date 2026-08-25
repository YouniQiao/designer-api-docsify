# @ohos.multimodalAwareness.onScreen(屏上感知)

本模块提供对屏上内容的感知能力，支持获取页面内容、链接、截屏等信息，识别阅读场景、短视频场景等应用场景，提供文章标题、正文等实体信息，以及点击、滚动等交互信息。

> **说明：**&gt;
> 1. 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 2. 本模块为系统接口。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

## 导入模块

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [apperceive(屏上感知)](arkts-multimodalawareness-onscreen-apperceive-f-sys.md) |
| [capture(屏上感知)](arkts-multimodalawareness-onscreen-capture-f-sys.md) |
| [getPageContent(屏上感知)](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md) |
| [interact(屏上感知)](arkts-multimodalawareness-onscreen-interact-f-sys.md) |
| [offReadingScreenPermissionListener(屏上感知)](arkts-multimodalawareness-onscreen-offreadingscreenpermissionlistener-f-sys.md) |
| [onReadingScreenPermissionListener(屏上感知)](arkts-multimodalawareness-onscreen-onreadingscreenpermissionlistener-f-sys.md) |
| [sendControlEvent(屏上感知)](arkts-multimodalawareness-onscreen-sendcontrolevent-f-sys.md) |
| [subscribe(屏上感知)](arkts-multimodalawareness-onscreen-subscribe-f-sys.md) |
| [trigger(屏上感知)](arkts-multimodalawareness-onscreen-trigger-f-sys.md) |
| [unsubscribe(屏上感知)](arkts-multimodalawareness-onscreen-unsubscribe-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AwarenessItem(屏上感知)](arkts-multimodalawareness-onscreen-awarenessitem-i-sys.md) |
| [ContentOptions(屏上感知)](arkts-multimodalawareness-onscreen-contentoptions-i-sys.md) |
| [ControlEvent(屏上感知)](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) |
| [EntityInfo(屏上感知)](arkts-multimodalawareness-onscreen-entityinfo-i-sys.md) |
| [OnscreenAwarenessCap(屏上感知)](arkts-multimodalawareness-onscreen-onscreenawarenesscap-i-sys.md) | 屏上感知能力（包括但不限于阅读场景感知、OCR识别等功能）。参数约束说明：用户可通过能力项（capList）或分组 ID（groupId）使用屏上感知功能。  * 逻辑关系：capList 与 groupId 互为补充必填项，至少需提供其一，且不为空。 * 校验规则：调用接口时，系统会单独检测capList和groupId。 * 能力列表：按能力项或分组ID使用屏上感知功能，具体定义如下。 * capList支持能力列表 按具体业务场景预设的能力，可进行单一订阅或者触发，如下： \|capList支持能力列表\|功能说明\| \| ---- \| ------ \| \|Article\|获取阅读场景的感知信息。\| \|ShortVideo\|获取短视频场景的感知信息。\| \|Todo\|获取待办场景的感知信息。\| \|Activity\|获取基础服务的感知信息。\| \|UiImage\|获取页面内子图信息。\| \|JumpContext\|高亮跳转到指定上下文。\| \|QuickSnap\|获取单次截屏信息。使用规格：仅在capture接口使用，capList仅传递"QuickSnap"时生效，其他使用接口均返回401错误码。\| \|UiTree\|获取页面内JSON树信息。起始版本：26.0.0\| \|InjectEvent\|注入事件。起始版本：26.0.0\| \|CollectStrategy\|获取屏幕采集策略。起始版本：26.0.0\|  * groupId支持能力列表<br> 按业务场景预设的一组能力集合。可统一订阅业务场景，如下： \|groupId支持能力列表\|对应子项能力\|功能说明\| \| ---- \| ------ \| ------\| \|SmartEdge\|Article\|获取阅读场景的感知信息。\| \|SmartEdge\|ShortVideo\|获取短视频场景的感知信息。\| \|SmartEdge\|Todo\|获取待办场景的感知信息。\| \|SmartEdge\|Activity\|获取基础服务的感知信息。\| \|CeliaMemory\|Article\|获取阅读场景的感知信息。\|
| [OnscreenAwarenessInfo(屏上感知)](arkts-multimodalawareness-onscreen-onscreenawarenessinfo-i-sys.md) |
| [OnscreenAwarenessOptions(屏上感知)](arkts-multimodalawareness-onscreen-onscreenawarenessoptions-i-sys.md) |
| [PageContent(屏上感知)](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md) |
| [Paragraph(屏上感知)](arkts-multimodalawareness-onscreen-paragraph-i-sys.md) |
| [ReadingScreenPermissionStatus(屏上感知)](arkts-multimodalawareness-onscreen-readingscreenpermissionstatus-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [CollectStrategy(屏上感知)](arkts-multimodalawareness-onscreen-collectstrategy-e-sys.md) |
| [EventType(屏上感知)](arkts-multimodalawareness-onscreen-eventtype-e-sys.md) |
| [Scenario(屏上感知)](arkts-multimodalawareness-onscreen-scenario-e-sys.md) |
<!--DelEnd-->
