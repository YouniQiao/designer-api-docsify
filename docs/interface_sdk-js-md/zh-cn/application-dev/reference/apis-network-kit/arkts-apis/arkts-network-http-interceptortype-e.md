# InterceptorType

Types of an HTTP interceptor.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export enum InterceptorType--><!--Device-http-export enum InterceptorType-End-->

**系统能力：** SystemCapability.Communication.NetStack

## INITIAL_REQUEST

```TypeScript
INITIAL_REQUEST = 'INITIAL_REQUEST'
```

Intercept after the initial HTTP request is assembled.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-InterceptorType-INITIAL_REQUEST = 'INITIAL_REQUEST'--><!--Device-InterceptorType-INITIAL_REQUEST = 'INITIAL_REQUEST'-End-->

**系统能力：** SystemCapability.Communication.NetStack

## REDIRECTION

```TypeScript
REDIRECTION = 'REDIRECTION'
```

Intercept when we get a redirection responsed and is going to send another request.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-InterceptorType-REDIRECTION = 'REDIRECTION'--><!--Device-InterceptorType-REDIRECTION = 'REDIRECTION'-End-->

**系统能力：** SystemCapability.Communication.NetStack

## CACHE_CHECKED

```TypeScript
CACHE_CHECKED = 'READ_CACHE'
```

Intercept after we checked the HTTP cache.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-InterceptorType-CACHE_CHECKED = 'READ_CACHE'--><!--Device-InterceptorType-CACHE_CHECKED = 'READ_CACHE'-End-->

**系统能力：** SystemCapability.Communication.NetStack

## NETWORK_CONNECT

```TypeScript
NETWORK_CONNECT = 'CONNECT_NETWORK'
```

Intercept when we perform network connection, such as TLS and TCP.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-InterceptorType-NETWORK_CONNECT = 'CONNECT_NETWORK'--><!--Device-InterceptorType-NETWORK_CONNECT = 'CONNECT_NETWORK'-End-->

**系统能力：** SystemCapability.Communication.NetStack

## FINAL_RESPONSE

```TypeScript
FINAL_RESPONSE = 'FINAL_RESPONSE'
```

Intercept when we get the final HTTP response.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-InterceptorType-FINAL_RESPONSE = 'FINAL_RESPONSE'--><!--Device-InterceptorType-FINAL_RESPONSE = 'FINAL_RESPONSE'-End-->

**系统能力：** SystemCapability.Communication.NetStack

