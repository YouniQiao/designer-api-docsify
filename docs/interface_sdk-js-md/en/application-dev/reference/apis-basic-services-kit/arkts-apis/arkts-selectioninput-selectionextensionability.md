# @ohos.selectionInput.SelectionExtensionAbility(SelectionExtensionAbility)

## Modules to Import

```TypeScript
import SelectionExtensionAbility from '@kit.BasicServicesKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [SelectionExtensionAbility(SelectionExtensionAbility)](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md) | This module provides APIs for word selection extension, which can implement extended interactions such as searching and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see [Developing a Word Selection Extension Ability](../../../basic-services/selectionInput/selection-services-application-guide.md). This module provides the following capabilities:  - Lifecycle management: Use the [onConnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#onconnect) and  [onDisconnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#ondisconnect) callbacks to process the connection and disconnection logic.  - **context**: You can use **context** to call  [startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability) to start the target ability in the same app, or use **context** as an input parameter of [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md) to create a word selection panel. |
