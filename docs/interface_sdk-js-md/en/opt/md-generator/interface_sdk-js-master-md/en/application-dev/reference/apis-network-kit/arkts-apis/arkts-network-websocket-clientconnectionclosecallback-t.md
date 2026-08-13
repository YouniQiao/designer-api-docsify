# ClientConnectionCloseCallback

```TypeScript
export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void
```

Callback function when a client connection is closed.

**Since:** 24

**Deprecated since:** -1

<!--Device-webSocket-export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void--><!--Device-webSocket-export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [clientConnection](arkts-network-websocket-websocketmessage-i.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | Yes |
| closeReason | [CloseResult](arkts-network-websocket-closeresult-i.md) | Yes |
