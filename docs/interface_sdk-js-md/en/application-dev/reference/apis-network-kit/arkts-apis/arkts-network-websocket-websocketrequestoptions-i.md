# WebSocketRequestOptions

Defines the optional parameters carried in the request for establishing a WebSocket connection.

**Since:** 23

<!--Device-webSocket-export interface WebSocketRequestOptions--><!--Device-webSocket-export interface WebSocketRequestOptions-End-->

**System capability:** SystemCapability.Communication.NetStack

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## caPath

```TypeScript
caPath?: string
```

Path of CA certificates. If a path is set, the system uses the CA certificates in this path. If a path is not set, the system uses the preset CA certificate, namely, **\/etc/ssl/certs/cacert.pem**. This path is the sandbox mapping path, which can be obtained by using **UIAbilityContext** APIs. Currently, only text certificates in PEM format are supported.

**Type:** string

**Since:** 23

<!--Device-WebSocketRequestOptions-caPath?: string--><!--Device-WebSocketRequestOptions-caPath?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## clientCert

```TypeScript
clientCert?: ClientCert
```

Client certificate.

**Type:** ClientCert

**Since:** 23

<!--Device-WebSocketRequestOptions-clientCert?: ClientCert--><!--Device-WebSocketRequestOptions-clientCert?: ClientCert-End-->

**System capability:** SystemCapability.Communication.NetStack

## header

```TypeScript
header?: Record<string, string>
```

HTTP request header.

**Type:** Record&lt;string, string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocketRequestOptions-header?: Record<string, string>--><!--Device-WebSocketRequestOptions-header?: Record<string, string>-End-->

**System capability:** SystemCapability.Communication.NetStack

## minSupportTlsProtocol

```TypeScript
minSupportTlsProtocol?: TlsProtocol
```

Custom minimum TLS version supported. For example, if this parameter is set to **TLS_V_1_1**, the client supports TLS 1.1, TLS 1.2, and TLS 1.3.

**Type:** [TlsProtocol](arkts-network-websocket-tlsprotocol-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSocketRequestOptions-minSupportTlsProtocol?: TlsProtocol--><!--Device-WebSocketRequestOptions-minSupportTlsProtocol?: TlsProtocol-End-->

**System capability:** SystemCapability.Communication.NetStack

## pingInterval

```TypeScript
pingInterval?: int
```

Custom [heartbeat detection interval](../../../network/websocket-connection.md). The default value is 30s. Heartbeat detection is initiated at the specified interval. If the value is set to **0**, heartbeat detection is disabled. The maximum value is 30000s, and the minimum value is 0s.

**Type:** int

**Since:** 26.0.0

<!--Device-WebSocketRequestOptions-pingInterval?: int--><!--Device-WebSocketRequestOptions-pingInterval?: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## pongTimeout

```TypeScript
pongTimeout?: int
```

Timeout interval for disconnecting a connection after heartbeat detection is initiated. The default value is 30s. If no response is received during the specified interval, the connection is disconnected. The maximum value is 30 000s, and the minimum value is 0s. **pongTimeout** must be less than or equal to **pingInterval**.

**Type:** int

**Since:** 26.0.0

<!--Device-WebSocketRequestOptions-pongTimeout?: int--><!--Device-WebSocketRequestOptions-pongTimeout?: int-End-->

**System capability:** SystemCapability.Communication.NetStack

## protocol

```TypeScript
protocol?: string
```

Custom **Sec-WebSocket-Protocol** field. The default value is "".

**Type:** string

**Since:** 23

<!--Device-WebSocketRequestOptions-protocol?: string--><!--Device-WebSocketRequestOptions-protocol?: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## proxy

```TypeScript
proxy?: ProxyConfiguration
```

Proxy configuration. By default, the system network proxy is used.

**Type:** [ProxyConfiguration](arkts-network-websocket-proxyconfiguration-t.md)

**Since:** 23

<!--Device-WebSocketRequestOptions-proxy?: ProxyConfiguration--><!--Device-WebSocketRequestOptions-proxy?: ProxyConfiguration-End-->

**System capability:** SystemCapability.Communication.NetStack

## skipServerCertVerification

```TypeScript
skipServerCertVerification?: boolean
```

Whether to skip server certificate verification. The value **true** means to skip server certificate verification, and the value **false** means the opposite. Default value: **false**.

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

