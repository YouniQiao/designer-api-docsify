# HttpResponse

Defines the response to an HTTP request.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-http-export interface HttpResponse--><!--Device-http-export interface HttpResponse-End-->

**System capability:** SystemCapability.Communication.NetStack

## connectionExtraInfo

```TypeScript
connectionExtraInfo?: ConnectionExtraInfo
```

Information details of HTTP request.

**Type:** ConnectionExtraInfo

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.0.0.

<!--Device-HttpResponse-connectionExtraInfo?: ConnectionExtraInfo--><!--Device-HttpResponse-connectionExtraInfo?: ConnectionExtraInfo-End-->

**System capability:** SystemCapability.Communication.NetStack

## cookies

```TypeScript
cookies: string
```

Cookies returned by the server.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpResponse-cookies: string--><!--Device-HttpResponse-cookies: string-End-->

**System capability:** SystemCapability.Communication.NetStack

## header

```TypeScript
header: Object
```

All headers in the response from the server.

**Type:** Object

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpResponse-header: Object--><!--Device-HttpResponse-header: Object-End-->

**System capability:** SystemCapability.Communication.NetStack

## performanceTiming

```TypeScript
performanceTiming: PerformanceTiming
```

The time taken of various stages of HTTP request.

**Type:** PerformanceTiming

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-HttpResponse-performanceTiming: PerformanceTiming--><!--Device-HttpResponse-performanceTiming: PerformanceTiming-End-->

**System capability:** SystemCapability.Communication.NetStack

## responseCode

```TypeScript
responseCode: ResponseCode | int
```

Server status code.

**Type:** ResponseCode \| int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpResponse-responseCode: ResponseCode | int--><!--Device-HttpResponse-responseCode: ResponseCode | int-End-->

**System capability:** SystemCapability.Communication.NetStack

## result

```TypeScript
result: string | Object | ArrayBuffer
```

result can be a string (API 6) or an ArrayBuffer(API 8). Object is deprecated from API 8.If \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is set, the system preferentially returns this parameter.

**Type:** string \| Object \| ArrayBuffer

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpResponse-result: string | Object | ArrayBuffer--><!--Device-HttpResponse-result: string | Object | ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.NetStack

## resultType

```TypeScript
resultType: HttpDataType
```

If the resultType is string, you can get result directly.If the resultType is Object, you can get result such as this: result['key'].If the resultType is ArrayBuffer, you can use ArrayBuffer to create the binary objects.

**Type:** HttpDataType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HttpResponse-resultType: HttpDataType--><!--Device-HttpResponse-resultType: HttpDataType-End-->

**System capability:** SystemCapability.Communication.NetStack

