# accessibility(Accessibility)

This module provides accessibility features, including obtaining the accessibility application list, obtaining the accessibility application enabling state, obtaining the captions configuration, sending accessibility events, and listening for accessibility application state changes.

**Since:** 7

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import config from '@kit.AccessibilityKit.config';
import accessibility from '@kit.AccessibilityKit';
import { GesturePath } from '@kit.AccessibilityKit.GesturePath';
import { GesturePoint } from '@kit.AccessibilityKit.GesturePoint';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isOpenAccessibility(Accessibility)](arkts-accessibility-accessibility-isopenaccessibility-f.md) | Checks whether an accessibility application is enabled. This API uses an asynchronous callback to return the result. |
| [isOpenAccessibility(Accessibility)](arkts-accessibility-accessibility-isopenaccessibility-f.md) | Checks whether an accessibility application is enabled. This API uses a promise to return the result. |
| [isOpenAccessibilitySync(Accessibility)](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md) | Checks whether any accessibility application has been enabled in the system.To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md). |
| [isOpenTouchGuide(Accessibility)](arkts-accessibility-accessibility-isopentouchguide-f.md) | Checks whether touch guide mode is enabled. This API uses an asynchronous callback to return the result. |
| [isOpenTouchGuide(Accessibility)](arkts-accessibility-accessibility-isopentouchguide-f.md) | Checks whether touch guide mode is enabled. This API uses a promise to return the result. |
| [isOpenTouchGuideSync(Accessibility)](arkts-accessibility-accessibility-isopentouchguidesync-f.md) | Checks whether touch guide mode is enabled. |
| [isScreenReaderOpenSync(Accessibility)](arkts-accessibility-accessibility-isscreenreaderopensync-f.md) | Checks whether screen reader mode is enabled. |
| [getAbilityLists(Accessibility)](arkts-accessibility-accessibility-getabilitylists-f.md) | Obtains the accessibility application list. This API uses an asynchronous callback to return the result. |
| [getAbilityLists(Accessibility)](arkts-accessibility-accessibility-getabilitylists-f.md) | Obtains the accessibility application list. This API uses a promise to return the result. |
| [getAccessibilityExtensionList(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) | Obtains the accessibility application list. This API uses a promise to return the result. |
| [getAccessibilityExtensionList(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) | Obtains the accessibility application list. This API uses an asynchronous callback to return the result. |
| [getAccessibilityExtensionListSync(Accessibility)](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md) | Query the list of accessibility applications in the current system, which can be queried by criteria.This API is the synchronous version of [accessibility.getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios. |
| [sendEvent(Accessibility)](arkts-accessibility-accessibility-sendevent-f.md) | Sends an accessibility event. The event will be distributed to registered accessibility extension applications that match the event type for response. This API uses an asynchronous callback to return the result. |
| [sendEvent(Accessibility)](arkts-accessibility-accessibility-sendevent-f.md) | Sends an accessibility event. The event will be distributed to registered accessibility extension applications that match the event type for response. This API uses a promise to return the result. |
| [sendAccessibilityEvent(Accessibility)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) | Sends an accessibility event. The event will be distributed to registered accessibility applications that match the event type for response. This API uses an asynchronous callback to return the result. |
| [sendAccessibilityEvent(Accessibility)](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) | Sends an accessibility event. The event will be distributed to registered accessibility extension applications that match the event type for response. This API uses a promise to return the result. |
| [getTouchModeSync(Accessibility)](arkts-accessibility-accessibility-gettouchmodesync-f.md) | Obtains the single-tap/number-tap operation mode in touch guide mode. This can be used to adjust the app's interaction response mode based on the current operation mode (for example, responding directly to taps in single- tap mode, or requiring number-tap confirmation in number-tap mode). |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#onaccessibilitystatechange) | Subscribes to the state changes of the accessibility application. This API uses an asynchronous callback to return the result.To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md). |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#ontouchguidestatechange) | Subscribes to the state changes of touch guide mode. This API uses an asynchronous callback to return the result.To obtain information about accessibility applications in the system, you are advised to use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md). |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#onscreenreaderstatechange) | Subscribes to the state changes of screen reader mode. This API uses an asynchronous callback to return the result. |
| [on(Accessibility)](arkts-accessibility-accessibility-on-f.md#ontouchmodechange) | Subscribes to the single-tap/number-tap operation mode change event in touch guide mode. This API uses an asynchronous callback to return the result. |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offaccessibilitystatechange) | Unsubscribes from the state changes of the accessibility application. This API uses an asynchronous callback to return the result. |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offtouchguidestatechange) | Unsubscribes from the state changes of touch guide mode. This API uses an asynchronous callback to return the result. |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offscreenreaderstatechange) | Unsubscribes from the state changes of screen reader mode. This API uses an asynchronous callback to return the result. |
| [off(Accessibility)](arkts-accessibility-accessibility-off-f.md#offtouchmodechange) | Unsubscribes from the single-tap/number-tap operation mode change event in touch guide mode. This API uses an asynchronous callback to return the result. |
| [getCaptionsManager(Accessibility)](arkts-accessibility-accessibility-getcaptionsmanager-f.md) | Obtains a **CaptionsManager** instance. |
| [onAnimationReduceStateChange(Accessibility)](arkts-accessibility-accessibility-onanimationreducestatechange-f.md) | Subscribes to the state changes of animation reduction mode. This API uses an asynchronous callback to return the result. |
| [offAnimationReduceStateChange(Accessibility)](arkts-accessibility-accessibility-offanimationreducestatechange-f.md) | Unsubscribes from the state changes in animation reduction mode. This API uses an asynchronous callback to return the result. |
| [isAnimationReduceEnabledSync(Accessibility)](arkts-accessibility-accessibility-isanimationreduceenabledsync-f.md) | Checks whether animation reduction mode is enabled.This API is the synchronous version of [accessibility.isAnimationReduceEnabled](arkts-accessibility-accessibility-isanimationreduceenabled-f.md) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios. |
| [isAnimationReduceEnabled(Accessibility)](arkts-accessibility-accessibility-isanimationreduceenabled-f.md) | Checks whether animation reduction mode is enabled. This API uses a promise to return the result. |
| [onFlashReminderStateChange(Accessibility)](arkts-accessibility-accessibility-onflashreminderstatechange-f.md) | Subscribes to the state changes of flash alerts mode. This API uses an asynchronous callback to return the result. |
| [offFlashReminderStateChange(Accessibility)](arkts-accessibility-accessibility-offflashreminderstatechange-f.md) | Unsubscribes from the state changes in flash alerts mode. This API uses an asynchronous callback to return the result. |
| [isFlashReminderEnabledSync(Accessibility)](arkts-accessibility-accessibility-isflashreminderenabledsync-f.md) | Checks whether flash alerts mode is enabled.This API is the synchronous version of [accessibility.isFlashReminderEnabled](arkts-accessibility-accessibility-isflashreminderenabled-f.md) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios. |
| [isFlashReminderEnabled(Accessibility)](arkts-accessibility-accessibility-isflashreminderenabled-f.md) | Checks whether flash alerts mode is enabled. This API uses a promise to return the result. |
| [onAudioMonoStateChange(Accessibility)](arkts-accessibility-accessibility-onaudiomonostatechange-f.md) | Subscribes to the state changes of mono audio mode. This API uses an asynchronous callback to return the result. |
| [offAudioMonoStateChange(Accessibility)](arkts-accessibility-accessibility-offaudiomonostatechange-f.md) | Unsubscribes from the state changes in mono audio mode. This API uses an asynchronous callback to return the result. |
| [isAudioMonoEnabledSync(Accessibility)](arkts-accessibility-accessibility-isaudiomonoenabledsync-f.md) | Checks whether mono audio mode is enabled.This API is the synchronous version of [accessibility.isAudioMonoEnabled](arkts-accessibility-accessibility-isaudiomonoenabled-f.md) (asynchronous version). They have the same functionality. Use this API if you need to obtain the result immediately. Use the asynchronous version if you need to query in non-blocking scenarios. |
| [isAudioMonoEnabled(Accessibility)](arkts-accessibility-accessibility-isaudiomonoenabled-f.md) | Checks whether mono audio mode is enabled. This API uses a promise to return the result. |
| [isSeniorModeEnabled(Accessibility)](arkts-accessibility-accessibility-isseniormodeenabled-f.md) | Checks whether the senior mode is enabled. This API uses a promise to return the result. |
| [onSeniorModeStateChange(Accessibility)](arkts-accessibility-accessibility-onseniormodestatechange-f.md) | Subscribes to the state changes of the senior mode. This API uses an asynchronous callback to return the result. |
| [offSeniorModeStateChange(Accessibility)](arkts-accessibility-accessibility-offseniormodestatechange-f.md) | Unsubscribes from the state changes of the senior mode. This API uses an asynchronous callback to return the result. |
| [onSeniorModeStateChangeForSelf(Accessibility)](arkts-accessibility-accessibility-onseniormodestatechangeforself-f.md) | Subscribes to the "senior mode" change event of the app itself. This API uses an asynchronous callback to return the result.Unlike [accessibility.onSeniorModeStateChange](arkts-accessibility-accessibility-onseniormodestatechange-f.md), which listens for system-level senior mode state changes, this API only monitors the state of the app itself. |
| [offSeniorModeStateChangeForSelf(Accessibility)](arkts-accessibility-accessibility-offseniormodestatechangeforself-f.md) | Unsubscribes from the "senior mode" change event of the app itself. This API uses an asynchronous callback to return the result. |
| [getSeniorModeStateForSelf(Accessibility)](arkts-accessibility-accessibility-getseniormodestateforself-f.md) | Checks whether the app has "senior mode" enabled. This API uses a promise to return the result.Unlike [accessibility.isSeniorModeEnabled](arkts-accessibility-accessibility-isseniormodeenabled-f.md), which checks whether the system-level senior mode is enabled, this API only queries the state of the app itself. |
| [setSeniorModeStateForSelf(Accessibility)](arkts-accessibility-accessibility-setseniormodestateforself-f.md) | Sets whether the app has "senior mode" enabled. This API uses a promise to return the result. |

### Classes

| Name | Description |
| --- | --- |
| [EventInfo(Accessibility)](arkts-accessibility-accessibility-eventinfo-c.md) | Defines the accessibility event information, which describes UI changes or interaction events. It is used as a parameter of [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md) to define the event type and trigger action. The sent accessibility event will be distributed by the system to registered accessibility applications that match the event type for response. For details, see [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md). |

### Interfaces

| Name | Description |
| --- | --- |
| [CaptionsManager(Accessibility)](arkts-accessibility-accessibility-captionsmanager-i.md) | Manages captions configuration. Before calling any method of **CaptionsManager**, call [accessibility.getCaptionsManager()](arkts-accessibility-accessibility-getcaptionsmanager-f.md) to obtain a **CaptionsManager** instance. |
| [CaptionsStyle(Accessibility)](arkts-accessibility-accessibility-captionsstyle-i.md) | Describes the style of captions. |
| [AccessibilityAbilityInfo(Accessibility)](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md) | Provides information about an accessibility application. |

### Types

| Name | Description |
| --- | --- |
| [AbilityType(Accessibility)](arkts-accessibility-accessibility-abilitytype-t.md) | Enumerates the types of accessibility applications. |
| [Action(Accessibility)](arkts-accessibility-accessibility-action-t.md) | Target actions supported by the app. Target actions that require configuration parameters are indicated in the description column of each action in the table below. |
| [EventType(Accessibility)](arkts-accessibility-accessibility-eventtype-t.md) | Accessibility event types. |
| [WindowUpdateType(Accessibility)](arkts-accessibility-accessibility-windowupdatetype-t.md) | Window update type. |
| [AbilityState(Accessibility)](arkts-accessibility-accessibility-abilitystate-t.md) | Enumerates the states of an accessibility application. |
| [Capability(Accessibility)](arkts-accessibility-accessibility-capability-t.md) | Enumerates the capabilities of an accessibility application. |
| [TextMoveUnit(Accessibility)](arkts-accessibility-accessibility-textmoveunit-t.md) | Enumerates the movement units for traversing the node text. |
| [CaptionsFontEdgeType(Accessibility)](arkts-accessibility-accessibility-captionsfontedgetype-t.md) | Enumerates the font edge types of captions. |
| [CaptionsFontFamily(Accessibility)](arkts-accessibility-accessibility-captionsfontfamily-t.md) | Enumerates the font families of captions. |
