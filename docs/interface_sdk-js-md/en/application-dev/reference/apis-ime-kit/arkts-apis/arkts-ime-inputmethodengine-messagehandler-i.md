# MessageHandler

Represents a custom communication object. > **NOTE：**> > You can register this object to receive custom communication data sent by the edit box application attached to > the input method application. When the custom communication data is received, the > [onMessage](#onMessage) callback in > this object is triggered. > > This object is globally unique. After multiple registrations, only the last registered object is valid and > retained, and the [onTerminated](#onTerminated) callback of the > penultimate registered object is triggered. > > If this object is unregistered, its [onTerminated](#onTerminated) > callback will be triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

Receives the custom data callback sent by the edit box application attached to the input method application. > **NOTE：**> > This callback is triggered when the registered [MessageHandler](#MessageHandler) > receives custom communication data sent by the edit box application attached to the input method application. > > The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** > data is received, confirm it with the data sender.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void--><!--Device-MessageHandler-onMessage(msgId: string, msgParam?: ArrayBuffer): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | Identifier of the received custom communication data. |
| msgParam | ArrayBuffer | No | Message body of the received custom communication data. |

## Examples

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

Listens for MessageHandler termination. > **NOTE：**> > When an application registers a new [MessageHandler](#MessageHandler) object, the > [onTerminated](#onTerminated) callback of the penultimate registered > [MessageHandler](#MessageHandler) object is triggered. > > When an application unregisters a new [MessageHandler](#MessageHandler) object, the > [onTerminated](#onTerminated) callback of the registered > [MessageHandler](#MessageHandler) object is triggered.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

<!--Device-MessageHandler-onTerminated(): void--><!--Device-MessageHandler-onTerminated(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Examples

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

This method is called when a custom message is received.

**Type:** OnMessageCallback

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MessageHandler-onMessage: OnMessageCallback--><!--Device-MessageHandler-onMessage: OnMessageCallback-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## onTerminated

```TypeScript
onTerminated: Callback<void>
```

This method is called when a new message handler is set.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-MessageHandler-onTerminated: Callback<void>--><!--Device-MessageHandler-onTerminated: Callback<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

