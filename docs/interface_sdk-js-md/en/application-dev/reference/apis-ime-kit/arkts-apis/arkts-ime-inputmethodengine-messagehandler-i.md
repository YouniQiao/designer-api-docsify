# MessageHandler

Represents a custom communication object.   
> **NOTE：**
   
> 
   
> You can register this object to receive custom communication data sent by the edit box application attached to the input method application. When the custom communication data is received, the [onMessage](#onmessage) callback in this object is triggered.
   
> 
   
> This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated) callback of the penultimate registered object is triggered.
   
> 
   
> If this object is unregistered, its [onTerminated](#onterminated) callback will be triggered.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

Receives the custom data callback sent by the edit box application attached to the input method application.   
> **NOTE：**
   
> 
   
> This callback is triggered when the registered [MessageHandler](#messagehandler) receives custom communication data sent by the edit box application attached to the input method application.
   
> 
   
> The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | Yes |
| msgParam | ArrayBuffer | No |

## onTerminated

```TypeScript
onTerminated(): void
```

Listens for MessageHandler termination.   
> **NOTE：**
   
> 
   
> When an application registers a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the penultimate registered [MessageHandler](#messagehandler) object is triggered.
   
> 
   
> When an application unregisters a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the registered [MessageHandler](#messagehandler) object is triggered.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework
