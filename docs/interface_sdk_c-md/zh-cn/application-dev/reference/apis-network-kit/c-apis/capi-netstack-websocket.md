# WebSocket

```c
struct WebSocket {...}
```

## 概述

WebSocket客户端结构体。

<!--Device-struct WebSocket {...}--><!--Device-struct WebSocket {...}-End-->

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](capi-network-kit-netstack.md)

**所在头文件：** [net_websocket_type.h](capi-net-websocket-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| -- | -- |
| [WebSocket_OnOpenCallback](capi-net-websocket-type-h.md#websocket_onopencallback) onOpen | 客户端接收连接消息的回调指针。 |
| [WebSocket_OnMessageCallback](capi-net-websocket-type-h.md#websocket_onmessagecallback) onMessage | 客户端接收消息的回调指针。 |
| [WebSocket_OnErrorCallback](capi-net-websocket-type-h.md#websocket_onerrorcallback) onError | 客户端接收错误消息的回调指针。 |
| [WebSocket_OnCloseCallback](capi-net-websocket-type-h.md#websocket_onclosecallback) onClose | 客户端接收关闭消息的回调指针。 |
| [WebSocket_RequestOptions](capi-netstack-websocket-requestoptions.md) requestOptions | 客户端建立连接请求内容。 |


