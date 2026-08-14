# @ohos.accessibility.config

The **accessibility.config** module provides APIs for configuring system accessibility features, including accessibility extension, high-contrast text, mouse buttons, and captions. > **NOTE：**> > - The APIs of this module are system APIs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace config--><!--Device-unnamed-declare namespace config-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { config } from 'config';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility) | Disables an accessibility extension. This API must be used together with [config.enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility-(System-API)) or [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)). This API uses a promise to return the result. |
| [disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)) | Disables an accessibility extension. This API must be used together with [config.enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility-(System-API)) or [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)). This API uses an asynchronous callback to return the result. |
| [enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility) | Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)). This API uses a promise to return the result. Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)). |
| [enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility-(System-API)) | Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)). This API uses an asynchronous callback to return the result. Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)). |
| [enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback) | Enables an accessibility extension and specifies [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md#ConnectCallback-(System-API)) as the callback for disconnection events of the accessibility extension. This API uses a promise to return the result. When the accessibility extension process is abnormally disconnected, the onDisconnect callback of ConnectCallback will be triggered. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)). |
| [getSeniorModeStateForApp](arkts-accessibility-config-getseniormodestateforapp-f-sys.md#getSeniorModeStateForApp) | Queries the senior mode state of an app. This API uses a promise to return the result. |
| [offEnabledAccessibilityExtensionListChange](arkts-accessibility-config-offenabledaccessibilityextensionlistchange-f-sys.md#offEnabledAccessibilityExtensionListChange) | Unregister listener that watches for changes in the enabled status of accessibility extensions. |
| [offInstalledAccessibilityListChange](arkts-accessibility-config-offinstalledaccessibilitylistchange-f-sys.md#offInstalledAccessibilityListChange) | Unregister listener that watches for changes in the installed status of accessibility extensions. |
| [offSeniorModeStateChangeForApp](arkts-accessibility-config-offseniormodestatechangeforapp-f-sys.md#offSeniorModeStateChangeForApp) | Cancels the listener for senior mode state change events of all apps. This API uses an asynchronous callback to return the result. |
| off_enabledAccessibilityExtensionListChange | Cancels the listener for changes in the list of enabled accessibility extensions. This API uses an asynchronous callback to return the result. |
| off_installedAccessibilityListChange | Cancels the listener for changes in the list of installed accessibility extensions. This API uses an asynchronous callback to return the result. |
| [onEnabledAccessibilityExtensionListChange](arkts-accessibility-config-onenabledaccessibilityextensionlistchange-f-sys.md#onEnabledAccessibilityExtensionListChange) | Register the listener that watches for changes in the enabled status of accessibility extensions. |
| [onInstalledAccessibilityListChange](arkts-accessibility-config-oninstalledaccessibilitylistchange-f-sys.md#onInstalledAccessibilityListChange) | Register the listener that watches for changes in the installed status of accessibility extensions. |
| [onSeniorModeStateChangeForApp](arkts-accessibility-config-onseniormodestatechangeforapp-f-sys.md#onSeniorModeStateChangeForApp) | Listens for senior mode state change events of all apps. This API uses an asynchronous callback to return the result. > **NOTE：**> > - The callback parameter for registration should use a named function instead of an anonymous function, otherwise > a new underlying object will be created each time it is called, causing memory leaks. > > - After calling this method, be sure to use > [config.offSeniorModeStateChangeForApp](arkts-accessibility-config-offseniormodestatechangeforapp-f-sys.md#offSeniorModeStateChangeForApp-(System-API)) > to cancel the listener before the component instance is destroyed (for example, in the aboutToDisappear lifecycle > ), otherwise crashes may occur. |
| on_enabledAccessibilityExtensionListChange | Adds a listener for changes in the list of enabled accessibility extensions. This API uses an asynchronous callback to return the result. This API must be used together with config.off('enabledAccessibilityExtensionListChange'). Call off to unregister the listener when it is no longer needed to avoid resource leaks. |
| on_installedAccessibilityListChange | Adds a listener for changes in the list of installed accessibility extensions. This API uses an asynchronous callback to return the result. This API must be used together with config.off('installedAccessibilityListChange'). Call off to unregister the listener when it is no longer needed to avoid resource leaks. |
| [setMagnificationState](arkts-accessibility-config-setmagnificationstate-f-sys.md#setMagnificationState) | Sets the enabled state of the magnification effect. The magnification effect depends on the magnification gesture feature. This API takes effect only when the magnification gesture feature is enabled. |
| [setSeniorModeStateForApp](arkts-accessibility-config-setseniormodestateforapp-f-sys.md#setSeniorModeStateForApp) | Sets the senior mode state for an app. This API uses a promise to return the result. |
| [startBlinking](arkts-accessibility-config-startblinking-f-sys.md#startBlinking) | Enables the flash or screen for blinking reminders. |
| [stopBlinking](arkts-accessibility-config-stopblinking-f-sys.md#stopBlinking) | Stops flash blinking or screen blinking. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AppSeniorModeInfo](arkts-accessibility-config-appseniormodeinfo-i-sys.md) | Senior mode state information of an app. |
| [Config](arkts-accessibility-config-config-i-sys.md) | Implements configuration, acquisition, and listening for properties. |
| [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) | Callback provided when enabling an accessibility extension app through the [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)) API. The callback is invoked when the connection to the accessibility extension app is disconnected. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [BlinkResultCode](arkts-accessibility-config-blinkresultcode-e-sys.md) | Enumerates the result codes of blinking operations. |
| [BlinkingMode](arkts-accessibility-config-blinkingmode-e-sys.md) | Enumerates the blinking modes. |
| [BlinkingScenario](arkts-accessibility-config-blinkingscenario-e-sys.md) | Enumerates the blinking scenarios. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ClickResponseTime](arkts-accessibility-config-clickresponsetime-t-sys.md) | Click duration of different lengths. |
| [DaltonizationColorFilter](arkts-accessibility-config-daltonizationcolorfilter-t-sys.md) | The configuration takes effect when the daltonization feature is enabled ( [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **true**). When the daltonization feature is disabled ([daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **false**), the standard type is displayed. |
| [OnDisconnectCallback](arkts-accessibility-config-ondisconnectcallback-t-sys.md) | Describes the callback to be invoked when the connection to **AccessibilityExtensionAbility** is disconnected. |
| [RepeatClickInterval](arkts-accessibility-config-repeatclickinterval-t-sys.md) | The configuration takes effect when the ignore repeated click feature is enabled ( [ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) is set to **true**). When the ignore repeated click feature is disabled ([ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) is set to **false**), the configuration does not take effect. |
<!--DelEnd-->

<!--Del-->
### Constants（系统接口）

| Name | Description |
| --- | --- |
| [audioBalance](arkts-accessibility-config-con-sys.md#audioBalance) | Indicates the configuration for left and right channel volume balance. **-1.0** indicates output from the left channel only; **0.0** indicates balanced output from both channels; **1.0** indicates output from the right channel only. Intermediate values represent a linear ratio of the left and right channel volumes. The value ranges from -1. 0 to 1.0. The default value is **0.0**. |
| [audioMono](arkts-accessibility-config-con-sys.md#audioMono) | Indicates the mono audio feature status. The value **true** indicates that the mono audio feature is enabled, and **false** indicates that it is disabled. The default value is **false**. |
| [clickResponseTime](arkts-accessibility-config-con-sys.md#clickResponseTime) | Length of time required for a click. |
| [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) | Indicates the color correction feature status. Used together with daltonizationColorFilter. The value **true** indicates that color correction is enabled, and **false** indicates that it is disabled. The default value is **false**. |
| [ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) | Whether to ignore repeated clicks. This parameter must be used together with **repeatClickInterval**. The value **true** indicates that the feature of ignoring repeated clicks is enabled, and **false** indicates the opposite. Default value: **false** |
| [repeatClickInterval](arkts-accessibility-config-con-sys.md#repeatClickInterval) | Indicates the configuration for the interval of ignoring repeated clicks. Used together with ignoreRepeatClick. This configuration takes effect only when ignoreRepeatClick is set to **true**. The default value is Shortest, indicating the shortest interval. |
| [screenMagnification](arkts-accessibility-config-con-sys.md#screenMagnification) | Indicates the configuration of screen magnification. |
| [shortkeyMultiTargets](arkts-accessibility-config-con-sys.md#shortkeyMultiTargets) | Indicates the multi-target list configuration of the accessibility extension shortcut key. The value is the name of the accessibility extension app, in the format ['bundleName/abilityName']. If the format is incorrect or the name is invalid, the setting does not take effect. |
<!--DelEnd-->

