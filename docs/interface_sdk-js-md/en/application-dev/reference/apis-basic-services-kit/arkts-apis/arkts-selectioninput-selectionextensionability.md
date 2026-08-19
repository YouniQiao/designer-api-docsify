# @ohos.selectionInput.SelectionExtensionAbility

## Modules to Import

```TypeScript
import { SelectionExtensionAbility } from '@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md) | This module provides APIs for word selection extension, which can implement extended interactions such as searching and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see [Developing a Word Selection Extension Ability](../../../basic-services/selectionInput/selection-services-application-guide.md). This module provides the following capabilities: - Lifecycle management: Use the [onConnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#onconnect) and [onDisconnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#ondisconnect) callbacks to process the connection and disconnection logic. - **context**: You can use **context** to call [startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c-sys.md#startability) to start the target ability in the same app, or use **context** as an input parameter of [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md) to create a word selection panel. &gt; **NOTE：**&gt; &gt; - This module is supported only on PCs/2-in-1 devices. You can use &gt; **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports the &gt; capability. |
<!--DelEnd-->

