# MessageHandler

&lt;p&gt;Custom message handler.&lt;/p&gt; &lt;p&gt;Implement this interface to respond to custom messages.&lt;/p&gt;

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

This method is called when a custom message is received.

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

This method is called when a new message handler is set.

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

This method is called when a custom message is received.

**Type:** OnMessageCallback

**Since:** 23

<!--Device-MessageHandler-onMessage: OnMessageCallback--><!--Device-MessageHandler-onMessage: OnMessageCallback-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## onTerminated

```TypeScript
onTerminated: Callback<void>
```

This method is called when a new message handler is set.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 23

<!--Device-MessageHandler-onTerminated: Callback<void>--><!--Device-MessageHandler-onTerminated: Callback<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

