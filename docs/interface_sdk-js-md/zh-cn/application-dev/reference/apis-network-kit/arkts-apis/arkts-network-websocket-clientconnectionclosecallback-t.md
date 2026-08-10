# ClientConnectionCloseCallback

```TypeScript
export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void
```

Callback function when a client connection is closed.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-webSocket-export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void--><!--Device-webSocket-export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientConnection | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 | the connection which is closed. |
| closeReason | [CloseResult](arkts-network-websocket-closeresult-i.md) | 是 | the error code and reason why the connection is closed. |

