# SelectionExtensionAbility

This module provides APIs for word selection extension, which can implement extended interactions such as searching and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see [Developing a Word Selection Extension Ability](../../../basic-services/selectionInput/selection-services-application-guide.md). This module provides the following capabilities:  
- Lifecycle management: Use the [onConnect](#onconnect) and  
[onDisconnect](#ondisconnect) callbacks to process the connection and disconnection logic.  
- **context**: You can use **context** to call  
[startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability) to start the target ability in the same app, or use **context** as an input parameter of [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md) to create a word selection panel.

> **NOTE：**&gt;
> - This module is supported only on PCs/2-in-1 devices. You can use
> **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports the
> capability.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { SelectionExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

Defines a callback triggered when the client connects to the **SelectionExtensionAbility**. You can return an RPC object in this callback to establish an IPC connection between the client and the server. You need to return a communication stub object that inherits **rpc.RemoteObject**. The system passes the stub object to the client, which then uses the stub object to communicate with the **SelectionExtensionAbility** through IPC.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## onDisconnect

```TypeScript
onDisconnect(): void
```

Defines a callback triggered when the client disconnects from the **SelectionExtensionAbility** (for example, when the user disables the word selection function or switches the word selection app). You can perform cleanup operations for the **onConnect** callback in this callback. For example, you can call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md) to destroy the created panel, or call off('selectionCompleted') to unsubscribe from the word selection completion event.The callback is triggered only when the **SelectionExtensionAbility** is disconnected normally. It is not triggered in cases of abnormal disconnection (for example, process termination due to low memory conditions).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

## context

```TypeScript
context: SelectionExtensionContext
```

Context of the **SelectionExtensionAbility**. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md). You can use **context** to call [startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability) to start the target ability in the same app, or use **context** as an input parameter of [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md) to create a word selection panel.

**Type:** [SelectionExtensionContext](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md)

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection
