# MessageHandler

Represents a custom communication object. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> You can register this object to receive custom communication data sent by the edit box application attached to the input method application. When the custom communication data is received, the [onMessage](#onmessage) callback in this object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated) callback of the penultimate registered object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> If this object is unregistered, its [onTerminated](#onterminated) callback will be triggered.

**Since:** 23

<!--Device-inputMethodEngine-interface MessageHandler--><!--Device-inputMethodEngine-interface MessageHandler-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

Receives the custom data callback sent by the edit box application attached to the input method application. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This callback is triggered when the registered [MessageHandler](#messagehandler) receives custom communication data sent by the edit box application attached to the input method application. &lt;br
&gt; 
> &lt;br
&gt; 
> The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**Since:** 15

<!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void--><!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | Identifier of the received custom communication data. |
| msgParam | ArrayBuffer | No | Message body of the received custom communication data. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

## onTerminated

```TypeScript
onTerminated(): void
```

Listens for MessageHandler termination. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> When an application registers a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the penultimate registered [MessageHandler](#messagehandler) object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> When an application unregisters a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the registered [MessageHandler](#messagehandler) object is triggered.

**Since:** 15

<!--Device-MessageHandler-onTerminated(): void--><!--Device-MessageHandler-onTerminated(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

## onMessage

```TypeScript
onMessage: OnMessageCallback
```

onMessage(msgId: string, msgParam?: ArrayBuffer): void <br> <br>Receives the custom data callback sent by the edit box application attached to the input method application. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This callback is triggered when the registered [MessageHandler](#messagehandler) receives custom communication data sent by the edit box application attached to the input method application. &lt;br
&gt; 
> &lt;br
&gt; 
> The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**Type:** OnMessageCallback

**Since:** 23

<!--Device-MessageHandler-onMessage: OnMessageCallback--><!--Device-MessageHandler-onMessage: OnMessageCallback-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## onTerminated

```TypeScript
onTerminated: Callback<void>
```

Listens for MessageHandler termination. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> When an application registers a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the penultimate registered [MessageHandler](#messagehandler) object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> When an application unregisters a new [MessageHandler](#messagehandler) object, the [onTerminated](#onterminated) callback of the registered [MessageHandler](#messagehandler) object is triggered.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 23

<!--Device-MessageHandler-onTerminated: Callback<void>--><!--Device-MessageHandler-onTerminated: Callback<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

