# isConnected

## 导入模块

```TypeScript
import { socket } from 'kits/@kit.ConnectivityKit';
```

## isConnected

```TypeScript
function isConnected(clientSocket: int): boolean
```

Check whether the current socket connection has been established.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-socket-function isConnected(clientSocket: int): boolean--><!--Device-socket-function isConnected(clientSocket: int): boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates client socket. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Indicates whether or not it is connected. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 入参clientNumber由sppAccept或sppConnect接口获取。
let clientSocket = 1; 
try {
    let result: boolean = socket.isConnected(clientSocket);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

