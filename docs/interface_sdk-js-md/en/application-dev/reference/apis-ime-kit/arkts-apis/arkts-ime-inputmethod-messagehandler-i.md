# MessageHandler

Represents a custom communication object.   
> **NOTE：**
   
> 
   
> You can register this object to receive custom communication data sent by the input method application. When the custom communication data is received, the [onMessage](#onmessage) callback in this object is triggered.
   
> 
   
> This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated) callback of the penultimate registered object is triggered.
   
> 
   
> If this object is unregistered, its [onTerminated](#onterminated) callback will be triggered.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

This method is called when a custom message is received.

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

This method is called when a new message handler is set.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework
