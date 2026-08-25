# MessageHandler

Represents a custom communication object. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> You can register this object to receive custom communication data sent by the input method application. When the custom communication data is received, the [onMessage](#onmessage) callback in this object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated) callback of the penultimate registered object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> If this object is unregistered, its [onTerminated](#onterminated) callback will be triggered.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage: OnMessageCallback
```

Receives custom data sent by the input method application. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This callback is triggered when the registered MeesageHandler receives custom communication data sent by the input method application. &lt;br
&gt; 
> &lt;br
&gt; 
> The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Examples**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
inputMethodController.recvMessage(messageHandler);
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

This method is called when a custom message is received.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | Yes |
| msgParam | ArrayBuffer | No |

**Examples**

See [onMessage](#onmessage)

## onTerminated

```TypeScript
onTerminated(): void
```

This method is called when a new message handler is set.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Examples**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
inputMethodController.recvMessage(messageHandler);
```

## onTerminated

```TypeScript
onTerminated: Callback<void>
```

Listens for MessageHandler termination. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> When an application registers a new MessageHandler object, the **OnTerminated** callback of the previous registered MessageHandler object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> When an application unregisters a MessageHandler object, the **OnTerminated** callback of the current registered MessageHandler object is triggered.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework
