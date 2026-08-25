# ClientConnectionCloseCallback

```TypeScript
export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason :CloseResult) => void
```

Callback invoked when the WebSocketServer connection is closed.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [clientConnection](arkts-network-websocket-websocketmessage-i.md) | [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md) | Yes |
| closeReason | [CloseResult](arkts-network-websocket-closeresult-i.md) | Yes |
