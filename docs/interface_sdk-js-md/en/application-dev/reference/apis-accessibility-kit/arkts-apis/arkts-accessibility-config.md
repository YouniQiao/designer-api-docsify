# @ohos.accessibility.config

The **accessibility.config** module provides APIs for configuring system accessibility features, including accessibility extension, high-contrast text, mouse buttons, and captions.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace config--><!--Device-unnamed-declare namespace config-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility) | Disables an accessibility extension ability. This API uses a promise to return the result. |
| [disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)) | Disables an accessibility extension ability. This API uses an asynchronous callback to return the result. |
| [enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility) | Enables an accessibility extension ability. This API uses a promise to return the result. |
| [enableAbility](arkts-accessibility-config-enableability-f-sys.md#enableAbility-(System-API)) | Enables an accessibility extension ability. This API uses an asynchronous callback to return the result. |
| [enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback) | Enables the auxiliary extension ability and specifies [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md#ConnectCallback-(System-API)) to be invoked when the state of an auxiliary extension ability changes. This API uses a promise to return the result. |
| [getSeniorModeStateForApp](arkts-accessibility-config-getseniormodestateforapp-f-sys.md#getSeniorModeStateForApp) | Get the senior mode state for app. |
| [offEnabledAccessibilityExtensionListChange](arkts-accessibility-config-offenabledaccessibilityextensionlistchange-f-sys.md#offEnabledAccessibilityExtensionListChange) | Unregister listener that watches for changes in the enabled status of accessibility extensions. |
| [offInstalledAccessibilityListChange](arkts-accessibility-config-offinstalledaccessibilitylistchange-f-sys.md#offInstalledAccessibilityListChange) | Unregister listener that watches for changes in the installed status of accessibility extensions. |
| [offSeniorModeStateChangeForApp](arkts-accessibility-config-offseniormodestatechangeforapp-f-sys.md#offSeniorModeStateChangeForApp) | Unregister the observer for application's senior mode state changes. |
| off_enabledAccessibilityExtensionListChange | Cancels a listener for changes in the list of enabled accessibility extension abilities. This API uses an asynchronous callback to return the result. |
| off_installedAccessibilityListChange | Cancels a listener for changes in the list of installed accessibility extension abilities. This API uses an asynchronous callback to return the result. |
| [onEnabledAccessibilityExtensionListChange](arkts-accessibility-config-onenabledaccessibilityextensionlistchange-f-sys.md#onEnabledAccessibilityExtensionListChange) | Register the listener that watches for changes in the enabled status of accessibility extensions. |
| [onInstalledAccessibilityListChange](arkts-accessibility-config-oninstalledaccessibilitylistchange-f-sys.md#onInstalledAccessibilityListChange) | Register the listener that watches for changes in the installed status of accessibility extensions. |
| [onSeniorModeStateChangeForApp](arkts-accessibility-config-onseniormodestatechangeforapp-f-sys.md#onSeniorModeStateChangeForApp) | Register an observer for anyone application's senior mode state changes. |
| on_enabledAccessibilityExtensionListChange | Adds a listener for changes in the list of enabled accessibility extension abilities. This API uses an asynchronous callback to return the result. |
| on_installedAccessibilityListChange | Adds a listener for changes in the list of installed accessibility extension abilities. This API uses an asynchronous callback to return the result. |
| [setMagnificationState](arkts-accessibility-config-setmagnificationstate-f-sys.md#setMagnificationState) | Sets the magnification state. Ensure that magnification is enabled before calling this API. |
| [setSeniorModeStateForApp](arkts-accessibility-config-setseniormodestateforapp-f-sys.md#setSeniorModeStateForApp) | Set the senior mode state for app. |
| [startBlinking](arkts-accessibility-config-startblinking-f-sys.md#startBlinking) | Enable the flash or screen to blink for flash alert. |
| [stopBlinking](arkts-accessibility-config-stopblinking-f-sys.md#stopBlinking) | Stop the flash or screen to blink for flash alert. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AppSeniorModeInfo](arkts-accessibility-config-appseniormodeinfo-i-sys.md) | Indicates the senior mode information of an application. |
| [Config](arkts-accessibility-config-config-i-sys.md) | Implements configuration, acquisition, and listening for properties. |
| [ConnectCallback](arkts-accessibility-config-connectcallback-i-sys.md) | Callback provided when the [enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)) API is called to enable an accessibility extension ability. This callback will be invoked when the connection to an auxiliary extension ability is disconnected. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [BlinkResultCode](arkts-accessibility-config-blinkresultcode-e-sys.md) | Enumerates the result codes for blinking operations. |
| [BlinkingMode](arkts-accessibility-config-blinkingmode-e-sys.md) | Blinking Mode Enumeration |
| [BlinkingScenario](arkts-accessibility-config-blinkingscenario-e-sys.md) | Blinking Scenario Enumeration |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ClickResponseTime](arkts-accessibility-config-clickresponsetime-t-sys.md) | Defines the length of time for a click. |
| [DaltonizationColorFilter](arkts-accessibility-config-daltonizationcolorfilter-t-sys.md) | Enumerates the daltonization filters. The configuration of **DaltonizationColorFilter** takes effect only when [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **true**; the normal type is used when [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) is set to **false**. |
| [OnDisconnectCallback](arkts-accessibility-config-ondisconnectcallback-t-sys.md) | Describes the callback to be invoked when the connection to **AccessibilityExtensionAbility** is disconnected. |
| [RepeatClickInterval](arkts-accessibility-config-repeatclickinterval-t-sys.md) | Defines the interval between repeated clicks. The configuration of **RepeatClickInterval** takes effect when [ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) is set to **true**; the normal type is used when [ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) is set to **false**. |
<!--DelEnd-->

<!--Del-->
### Constants（系统接口）

| Name | Description |
| --- | --- |
| [audioBalance](arkts-accessibility-config-con-sys.md#audioBalance) | Audio balance for the left and right audio channels. The value ranges from -1.0 to 1.0. Default value: **0.0** |
| [audioMono](arkts-accessibility-config-con-sys.md#audioMono) | Whether to enable mono audio. The value **true** indicates that mono audio is enabled, and **false** indicates the opposite. Default value: **false** |
| [clickResponseTime](arkts-accessibility-config-con-sys.md#clickResponseTime) | Length of time required for a click. |
| [daltonizationState](arkts-accessibility-config-con-sys.md#daltonizationState) | Whether to enable daltonization. It must be used with **daltonizationColorFilter**. The value **true** indicates that daltonization is enabled, and **false** indicates the opposite. Default value: **false** |
| [ignoreRepeatClick](arkts-accessibility-config-con-sys.md#ignoreRepeatClick) | Whether to ignore repeated clicks. This parameter must be used together with **repeatClickInterval**. The value **true** indicates that the feature of ignoring repeated clicks is enabled, and **false** indicates the opposite. Default value: **false** |
| [repeatClickInterval](arkts-accessibility-config-con-sys.md#repeatClickInterval) | Interval between repeated clicks. |
| [screenMagnification](arkts-accessibility-config-con-sys.md#screenMagnification) | Indicates the configuration of screen magnification. |
| [shortkeyMultiTargets](arkts-accessibility-config-con-sys.md#shortkeyMultiTargets) | List of target applications for the accessibility shortcut keys. The value format is ['bundleName/abilityName']. |
<!--DelEnd-->

