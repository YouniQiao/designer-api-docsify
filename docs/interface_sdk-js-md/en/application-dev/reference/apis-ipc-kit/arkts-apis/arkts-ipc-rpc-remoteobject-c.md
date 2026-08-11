# RemoteObject

Provides methods to implement **RemoteObject**. The service provider must inherit from this class.

**Inheritance/Implementation:** RemoteObject extends [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-rpc-class RemoteObject extends IRemoteObject--><!--Device-rpc-class RemoteObject extends IRemoteObject-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## attachLocalInterface

```TypeScript
attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

Binds an interface descriptor to an **IRemoteBroker** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [modifyLocalInterface](arkts-ipc-rpc-remoteobject-c.md#modifylocalinterface)(localInterface:

<!--Device-RemoteObject-attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void--><!--Device-RemoteObject-attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | Yes | IRemoteBroker** object. |
| descriptor | string | Yes | Interface descriptor. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    this.attachLocalInterface(this, descriptor);
  }
  addDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // Implement the method logic based on service requirements.
    return true;
  }
  removeDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // Implement the method logic based on service requirements.
    return true;
  }
}
let testRemoteObject = new TestRemoteObject("testObject");
```

## constructor

```TypeScript
constructor(descriptor: string)
```

A constructor used to create a **RemoteObject** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-RemoteObject-constructor(descriptor: string)--><!--Device-RemoteObject-constructor(descriptor: string)-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| descriptor | string | Yes | Interface descriptor. The length of the string must be less than 40960. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
}
```

## getCallingPid

ArkTS-Dyn:
```TypeScript
getCallingPid(): number
```

ArkTS-Sta:
```TypeScript
getCallingPid(): int
```

Obtains the PID of the remote process.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-RemoteObject-getCallingPid(): int--><!--Device-RemoteObject-getCallingPid(): int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | PID of the remote process obtained. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid: ' + testRemoteObject.getCallingPid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

## getCallingUid

ArkTS-Dyn:
```TypeScript
getCallingUid(): number
```

ArkTS-Sta:
```TypeScript
getCallingUid(): int
```

Obtains the UID of the remote process.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-RemoteObject-getCallingUid(): int--><!--Device-RemoteObject-getCallingUid(): int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Return the UID of the { |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid: ' + testRemoteObject.getCallingUid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

## getDescriptor

```TypeScript
getDescriptor(): string
```

Obtains the interface descriptor of this object. The interface descriptor is a string.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RemoteObject-getDescriptor(): string--><!--Device-RemoteObject-getDescriptor(): string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Interface descriptor obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) | The proxy or remote object is invalid. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testObject = new TestRemoteObject("ipcTest");
  let descriptor = testObject.getDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is ' + descriptor);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## getInterfaceDescriptor

```TypeScript
getInterfaceDescriptor(): string
```

Obtains the interface descriptor.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.IRemoteObject#getDescriptor](arkts-ipc-rpc-iremoteobject-c.md#getdescriptor)()

<!--Device-RemoteObject-getInterfaceDescriptor(): string--><!--Device-RemoteObject-getInterfaceDescriptor(): string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Interface descriptor obtained. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let descriptor = testRemoteObject.getInterfaceDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is: ' + descriptor);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getLocalInterface

```TypeScript
getLocalInterface(descriptor: string): IRemoteBroker
```

Obtains the string of the interface descriptor.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RemoteObject-getLocalInterface(descriptor: string): IRemoteBroker--><!--Device-RemoteObject-getLocalInterface(descriptor: string): IRemoteBroker-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| descriptor | string | Yes | String of the interface descriptor. The length of the string must be less than 40960. |

**Return value:**

| Type | Description |
| --- | --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | IRemoteBroker** object bound to the specified interface token. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.The number of parameters is incorrect; 2.The parameter type does not match; 3.The string length is greater than or equal to 40960; 4.The number of bytes copied to the buffer is different from the length of the obtained string. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.getLocalInterface("testObject");
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

## modifyLocalInterface

```TypeScript
modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void
```

Binds an interface descriptor to an **IRemoteBroker** object.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RemoteObject-modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void--><!--Device-RemoteObject-modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localInterface | [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | Yes | IRemoteBroker** object. |
| descriptor | string | Yes | IRemoteBroker** object bound to the interface descriptor. The length of the descriptor must be less than 40960. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.The number of parameters is incorrect; 2.The parameter type does not match; 3.The string length is greater than or equal to 40960; 4.The number of bytes copied to the buffer is different from the length of the obtained string. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    try {
      this.modifyLocalInterface(this, descriptor);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
      hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
    }
  }
  registerDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // Implement the method logic based on service requirements.
  }
  unregisterDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // Implement the method logic based on service requirements.
  }
}
let testRemoteObject = new TestRemoteObject("testObject");
```

