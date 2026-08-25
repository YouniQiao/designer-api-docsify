# InterceptorType

Enumerates the types of HTTP interceptors.  
| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) |Description | | ------ | --|-------------------------------------- | | [INITIAL_REQUEST](arkts-network-http-interceptortype-e.md) |'INITIAL_REQUEST' |Intercepts after the initial HTTP request is assembled.| | [REDIRECTION](arkts-network-http-interceptortype-e.md) | 'REDIRECTION' |Intercepts when a redirection response is received.| | [CACHE_CHECKED](arkts-network-http-interceptortype-e.md) | 'READ_CACHE' |Intercepts when the HTTP cache is checked and hit.| | [NETWORK_CONNECT](arkts-network-http-interceptortype-e.md) | 'CONNECT_NETWORK' |Intercepts before the network request is sent.| | [FINAL_RESPONSE](arkts-network-http-interceptortype-e.md) | 'FINAL_RESPONSE' |

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**System capability:** SystemCapability.Communication.NetStack

## INITIAL_REQUEST

```TypeScript
INITIAL_REQUEST = 'INITIAL_REQUEST'
```

Intercept after the initial HTTP request is assembled.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

## REDIRECTION

```TypeScript
REDIRECTION = 'REDIRECTION'
```

Intercept when we get a redirection responsed and is going to send another request.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

## CACHE_CHECKED

```TypeScript
CACHE_CHECKED = 'READ_CACHE'
```

Intercept after we checked the HTTP cache.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

## NETWORK_CONNECT

```TypeScript
NETWORK_CONNECT = 'CONNECT_NETWORK'
```

Intercept when we perform network connection, such as TLS and TCP.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack

## FINAL_RESPONSE

```TypeScript
FINAL_RESPONSE = 'FINAL_RESPONSE'
```

Intercept when we get the final HTTP response.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Communication.NetStack
