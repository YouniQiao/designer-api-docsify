# HttpResponse

Defines the response to an HTTP request.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-http-export interface HttpResponse--><!--Device-http-export interface HttpResponse-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## connectionExtraInfo

```TypeScript
connectionExtraInfo?: ConnectionExtraInfo
```

Information details of HTTP request.

**类型：** [ConnectionExtraInfo](arkts-network-http-connectionextrainfo-i.md)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

<!--Device-HttpResponse-connectionExtraInfo?: ConnectionExtraInfo--><!--Device-HttpResponse-connectionExtraInfo?: ConnectionExtraInfo-End-->

**系统能力：** SystemCapability.Communication.NetStack

## cookies

```TypeScript
cookies: string
```

Cookies returned by the server.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpResponse-cookies: string--><!--Device-HttpResponse-cookies: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

## header

```TypeScript
header: Object
```

All headers in the response from the server.

**类型：** Object

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpResponse-header: Object--><!--Device-HttpResponse-header: Object-End-->

**系统能力：** SystemCapability.Communication.NetStack

## performanceTiming

```TypeScript
performanceTiming: PerformanceTiming
```

The time taken of various stages of HTTP request.

**类型：** [PerformanceTiming](arkts-network-http-performancetiming-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-HttpResponse-performanceTiming: PerformanceTiming--><!--Device-HttpResponse-performanceTiming: PerformanceTiming-End-->

**系统能力：** SystemCapability.Communication.NetStack

## responseCode

```TypeScript
responseCode: ResponseCode | int
```

Server status code.

**类型：** ArkTS-Dyn: [ResponseCode](arkts-network-http-responsecode-e.md) \| number  <br>ArkTS-Sta：[ResponseCode](arkts-network-http-responsecode-e.md) \| int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpResponse-responseCode: ResponseCode | int--><!--Device-HttpResponse-responseCode: ResponseCode | int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## result

```TypeScript
result: string | Object | ArrayBuffer
```

result can be a string (API 6) or an ArrayBuffer(API 8). Object is deprecated from API 8.If {@link HttpRequestOptions#expectDataType} is set, the system preferentially returns this parameter.

**类型：** string \| Object \| ArrayBuffer

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpResponse-result: string | Object | ArrayBuffer--><!--Device-HttpResponse-result: string | Object | ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

## resultType

```TypeScript
resultType: HttpDataType
```

If the resultType is string, you can get result directly.If the resultType is Object, you can get result such as this: result['key'].If the resultType is ArrayBuffer, you can use ArrayBuffer to create the binary objects.

**类型：** [HttpDataType](arkts-network-http-httpdatatype-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HttpResponse-resultType: HttpDataType--><!--Device-HttpResponse-resultType: HttpDataType-End-->

**系统能力：** SystemCapability.Communication.NetStack

