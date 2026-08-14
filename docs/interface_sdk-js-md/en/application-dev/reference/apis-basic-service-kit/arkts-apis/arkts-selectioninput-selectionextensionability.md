# @ohos.selectionInput.SelectionExtensionAbility

## Modules to Import

```TypeScript
import { SelectionExtensionAbility } from 'SelectionExtensionAbility';
```

## Summary

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md) | This module provides APIs for word selection extension, which can implement extended interactions such as searching and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see [Developing a Word Selection Extension Ability](../../../basic-services/selectionInput/selection-services-application-guide.md). This module provides the following capabilities: - Lifecycle management: Use the [onConnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#onConnect) and [onDisconnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#onDisconnect) callbacks to process the connection and disconnection logic. - **context**: You can use **context** to call [startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c-sys.md#startAbility) to start the target ability in the same app, or use **context** as an input parameter of [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)) to create a word selection panel. > **NOTE：**> > - This module is supported only on PCs/2-in-1 devices. You can use > **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports the > capability. |
<!--DelEnd-->

