# ClientConnectionCloseCallback

```TypeScript
export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason :CloseResult) => void
```

关闭WebSocketServer连接时，订阅close事件得到的指定客户端的关闭结果。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [clientConnection](arkts-network-websocket-websocketmessage-i.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | 是 |
| closeReason | [CloseResult](arkts-network-websocket-closeresult-i.md) | 是 |
