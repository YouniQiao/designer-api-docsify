# accessibility

Accessibility

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace accessibility--><!--Device-unnamed-declare namespace accessibility-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isOpenAccessibility](arkts-accessibility-accessibility-isopenaccessibility-f.md#isOpenAccessibility) | Checks whether an accessibility application is enabled. This API uses an asynchronous callback to return the result. |
| [isOpenAccessibility](arkts-accessibility-accessibility-isopenaccessibility-f.md#isOpenAccessibility) | Checks whether an accessibility application is enabled. This API uses a promise to return the result. |
| [isOpenAccessibilitySync](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md#isOpenAccessibilitySync) | Checks whether any accessibility application has been enabled in the system. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getAccessibilityExtensionListSync). |
| [isOpenTouchGuide](arkts-accessibility-accessibility-isopentouchguide-f.md#isOpenTouchGuide) | Checks whether touch guide mode is enabled. This API uses an asynchronous callback to return the result. |
| [isOpenTouchGuide](arkts-accessibility-accessibility-isopentouchguide-f.md#isOpenTouchGuide) | Checks whether touch guide mode is enabled. This API uses a promise to return the result. |
| [isOpenTouchGuideSync](arkts-accessibility-accessibility-isopentouchguidesync-f.md#isOpenTouchGuideSync) | Checks whether touch guide mode is enabled. |
| [isScreenReaderOpenSync](arkts-accessibility-accessibility-isscreenreaderopensync-f.md#isScreenReaderOpenSync) | Checks whether screen reader mode is enabled. |
| [getAbilityLists](arkts-accessibility-accessibility-getabilitylists-f.md#getAbilityLists) | Obtains the accessibility application list. This API uses an asynchronous callback to return the result. |
| [getAbilityLists](arkts-accessibility-accessibility-getabilitylists-f.md#getAbilityLists) | Obtains the accessibility application list. This API uses a promise to return the result. |
| [getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md#getAccessibilityExtensionList) | Obtains the accessibility application list. This API uses a promise to return the result. |
| [getAccessibilityExtensionList](arkts-accessibility-accessibility-getaccessibilityextensionlist-f.md#getAccessibilityExtensionList) | Obtains the accessibility application list. This API uses an asynchronous callback to return the result. |
| [getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getAccessibilityExtensionListSync) | Query the list of accessibility applications in the current system, which can be queried by criteria. |
| [sendEvent](arkts-accessibility-accessibility-sendevent-f.md#sendEvent) | Sends an accessibility event. This API uses an asynchronous callback to return the result. |
| [sendEvent](arkts-accessibility-accessibility-sendevent-f.md#sendEvent) | Sends an accessibility event. This API uses a promise to return the result. |
| [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md#sendAccessibilityEvent) | Sends an accessibility event. This API uses an asynchronous callback to return the result. |
| [sendAccessibilityEvent](arkts-accessibility-accessibility-sendaccessibilityevent-f.md#sendAccessibilityEvent) | Sends an accessibility event. This API uses a promise to return the result. |
| [getTouchModeSync](arkts-accessibility-accessibility-gettouchmodesync-f.md#getTouchModeSync) | Queries single- or double-touch mode. |
| on_accessibilityStateChange | Subscribes to the state changes of the accessibility application. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getAccessibilityExtensionListSync). > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > accessibility.off('accessibilityStateChange') > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [onAccessibilityStateChange](arkts-accessibility-accessibility-onaccessibilitystatechange-f.md#onAccessibilityStateChange) | Register the observe of the accessibility state changed. |
| on_touchGuideStateChange | Subscribes to the state changes in touch guide mode. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md#getAccessibilityExtensionListSync). > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > accessibility.off('touchGuideStateChange') > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [onTouchGuideStateChange](arkts-accessibility-accessibility-ontouchguidestatechange-f.md#onTouchGuideStateChange) | Register the observe of the touchGuide state changed. |
| on_screenReaderStateChange | Subscribes to the state changes of the screen reader. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > accessibility.off('screenReaderStateChange') > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [onScreenReaderStateChange](arkts-accessibility-accessibility-onscreenreaderstatechange-f.md#onScreenReaderStateChange) | Register the observe of the screen reader state changed. |
| on_touchModeChange | Subscribes to the single- or double-touch event changes in touch guide mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > accessibility.off('touchModeChange') > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [onTouchModeChange](arkts-accessibility-accessibility-ontouchmodechange-f.md#onTouchModeChange) | Register the observe of the touch mode changed. |
| off_accessibilityStateChange | Unsubscribes from the state changes of the accessibility application. This API uses an asynchronous callback to return the result. |
| [offAccessibilityStateChange](arkts-accessibility-accessibility-offaccessibilitystatechange-f.md#offAccessibilityStateChange) | Unregister the observe of the accessibility state changed. |
| off_touchGuideStateChange | Unsubscribes from the state changes in touch guide mode. This API uses an asynchronous callback to return the result. |
| [offTouchGuideStateChange](arkts-accessibility-accessibility-offtouchguidestatechange-f.md#offTouchGuideStateChange) | Unregister the observe of the touchGuide state changed. |
| off_screenReaderStateChange | Unsubscribes from the state changes of the screen reader. This API uses an asynchronous callback to return the result. |
| [offScreenReaderStateChange](arkts-accessibility-accessibility-offscreenreaderstatechange-f.md#offScreenReaderStateChange) | Unregister the observe of the screen reader state changed. |
| off_touchModeChange | Unsubscribes from the single- or double-touch event changes in touch guide mode. This API uses an asynchronous callback to return the result. |
| [offTouchModeChange](arkts-accessibility-accessibility-offtouchmodechange-f.md#offTouchModeChange) | Unregister the observe of the touch mode changed. |
| [getCaptionsManager](arkts-accessibility-accessibility-getcaptionsmanager-f.md#getCaptionsManager) | Obtains a **CaptionsManager** instance. |
| [onAnimationReduceStateChange](arkts-accessibility-accessibility-onanimationreducestatechange-f.md#onAnimationReduceStateChange) | Subscribes to the state changes in animation reduction mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > [accessibility.offAnimationReduceStateChange](arkts-accessibility-accessibility-offanimationreducestatechange-f.md#offAnimationReduceStateChange) > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [offAnimationReduceStateChange](arkts-accessibility-accessibility-offanimationreducestatechange-f.md#offAnimationReduceStateChange) | Unsubscribes from the state changes in animation reduction mode. This API uses an asynchronous callback to return the result. |
| [isAnimationReduceEnabledSync](arkts-accessibility-accessibility-isanimationreduceenabledsync-f.md#isAnimationReduceEnabledSync) | Checks whether animation reduction mode is enabled with a synchronous method. |
| [isAnimationReduceEnabled](arkts-accessibility-accessibility-isanimationreduceenabled-f.md#isAnimationReduceEnabled) | Checks whether animation reduction mode is enabled. This API uses a promise to return the result. |
| [onFlashReminderStateChange](arkts-accessibility-accessibility-onflashreminderstatechange-f.md#onFlashReminderStateChange) | Subscribes to the state changes in flash alerts mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > [accessibility.offFlashReminderStateChange](arkts-accessibility-accessibility-offflashreminderstatechange-f.md#offFlashReminderStateChange) > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [offFlashReminderStateChange](arkts-accessibility-accessibility-offflashreminderstatechange-f.md#offFlashReminderStateChange) | Unsubscribes from the state changes in flash alerts mode. This API uses an asynchronous callback to return the result. |
| [isFlashReminderEnabledSync](arkts-accessibility-accessibility-isflashreminderenabledsync-f.md#isFlashReminderEnabledSync) | Checks whether flash alerts mode is enabled with a synchronous method. |
| [isFlashReminderEnabled](arkts-accessibility-accessibility-isflashreminderenabled-f.md#isFlashReminderEnabled) | Checks whether flash alerts mode is enabled. This API uses a promise to return the result. |
| [onAudioMonoStateChange](arkts-accessibility-accessibility-onaudiomonostatechange-f.md#onAudioMonoStateChange) | Subscribes to the state changes in mono audio mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > [accessibility.offAudioMonoStateChange](arkts-accessibility-accessibility-offaudiomonostatechange-f.md#offAudioMonoStateChange) > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [offAudioMonoStateChange](arkts-accessibility-accessibility-offaudiomonostatechange-f.md#offAudioMonoStateChange) | Unsubscribes from the state changes in mono audio mode. This API uses an asynchronous callback to return the result. |
| [isAudioMonoEnabledSync](arkts-accessibility-accessibility-isaudiomonoenabledsync-f.md#isAudioMonoEnabledSync) | Checks whether mono audio mode is enabled with a synchronous mode. |
| [isAudioMonoEnabled](arkts-accessibility-accessibility-isaudiomonoenabled-f.md#isAudioMonoEnabled) | Checks whether mono audio mode is enabled. This API uses a promise to return the result. |
| [isSeniorModeEnabled](arkts-accessibility-accessibility-isseniormodeenabled-f.md#isSeniorModeEnabled) | Checks whether the senior mode is enabled. This API uses a promise to return the result. |
| [onSeniorModeStateChange](arkts-accessibility-accessibility-onseniormodestatechange-f.md#onSeniorModeStateChange) | Listens for enabling status changes of the senior mode. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registering a listener must use a named function instead of an anonymous function. > Otherwise, a new underlying object is created each time the function is called, causing memory leakage. > > - After calling this method, you must use > [accessibility.offSeniorModeStateChange](arkts-accessibility-accessibility-offseniormodestatechange-f.md#offSeniorModeStateChange) > to cancel the listener before the object's lifecycle ends. Otherwise, a crash may occur. |
| [offSeniorModeStateChange](arkts-accessibility-accessibility-offseniormodestatechange-f.md#offSeniorModeStateChange) | Cancels listening for the senior mode change event. This API uses an asynchronous callback to return the result. |
| [onSeniorModeStateChangeForSelf](arkts-accessibility-accessibility-onseniormodestatechangeforself-f.md#onSeniorModeStateChangeForSelf) | Register an observer for this application's senior mode state changes. |
| [offSeniorModeStateChangeForSelf](arkts-accessibility-accessibility-offseniormodestatechangeforself-f.md#offSeniorModeStateChangeForSelf) | Unregister the observer for this application's senior mode state changes. |
| [getSeniorModeStateForSelf](arkts-accessibility-accessibility-getseniormodestateforself-f.md#getSeniorModeStateForSelf) | Check if this application's senior mode is enabled. |
| [setSeniorModeStateForSelf](arkts-accessibility-accessibility-setseniormodestateforself-f.md#setSeniorModeStateForSelf) | Set this application's senior mode. |

### Classes

| Name | Description |
| --- | --- |
| [EventInfo](arkts-accessibility-accessibility-eventinfo-c.md) | Describes a GUI change event. |

### Interfaces

| Name | Description |
| --- | --- |
| [CaptionsManager](arkts-accessibility-accessibility-captionsmanager-i.md) | Implements configuration management for captions. Before calling any API of **CaptionsManager**, you must use the [accessibility.getCaptionsManager()](arkts-accessibility-accessibility-getcaptionsmanager-f.md#getCaptionsManager) API to obtain a **CaptionsManager** instance. |
| [CaptionsStyle](arkts-accessibility-accessibility-captionsstyle-i.md) | Describes the style of captions. |
| [AccessibilityAbilityInfo](arkts-accessibility-accessibility-accessibilityabilityinfo-i.md) | Provides information about an accessibility application. |

### Types

| Name | Description |
| --- | --- |
| [AbilityType](arkts-accessibility-accessibility-abilitytype-t.md) | Enumerates the types of accessibility applications. |
| [Action](arkts-accessibility-accessibility-action-t.md) | Target actions supported by the application. The target actions for which parameters need to be set have been specified in the description of the following table. |
| [EventType](arkts-accessibility-accessibility-eventtype-t.md) | Accessibility event types. |
| [WindowUpdateType](arkts-accessibility-accessibility-windowupdatetype-t.md) | Window update type. |
| [AbilityState](arkts-accessibility-accessibility-abilitystate-t.md) | Enumerates the states of an accessibility application. |
| [Capability](arkts-accessibility-accessibility-capability-t.md) | Enumerates the capabilities of an accessibility application. |
| [TextMoveUnit](arkts-accessibility-accessibility-textmoveunit-t.md) | Enumerates the movement units for traversing the node text. |
| [CaptionsFontEdgeType](arkts-accessibility-accessibility-captionsfontedgetype-t.md) | Enumerates the font edge types of captions. |
| [CaptionsFontFamily](arkts-accessibility-accessibility-captionsfontfamily-t.md) | Enumerates the font families of captions. |

