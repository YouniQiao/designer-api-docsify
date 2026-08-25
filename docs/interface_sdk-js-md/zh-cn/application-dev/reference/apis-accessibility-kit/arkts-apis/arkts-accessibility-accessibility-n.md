# accessibility(辅助功能)

本模块提供辅助功能相关能力，包括获取辅助应用列表、获取辅助应用启用状态、获取无障碍字幕配置、发送无障碍事件、监听辅助应用状态变化等。

**起始版本：** 7

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [isOpenAccessibility(辅助功能)](arkts-accessibility-accessibility-isopenaccessibility-f.md) |
| [isOpenAccessibility(辅助功能)](arkts-accessibility-accessibility-isopenaccessibility-f.md) |
| [isOpenAccessibilitySync(辅助功能)](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md) |
| [isOpenTouchGuide(辅助功能)](arkts-accessibility-accessibility-isopentouchguide-f.md) |
| [isOpenTouchGuide(辅助功能)](arkts-accessibility-accessibility-isopentouchguide-f.md) |
| [isOpenTouchGuideSync(辅助功能)](arkts-accessibility-accessibility-isopentouchguidesync-f.md) |
| [getAbilityLists(辅助功能)](arkts-accessibility-accessibility-getabilitylists-f.md) |
| [getAbilityLists(辅助功能)](arkts-accessibility-accessibility-getabilitylists-f.md) |
| [getAccessibilityExtensionList(辅助功能)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) |
| [getAccessibilityExtensionList(辅助功能)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) |
| [getAccessibilityExtensionListSync(辅助功能)](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md) |
| [sendEvent(辅助功能)](arkts-accessibility-accessibility-sendevent-f.md) |
| [sendEvent(辅助功能)](arkts-accessibility-accessibility-sendevent-f.md) |
| [sendAccessibilityEvent(辅助功能)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) |
| [sendAccessibilityEvent(辅助功能)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) |
| [on(辅助功能)](arkts-accessibility-accessibility-on-f.md#onaccessibilitystatechange) |
| [on(辅助功能)](arkts-accessibility-accessibility-on-f.md#ontouchguidestatechange) |
| [off(辅助功能)](arkts-accessibility-accessibility-off-f.md#offaccessibilitystatechange) |
| [off(辅助功能)](arkts-accessibility-accessibility-off-f.md#offtouchguidestatechange) |
| [getCaptionsManager(辅助功能)](arkts-accessibility-accessibility-getcaptionsmanager-f.md) |
| [isScreenReaderOpenSync(辅助功能)](arkts-accessibility-accessibility-isscreenreaderopensync-f.md) |
| [on(辅助功能)](arkts-accessibility-accessibility-on-f.md#onscreenreaderstatechange) |
| [off(辅助功能)](arkts-accessibility-accessibility-off-f.md#offscreenreaderstatechange) |
| [on(辅助功能)](arkts-accessibility-accessibility-on-f.md#ontouchmodechange) |
| [off(辅助功能)](arkts-accessibility-accessibility-off-f.md#offtouchmodechange) |
| [getTouchModeSync(辅助功能)](arkts-accessibility-accessibility-gettouchmodesync-f.md) |
| [onAnimationReduceStateChange(辅助功能)](arkts-accessibility-accessibility-onanimationreducestatechange-f.md) |
| [offAnimationReduceStateChange(辅助功能)](arkts-accessibility-accessibility-offanimationreducestatechange-f.md) |
| [isAnimationReduceEnabledSync(辅助功能)](arkts-accessibility-accessibility-isanimationreduceenabledsync-f.md) |
| [isAnimationReduceEnabled(辅助功能)](arkts-accessibility-accessibility-isanimationreduceenabled-f.md) |
| [onFlashReminderStateChange(辅助功能)](arkts-accessibility-accessibility-onflashreminderstatechange-f.md) |
| [offFlashReminderStateChange(辅助功能)](arkts-accessibility-accessibility-offflashreminderstatechange-f.md) |
| [isFlashReminderEnabledSync(辅助功能)](arkts-accessibility-accessibility-isflashreminderenabledsync-f.md) |
| [isFlashReminderEnabled(辅助功能)](arkts-accessibility-accessibility-isflashreminderenabled-f.md) |
| [onAudioMonoStateChange(辅助功能)](arkts-accessibility-accessibility-onaudiomonostatechange-f.md) |
| [offAudioMonoStateChange(辅助功能)](arkts-accessibility-accessibility-offaudiomonostatechange-f.md) |
| [isAudioMonoEnabledSync(辅助功能)](arkts-accessibility-accessibility-isaudiomonoenabledsync-f.md) |
| [isAudioMonoEnabled(辅助功能)](arkts-accessibility-accessibility-isaudiomonoenabled-f.md) |
| [onSeniorModeStateChange(辅助功能)](arkts-accessibility-accessibility-onseniormodestatechange-f.md) |
| [offSeniorModeStateChange(辅助功能)](arkts-accessibility-accessibility-offseniormodestatechange-f.md) |
| [isSeniorModeEnabled(辅助功能)](arkts-accessibility-accessibility-isseniormodeenabled-f.md) |
| [onSeniorModeStateChangeForSelf(辅助功能)](arkts-accessibility-accessibility-onseniormodestatechangeforself-f.md) |
| [offSeniorModeStateChangeForSelf(辅助功能)](arkts-accessibility-accessibility-offseniormodestatechangeforself-f.md) |
| [getSeniorModeStateForSelf(辅助功能)](arkts-accessibility-accessibility-getseniormodestateforself-f.md) |
| [setSeniorModeStateForSelf(辅助功能)](arkts-accessibility-accessibility-setseniormodestateforself-f.md) |

### 类

| 名称 |
| --- |
| [EventInfo(辅助功能)](arkts-accessibility-accessibility-eventinfo-c.md) |

### 接口

| 名称 |
| --- |
| [CaptionsManager(辅助功能)](arkts-accessibility-accessibility-captionsmanager-i.md) |
| [CaptionsStyle(辅助功能)](arkts-accessibility-accessibility-captionsstyle-i.md) |
| [AccessibilityAbilityInfo(辅助功能)](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md) |

### 类型

| 名称 |
| --- |
| [AbilityType(辅助功能)](arkts-accessibility-accessibility-abilitytype-t.md) |
| [Action(辅助功能)](arkts-accessibility-accessibility-action-t.md) |
| [EventType(辅助功能)](arkts-accessibility-accessibility-eventtype-t.md) |
| [WindowUpdateType(辅助功能)](arkts-accessibility-accessibility-windowupdatetype-t.md) |
| [AbilityState(辅助功能)](arkts-accessibility-accessibility-abilitystate-t.md) |
| [Capability(辅助功能)](arkts-accessibility-accessibility-capability-t.md) |
| [TextMoveUnit(辅助功能)](arkts-accessibility-accessibility-textmoveunit-t.md) |
| [CaptionsFontEdgeType(辅助功能)](arkts-accessibility-accessibility-captionsfontedgetype-t.md) |
| [CaptionsFontFamily(辅助功能)](arkts-accessibility-accessibility-captionsfontfamily-t.md) |
