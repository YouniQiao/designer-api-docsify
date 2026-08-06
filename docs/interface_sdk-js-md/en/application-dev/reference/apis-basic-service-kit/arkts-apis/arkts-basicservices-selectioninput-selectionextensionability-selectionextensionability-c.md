# SelectionExtensionAbility

This module provides APIs for word selection extension, which can implement extended interactions such as searching and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.This module provides the following capabilities:

- Lifecycle management: Use the [onConnect]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and  
[onDisconnect]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ callbacks to process the connection and disconnection logic.  
- **context**: You can use **context** to call  
[startAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ to start the target ability in the same app, or use **context** as an input parameter of  
[createPanel]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ to create a word selection panel.
    **NOTE**  
    
    - This module is supported only on PCs/2-in-1 devices. You can use  
    **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports the  
    capability.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-unnamed-declare class SelectionExtensionAbility--><!--Device-unnamed-declare class SelectionExtensionAbility-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

Defines a callback triggered when the client connects to the **SelectionExtensionAbility**. You can return an RPC object in this callback to establish an IPC connection between the client and the server. You need to return a communication stub object that inherits **rpc.RemoteObject**. The system passes the stub object to the client,which then uses the stub object to communicate with the **SelectionExtensionAbility** through IPC.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-onConnect(want: Want): rpc.RemoteObject--><!--Device-SelectionExtensionAbility-onConnect(want: Want): rpc.RemoteObject-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want** object passed by the system when the **SelectionExtensionAbility** is connected. The object contains the description information such as the ability name and bundle name. It is used to obtain the ability connection configuration in the **onConnect** callback so that the corresponding initialization logic can be executed. |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | RemoteObject** communication stub object. You need to implement the remote message processing method (for example, **onRemoteMessageRequest**) of this object. The system passes this object to the client for IPC. |

**Example**

```TypeScript
import { SelectionExtensionAbility } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[SelectionExtensionAbility]';

class StubTest extends rpc.RemoteObject {
  constructor(des: string) {
    super(des);
  }
  onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
  }
}

class ServiceExtAbility extends SelectionExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(): void
```

Defines a callback triggered when the client disconnects from the **SelectionExtensionAbility** (for example, when the user disables the word selection function or switches the word selection app). You can perform cleanup operations for the **onConnect** callback in this callback. For example, you can  
[destroyPanel]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to destroy the created panel, or call  
[off('selectionCompleted')]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_to unsubscribe from the word selection completion event.

The callback is triggered only when the **SelectionExtensionAbility** is disconnected normally. It is not triggered in cases of abnormal disconnection (for example, process termination due to low memory conditions).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-onDisconnect(): void--><!--Device-SelectionExtensionAbility-onDisconnect(): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Example**

```TypeScript
import { SelectionExtensionAbility } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[SelectionExtensionAbility]';

class ServiceExtAbility extends SelectionExtensionAbility {
  onDisconnect(): void {
    hilog.info(0x0000, TAG, `onDisconnect`);
  }
}
```

## context

```TypeScript
context: SelectionExtensionContext
```

Context of the **SelectionExtensionAbility**. This context is inherited from  
[ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. You can use **context** to call  
[startAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to start the target ability in the same app, or use **context** as an input parameter of  
[createPanel]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to create a word selection panel.

**Type:** SelectionExtensionContext

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-context: SelectionExtensionContext--><!--Device-SelectionExtensionAbility-context: SelectionExtensionContext-End-->

**System capability:** SystemCapability.SelectionInput.Selection

