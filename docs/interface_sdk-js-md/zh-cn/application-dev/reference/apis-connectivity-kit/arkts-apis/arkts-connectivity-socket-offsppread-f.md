# offSppRead

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## offSppRead

```TypeScript
function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void
```

Unsubscribe the event reported when data is read from the socket.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-socket-function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void--><!--Device-socket-function offSppRead(clientSocket: int, callback?: Callback<ArrayBuffer>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | int | 是 | Client socket ID, which is obtained by sppAccept or sppConnect. The value should be an integer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ArrayBuffer&gt; | 否 | Callback used to listen for the spp read event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

