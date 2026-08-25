# MessageHandler

自定义通信对象。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 开发者可通过注册此对象来接收输入法应用发送的自定义通信数据，接收到自定义通信数据时会触发此对象中 &lt;br
&gt; 
> [onMessage](#onmessage)回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#onterminated)回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](#onterminated)回调函数。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## onMessage

```TypeScript
onMessage: OnMessageCallback
```

接收输入法应用发送的自定义数据回调函数。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 当已注册的MessageHandler接收到来自输入法应用发送的自定义通信数据时，会触发该回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
  }
};
inputMethodController.recvMessage(messageHandler);
```

## onMessage

```TypeScript
onMessage(msgId: string, msgParam?: ArrayBuffer): void
```

接收输入法应用发送的自定义数据回调函数。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 当已注册的MessageHandler接收到来自输入法应用发送的自定义通信数据时，会触发该回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | 是 |
| msgParam | ArrayBuffer | 否 |

**示例**

参见 [onMessage](#onmessage)

## onTerminated

```TypeScript
onTerminated(): void
```

监听对象终止回调函数。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 当应用注册新的MessageHandler对象时，会触发上一个已注册MessageHandler对象的OnTerminated回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 当应用取消注册时，会触发当前已注册MessageHandler对象的OnTerminated回调函数。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例**

```TypeScript
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
  }
};
inputMethodController.recvMessage(messageHandler);
```

## onTerminated

```TypeScript
onTerminated: Callback<void>
```

监听对象终止回调函数。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 当应用注册新的MessageHandler对象时，会触发上一个已注册MessageHandler对象的OnTerminated回调函数。 &lt;br
&gt; 
> &lt;br
&gt; 
> 当应用取消注册时，会触发当前已注册MessageHandler对象的OnTerminated回调函数。

**类型：** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework
