# @ohos.accessibility.config(System Accessibility Configuration)

The **accessibility.config** module provides APIs for configuring system accessibility features, including accessibility extension, high-contrast text, mouse buttons, and captions.

**Since:** 9

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import config from '@kit.AccessibilityKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [disableAbility(System Accessibility Configuration)](arkts-accessibility-config-disableability-f-sys.md) | Disables an accessibility extension. This API must be used together with [config.enableAbility](arkts-accessibility-config-enableability-f-sys.md) or [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md). This API uses a promise to return the result. |
| [disableAbility(System Accessibility Configuration)](arkts-accessibility-config-disableability-f-sys.md) | Disables an accessibility extension. This API must be used together with [config.enableAbility](arkts-accessibility-config-enableability-f-sys.md) or [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md). This API uses an asynchronous callback to return the result. |
| [enableAbility(System Accessibility Configuration)](arkts-accessibility-config-enableability-f-sys.md) | Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md). This API uses a promise to return the result.Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md). |
| [enableAbility(System Accessibility Configuration)](arkts-accessibility-config-enableability-f-sys.md) | Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md). This API uses an asynchronous callback to return the result.Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md). |
| [enableAbilityWithCallback(System Accessibility Configuration)](arkts-accessibility-config-enableabilitywithcallback-f-sys.md) | Enables an accessibility extension and specifies [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) as the callback for disconnection events of the accessibility extension. This API uses a promise to return the result.When the accessibility extension process is abnormally disconnected, the onDisconnect callback of ConnectCallback will be triggered. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md). |
| [getSeniorModeStateForApp(System Accessibility Configuration)](arkts-accessibility-config-getseniormodestateforapp-f-sys.md) | Queries the senior mode state of an app. This API uses a promise to return the result. |
| off(System Accessibility Configuration) | Cancels the listener for changes in the list of enabled accessibility extensions. This API uses an asynchronous callback to return the result. |
| off(System Accessibility Configuration) | Cancels the listener for changes in the list of installed accessibility extensions. This API uses an asynchronous callback to return the result. |
| [offSeniorModeStateChangeForApp(System Accessibility Configuration)](arkts-accessibility-config-offseniormodestatechangeforapp-f-sys.md) | Cancels the listener for senior mode state change events of all apps. This API uses an asynchronous callback to return the result. |
| on(System Accessibility Configuration) | Adds a listener for changes in the list of enabled accessibility extensions. This API uses an asynchronous callback to return the result.This API must be used together with config.off('enabledAccessibilityExtensionListChange'). Call off to unregister the listener when it is no longer needed to avoid resource leaks. |
| on(System Accessibility Configuration) | Adds a listener for changes in the list of installed accessibility extensions. This API uses an asynchronous callback to return the result.This API must be used together with config.off('installedAccessibilityListChange'). Call off to unregister the listener when it is no longer needed to avoid resource leaks. |
| [onSeniorModeStateChangeForApp(System Accessibility Configuration)](arkts-accessibility-config-onseniormodestatechangeforapp-f-sys.md) | Listens for senior mode state change events of all apps. This API uses an asynchronous callback to return the result. |
| [setMagnificationState(System Accessibility Configuration)](arkts-accessibility-config-setmagnificationstate-f-sys.md) | Sets the enabled state of the magnification effect. The magnification effect depends on the magnification gesture feature. This API takes effect only when the magnification gesture feature is enabled. |
| [setSeniorModeStateForApp(System Accessibility Configuration)](arkts-accessibility-config-setseniormodestateforapp-f-sys.md) | Sets the senior mode state for an app. This API uses a promise to return the result. |
| [startBlinking(System Accessibility Configuration)](arkts-accessibility-config-startblinking-f-sys.md) | Enables the flash or screen for blinking reminders. |
| [stopBlinking(System Accessibility Configuration)](arkts-accessibility-config-stopblinking-f-sys.md) | Stops flash blinking or screen blinking. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AppSeniorModeInfo(System Accessibility Configuration)](arkts-accessibility-config-appseniormodeinfo-i-sys.md) | Senior mode state information of an app. |
| [Config(System Accessibility Configuration)](arkts-accessibility-config-config-i-sys.md) | Implements configuration, acquisition, and listening for properties. |
| [ConnectCallback(System Accessibility Configuration)](arkts-accessibility-config-connectcallback-i-sys.md) | Callback provided when enabling an accessibility extension app through the [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md) API. The callback is invoked when the connection to the accessibility extension app is disconnected. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [BlinkingMode(System Accessibility Configuration)](arkts-accessibility-config-blinkingmode-e-sys.md) | Enumerates the blinking modes. |
| [BlinkingScenario(System Accessibility Configuration)](arkts-accessibility-config-blinkingscenario-e-sys.md) | Enumerates the blinking scenarios. |
| [BlinkResultCode(System Accessibility Configuration)](arkts-accessibility-config-blinkresultcode-e-sys.md) | Enumerates the result codes of blinking operations. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [ClickResponseTime(System Accessibility Configuration)](arkts-accessibility-config-clickresponsetime-t-sys.md) | Click duration of different lengths. |
| [DaltonizationColorFilter(System Accessibility Configuration)](arkts-accessibility-config-daltonizationcolorfilter-t-sys.md) | Color correction filters for different types of color vision deficiency.The configuration takes effect when the daltonization feature is enabled ([daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationstate) is set to **true**). When the daltonization feature is disabled ([daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationstate) is set to **false**), the standard type is displayed. |
| [OnDisconnectCallback(System Accessibility Configuration)](arkts-accessibility-config-ondisconnectcallback-t-sys.md) | Describes the callback to be invoked when the connection to **AccessibilityExtensionAbility** is disconnected. |
| [RepeatClickInterval(System Accessibility Configuration)](arkts-accessibility-config-repeatclickinterval-t-sys.md) | Ignore repeated clicks at different time intervals.The configuration takes effect when the ignore repeated click feature is enabled ([ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignorerepeatclick) is set to **true**). When the ignore repeated click feature is disabled ([ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignorerepeatclick) is set to **false**), the configuration does not take effect. |
<!--DelEnd-->