## onRemoteMessageRequest

ArkTS-Dyn:
```TypeScript
onRemoteMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): boolean | Promise<boolean>
```

ArkTS-Sta:
```TypeScript
onRemoteMessageRequest(
      code: int,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): boolean | Promise<boolean>
```

Called to return a response to **sendMessageRequest()**. The server processes the request synchronously or  asynchronously and returns the result in this API.

> **NOTE：**
> 
> - You are advised to overload **onRemoteMessageRequest** preferentially, which implements synchronous and
> asynchronous message processing.
> 
> - If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
> **onRemoteMessageRequest()** takes effect.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RemoteObject-onRemoteMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): boolean | Promise<boolean>--><!--Device-RemoteObject-onRemoteMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): boolean | Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Service request code sent by the remote end. |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object that holds the parameters called by the client. |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object to which the result is written. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Whether the operation is synchronous or asynchronous. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the request is processed synchronously in **onRemoteMessageRequest**, a Boolean value is returned. The value **true** means that the operation is successful, and **false** means the opposite.&lt;br&gt;- If the request is processed asynchronously in **onRemoteMessageRequest**, a promise object is returned. The value **true** means that the operation is successful, and **false** means the opposite. |

## onRemoteMessageRequest

ArkTS-Dyn:
```TypeScript
onRemoteMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callingInfo?: CallingInfo
    ): boolean | Promise<boolean>
```

ArkTS-Sta:
```TypeScript
onRemoteMessageRequest(
      code: int,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callingInfo?: CallingInfo
    ): boolean | Promise<boolean>
```

Provides a response to **sendMessageRequest()**. The server processes the request and returns a response in this  API. The IPC context can be obtained from the input parameter **callingInfo**.

> **NOTE：**
> 
> You are advised to overload the **onRemoteMessageRequest** method with the **CallingInfo** parameter to
> implement synchronous and asynchronous message processing.
> If both **onRemoteRequest()** and **onRemoteMessageRequest()** are overloaded, only
> **onRemoteMessageRequest()** takes effect.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RemoteObject-onRemoteMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callingInfo?: CallingInfo    ): boolean | Promise<boolean>--><!--Device-RemoteObject-onRemoteMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callingInfo?: CallingInfo    ): boolean | Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Service request code sent by the remote end. |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object that holds the parameters called by the client. |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object to which the result is written. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Whether the operation is synchronous or asynchronous. |
| callingInfo | [CallingInfo](arkts-ipc-rpc-callinginfo-c.md) | No | IPC context. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the request is processed synchronously in **onRemoteMessageRequest**, a Boolean value is returned. The value **true** means that the operation is successful, and **false** means the opposite.&lt;br&gt;- If the request is processed asynchronously in **onRemoteMessageRequest**, a promise object is returned. The value **true** means that the operation is successful, and **false** means the opposite. |

## onRemoteRequest

```TypeScript
onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

Called to return a response to **sendRequest()**. The server processes the request and returns a response in this  function.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)(code:

<!--Device-RemoteObject-onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean--><!--Device-RemoteObject-onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | Service request code sent by the remote end. |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object that holds the parameters called by the client. |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object carrying the result. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Whether the operation is synchronous or asynchronous. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

## queryLocalInterface

```TypeScript
queryLocalInterface(descriptor: string): IRemoteBroker
```

Checks whether the remote object corresponding to the specified interface token exists.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [rpc.IRemoteObject#getLocalInterface](arkts-ipc-rpc-iremoteobject-c.md#getlocalinterface)(descriptor:

<!--Device-RemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker--><!--Device-RemoteObject-queryLocalInterface(descriptor: string): IRemoteBroker-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| descriptor | string | Yes | Interface descriptor. |

**Return value:**

| Type | Description |
| --- | --- |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) | Returns the remote object if a match is found; returns **Null** otherwise. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.queryLocalInterface("testObject");
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

## sendMessageRequest

ArkTS-Dyn:
```TypeScript
sendMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): Promise<RequestResult>
```

ArkTS-Sta:
```TypeScript
sendMessageRequest(
      code: int,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption
    ): Promise<RequestResult>
```

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous  mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The  specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in  
 **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the  reply message contains the returned information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>--><!--Device-RemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption    ): Promise<RequestResult>-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Message code [1-16777215] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object holding the data to send. |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object that receives the response. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;RequestResult&gt; | Promise used to return a **requestResult** instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.The number of parameters is incorrect; 2.The parameter type does not match; 3.Failed to obtain the passed object instance. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeInt(1);
  data.writeString("hello");
  testRemoteObject.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
}
```

## sendMessageRequest

ArkTS-Dyn:
```TypeScript
sendMessageRequest(
      code: number,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callback: AsyncCallback<RequestResult>
    ): void
```

ArkTS-Sta:
```TypeScript
sendMessageRequest(
      code: int,
      data: MessageSequence,
      reply: MessageSequence,
      options: MessageOption,
      callback: AsyncCallback<RequestResult>
    ): void
```

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous  mode is set in **options**, a callback will be called immediately, and the reply message is empty. The  specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in  
 **options**, a callback will be invoked when the response to **sendMessageRequest** is returned, and the  reply message contains the returned information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void--><!--Device-RemoteObject-sendMessageRequest(      code: int,      data: MessageSequence,      reply: MessageSequence,      options: MessageOption,      callback: AsyncCallback<RequestResult>    ): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Message code [1-16777215] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object holding the data to send. |
| reply | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes | MessageSequence** object that receives the response. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestResult&gt; | Yes | Callback for receiving the sending result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.The number of parameters is incorrect; 2.The parameter type does not match; 3.Failed to obtain the passed object instance. |

## sendRequest

```TypeScript
sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific  reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains  the returned information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** [rpc.IRemoteObject#sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-RemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean--><!--Device-RemoteObject-sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | Message code [1-16777215] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object holding the data to send. |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object that receives the response. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns **true** if the message is sent successfully; returns **false** otherwise. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class testRemoteObject extends rpc.RemoteObject {
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let ret: boolean = testRemoteObject.sendRequest(1, data, reply, option);
  if (ret) {
    hilog.info(0x0000, 'testTag', 'sendRequest got result');
    let msg = reply.readString();
    hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
  } else {
    hilog.error(0x0000, 'testTag', 'sendRequest failed');
  }
  hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
  data.reclaim();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## sendRequest

```TypeScript
sendRequest(
      code: number,
      data: MessageParcel,
      reply: MessageParcel,
      options: MessageOption
    ): Promise<SendRequestResult>
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific  reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains  the returned information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.IRemoteObject#sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-RemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>--><!--Device-RemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption    ): Promise<SendRequestResult>-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | Message code [1-16777215] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object holding the data to send. |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object that receives the response. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SendRequestResult&gt; | Promise used to return a **sendRequestResult** instance. |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let a = testRemoteObject.sendRequest(1, data, reply, option) as Object;
  let b = a as Promise<rpc.SendRequestResult>;
  b.then((result: rpc.SendRequestResult) => {
    if (result.errCode === 0) {
      hilog.info(0x0000, 'testTag', 'sendRequest got result');
      let num = result.reply.readInt();
      let msg = result.reply.readString();
      hilog.info(0x0000, 'testTag', 'reply num: ' + num);
      hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
    } else {
      hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
    }
  }).catch((e: Error) => {
    hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
  }).finally (() => {
    hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
    data.reclaim();
    reply.reclaim();
  });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

## sendRequest

```TypeScript
sendRequest(
      code: number,
      data: MessageParcel,
      reply: MessageParcel,
      options: MessageOption,
      callback: AsyncCallback<SendRequestResult>
    ): void
```

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode  is set in **options**, a callback will be called immediately, and the reply message is empty. The specific  reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains  the returned information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.IRemoteObject#sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)(code:

<!--Device-RemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void--><!--Device-RemoteObject-sendRequest(      code: number,      data: MessageParcel,      reply: MessageParcel,      options: MessageOption,      callback: AsyncCallback<SendRequestResult>    ): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | Message code [1-16777215] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object holding the data to send. |
| reply | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes | MessageParcel** object that receives the response. |
| options | [MessageOption](arkts-ipc-rpc-messageoption-c.md) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SendRequestResult&gt; | Yes | Callback for receiving the sending result. |

