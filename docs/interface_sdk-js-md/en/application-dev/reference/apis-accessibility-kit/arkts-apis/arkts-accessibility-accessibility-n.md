# accessibility(Accessibility)

This module provides accessibility features, including obtaining the accessibility application list, obtaining the accessibility application enabling state, obtaining the captions configuration, sending accessibility events, and listening for accessibility application state changes.

**Since:** 7

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isOpenAccessibility(Accessibility)](arkts-accessibility-accessibility-isopenaccessibility-f.md) |
| [isOpenAccessibility(Accessibility)](arkts-accessibility-accessibility-isopenaccessibility-f.md) |
| [isOpenAccessibilitySync(Accessibility)](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md) |
| [isOpenTouchGuide(Accessibility)](arkts-accessibility-accessibility-isopentouchguide-f.md) |
| [isOpenTouchGuide(Accessibility)](arkts-accessibility-accessibility-isopentouchguide-f.md) |
| [isOpenTouchGuideSync(Accessibility)](arkts-accessibility-accessibility-isopentouchguidesync-f.md) |
| [isScreenReaderOpenSync(Accessibility)](arkts-accessibility-accessibility-isscreenreaderopensync-f.md) |
| [getAbilityLists(Accessibility)](arkts-accessibility-accessibility-getabilitylists-f.md) |
| [getAbilityLists(Accessibility)](arkts-accessibility-accessibility-getabilitylists-f.md) |
| [getAccessibilityExtensionList(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) |
| [getAccessibilityExtensionList(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) |
| [getAccessibilityExtensionListSync(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md) |
| [sendEvent(Accessibility)](arkts-accessibility-accessibility-sendevent-f.md) |
| [sendEvent(Accessibility)](arkts-accessibility-accessibility-sendevent-f.md) |
| [sendAccessibilityEvent(Accessibility)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) |
| [sendAccessibilityEvent(Accessibility)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) |
| [getTouchModeSync(Accessibility)](arkts-accessibility-accessibility-gettouchmodesync-f.md) |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#onaccessibilitystatechange) |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#ontouchguidestatechange) |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#onscreenreaderstatechange) |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#ontouchmodechange) |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offaccessibilitystatechange) |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offtouchguidestatechange) |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offscreenreaderstatechange) |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offtouchmodechange) |
| [getCaptionsManager(Accessibility)](arkts-accessibility-accessibility-getcaptionsmanager-f.md) |
| [onAnimationReduceStateChange(Accessibility)](arkts-accessibility-accessibility-onanimationreducestatechange-f.md) |
| [offAnimationReduceStateChange(Accessibility)](arkts-accessibility-accessibility-offanimationreducestatechange-f.md) |
| [isAnimationReduceEnabledSync(Accessibility)](arkts-accessibility-accessibility-isanimationreduceenabledsync-f.md) |
| [isAnimationReduceEnabled(Accessibility)](arkts-accessibility-accessibility-isanimationreduceenabled-f.md) |
| [onFlashReminderStateChange(Accessibility)](arkts-accessibility-accessibility-onflashreminderstatechange-f.md) |
| [offFlashReminderStateChange(Accessibility)](arkts-accessibility-accessibility-offflashreminderstatechange-f.md) |
| [isFlashReminderEnabledSync(Accessibility)](arkts-accessibility-accessibility-isflashreminderenabledsync-f.md) |
| [isFlashReminderEnabled(Accessibility)](arkts-accessibility-accessibility-isflashreminderenabled-f.md) |
| [onAudioMonoStateChange(Accessibility)](arkts-accessibility-accessibility-onaudiomonostatechange-f.md) |
| [offAudioMonoStateChange(Accessibility)](arkts-accessibility-accessibility-offaudiomonostatechange-f.md) |
| [isAudioMonoEnabledSync(Accessibility)](arkts-accessibility-accessibility-isaudiomonoenabledsync-f.md) |
| [isAudioMonoEnabled(Accessibility)](arkts-accessibility-accessibility-isaudiomonoenabled-f.md) |
| [isSeniorModeEnabled(Accessibility)](arkts-accessibility-accessibility-isseniormodeenabled-f.md) |
| [onSeniorModeStateChange(Accessibility)](arkts-accessibility-accessibility-onseniormodestatechange-f.md) |
| [offSeniorModeStateChange(Accessibility)](arkts-accessibility-accessibility-offseniormodestatechange-f.md) |
| [onSeniorModeStateChangeForSelf(Accessibility)](arkts-accessibility-accessibility-onseniormodestatechangeforself-f.md) |
| [offSeniorModeStateChangeForSelf(Accessibility)](arkts-accessibility-accessibility-offseniormodestatechangeforself-f.md) |
| [getSeniorModeStateForSelf(Accessibility)](arkts-accessibility-accessibility-getseniormodestateforself-f.md) |
| [setSeniorModeStateForSelf(Accessibility)](arkts-accessibility-accessibility-setseniormodestateforself-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventInfo(Accessibility)](arkts-accessibility-accessibility-eventinfo-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CaptionsManager(Accessibility)](arkts-accessibility-accessibility-captionsmanager-i.md) |
| [CaptionsStyle(Accessibility)](arkts-accessibility-accessibility-captionsstyle-i.md) |
| [AccessibilityAbilityInfo(Accessibility)](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityType(Accessibility)](arkts-accessibility-accessibility-abilitytype-t.md) |
| [Action(Accessibility)](arkts-accessibility-accessibility-action-t.md) |
| [EventType(Accessibility)](arkts-accessibility-accessibility-eventtype-t.md) |
| [WindowUpdateType(Accessibility)](arkts-accessibility-accessibility-windowupdatetype-t.md) |
| [AbilityState(Accessibility)](arkts-accessibility-accessibility-abilitystate-t.md) |
| [Capability(Accessibility)](arkts-accessibility-accessibility-capability-t.md) |
| [TextMoveUnit(Accessibility)](arkts-accessibility-accessibility-textmoveunit-t.md) |
| [CaptionsFontEdgeType(Accessibility)](arkts-accessibility-accessibility-captionsfontedgetype-t.md) |
| [CaptionsFontFamily(Accessibility)](arkts-accessibility-accessibility-captionsfontfamily-t.md) |