<!--Del-->
### Constants(System API)

| Name | Description |
| --- | --- |
| [audioBalance(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#audiobalance) | Indicates the configuration for left and right channel volume balance. **-1.0** indicates output from the left channel only; **0.0** indicates balanced output from both channels; **1.0** indicates output from the right channel only. Intermediate values represent a linear ratio of the left and right channel volumes. The value ranges from -1. 0 to 1.0. The default value is **0.0**. |
| [audioMono(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#audiomono) | Indicates the mono audio feature status. The value **true** indicates that the mono audio feature is enabled, and **false** indicates that it is disabled. The default value is **false**. |
| [clickResponseTime(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#clickresponsetime) | Length of time required for a click. |
| [daltonizationState(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#daltonizationstate) | Indicates the color correction feature status. Used together with daltonizationColorFilter. The value **true** indicates that color correction is enabled, and **false** indicates that it is disabled. The default value is **false**. |
| [ignoreRepeatClick(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#ignorerepeatclick) | Whether to ignore repeated clicks. This parameter must be used together with **repeatClickInterval**. The value **true** indicates that the feature of ignoring repeated clicks is enabled, and **false** indicates the opposite.Default value: **false** |
| [repeatClickInterval(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#repeatclickinterval) | Indicates the configuration for the interval of ignoring repeated clicks. Used together with ignoreRepeatClick. This configuration takes effect only when ignoreRepeatClick is set to **true**. The default value is Shortest, indicating the shortest interval. |
| [screenMagnification(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#screenmagnification) | Indicates the configuration of screen magnification. |
| [shortkeyMultiTargets(System Accessibility Configuration)](arkts-accessibility-config-con-sys.md#shortkeymultitargets) | Indicates the multi-target list configuration of the accessibility extension shortcut key. The value is the name of the accessibility extension app, in the format ['bundleName/abilityName']. If the format is incorrect or the name is invalid, the setting does not take effect. |
<!--DelEnd-->
