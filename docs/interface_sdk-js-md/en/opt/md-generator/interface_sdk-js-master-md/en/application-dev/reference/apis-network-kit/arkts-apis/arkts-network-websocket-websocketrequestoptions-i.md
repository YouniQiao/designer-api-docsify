# WebSocketRequestOptions

Defines the optional parameters carried in the request for establishing a WebSocket connection.

**Since:** 23

<!--Device-webSocket-export interface WebSocketRequestOptions--><!--Device-webSocket-export interface WebSocketRequestOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
```

## caPath

```TypeScript
caPath?: string
```

File path for client cert.

**Type:** string

**Since:** 23

<!--Device-WebSocketRequestOptions-caPath?: string--><!--Device-WebSocketRequestOptions-caPath?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## clientCert

```TypeScript
clientCert?: ClientCert
```

Client cert.

**Type:** ClientCert

**Since:** 23

<!--Device-WebSocketRequestOptions-clientCert?: ClientCert--><!--Device-WebSocketRequestOptions-clientCert?: ClientCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## header

```TypeScript
header?: Record<string, string>
```

HTTP request header.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocketRequestOptions-header?: Record<string, string>--><!--Device-WebSocketRequestOptions-header?: Record<string, string>-End-->

**System capability:** SystemCapability.Communication.NetStack

## minSupportTlsProtocol

```TypeScript
minSupportTlsProtocol?: TlsProtocol
```

The minimum support version of TLS protocol.

**Type:** [TlsProtocol](arkts-network-websocket-tlsprotocol-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocketRequestOptions-minSupportTlsProtocol?: TlsProtocol--><!--Device-WebSocketRequestOptions-minSupportTlsProtocol?: TlsProtocol-End-->

**System capability:** SystemCapability.Communication.NetStack

## pingInterval

```TypeScript
pingInterval?: number
```

Self defined interval of ping frame. default: 30. disable: 0. max: 30000. unit:second. Ping is performed at every pingInterval.

**Type:** number

**Since:** 26.0.0

<!--Device-WebSocketRequestOptions-pingInterval?: int--><!--Device-WebSocketRequestOptions-pingInterval?: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## pongTimeout

```TypeScript
pongTimeout?: number
```

Self defined timeout of pong frame. default: 30. max: 30000. unit:second. The value must be less than or equal to pingInterval. If no pong is received within the pongTimeout period, the websocket connection will be disconnected.

**Type:** number

**Since:** 26.0.0

<!--Device-WebSocketRequestOptions-pongTimeout?: int--><!--Device-WebSocketRequestOptions-pongTimeout?: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## protocol

```TypeScript
protocol?: string
```

Self defined protocol.

**Type:** string

**Since:** 24

<!--Device-WebSocketRequestOptions-protocol?: string--><!--Device-WebSocketRequestOptions-protocol?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyConfiguration
```

HTTP proxy configuration. Use 'system' if this field is not set.

**Type:** [ProxyConfiguration](arkts-network-websocket-proxyconfiguration-t.md)

**Since:** 24

<!--Device-WebSocketRequestOptions-proxy?: ProxyConfiguration--><!--Device-WebSocketRequestOptions-proxy?: ProxyConfiguration-End-->

**System capability:** SystemCapability.Communication.NetStack

## skipServerCertVerification

```TypeScript
skipServerCertVerification?: boolean
```

Whether or not to skip the verification of the server's certification.

**Type:** boolean

**Since:** 26.0.0

<!--Device-WebSocketRequestOptions-skipServerCertVerification?: boolean--><!--Device-WebSocketRequestOptions-skipServerCertVerification?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack

## supportOriginPort

```TypeScript
supportOriginPort?: boolean
```

The option of supporting origin port.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocketRequestOptions-supportOriginPort?: boolean--><!--Device-WebSocketRequestOptions-supportOriginPort?: boolean-End-->

**System capability:** SystemCapability.Communication.NetStack
