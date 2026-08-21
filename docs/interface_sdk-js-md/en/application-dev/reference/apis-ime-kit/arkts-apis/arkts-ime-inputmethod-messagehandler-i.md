# MessageHandler

@brief Represents a custom communication object. <br> <br>   
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

**Since:** 23

<!--Device-inputMethod-interface MessageHandler--><!--Device-inputMethod-interface MessageHandler-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

@brief This method is called when a custom message is received.

**Since:** 15

<!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void--><!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | the identifier of the message. |
| msgParam | ArrayBuffer | No | the parameter of the custom message. |

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
onTerminated(): void
```

@brief This method is called when a new message handler is set.

**Since:** 15

<!--Device-MessageHandler-onTerminated(): void--><!--Device-MessageHandler-onTerminated(): void-End-->

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
onMessage: OnMessageCallback
```

@brief Receives custom data sent by the input method application. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> This callback is triggered when the registered MeesageHandler receives custom communication data sent by the input method application. &lt;br
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

@brief Listens for MessageHandler termination. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> When an application registers a new MessageHandler object, the **OnTerminated** callback of the previous registered MessageHandler object is triggered. &lt;br
&gt; 
> &lt;br
&gt; 
> When an application unregisters a MessageHandler object, the **OnTerminated** callback of the current registered MessageHandler object is triggered.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 23

<!--Device-MessageHandler-onTerminated: Callback<void>--><!--Device-MessageHandler-onTerminated: Callback<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

