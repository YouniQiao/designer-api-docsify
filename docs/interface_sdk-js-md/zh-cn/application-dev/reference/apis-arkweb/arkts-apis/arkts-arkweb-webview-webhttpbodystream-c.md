# WebHttpBodyStream

WebHttpBodyStream是HTTP请求体数据流对象，用于在自定义scheme拦截场景中读取POST、PUT等请求的请求体数据。该对象通过WebSchemeHandlerRequest的getHttpBodyStream方 法获取，支持BYTES、FILE、BLOB、CHUNKED类型的数据。开发者可以通过该接口在自定义协议拦截器中读取上行数据，实现对请求体的检视或转发。注意本类中的其他接口需要在 [initialize](#initialize)成功后才能调用。WebHttpBodyStream与[WebSchemeHandlerRequest](arkts-arkweb-webview-webschemehandlerrequest-c.md)配合使用：WebSchemeHandlerRequest代表被拦截 的请求，WebHttpBodyStream代表该请求的HTTP body数据流。通过读取流中的数据，开发者可以获取完整的请求体内容。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## getPosition

```TypeScript
getPosition(): number
```

读取WebHttpBodyStream中当前的读取位置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

获取WebHttpBodyStream中的数据大小，分块传输时总是返回零。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

## initialize

```TypeScript
initialize(): Promise<void>
```

初始化WebHttpBodyStream。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17100022](../errorcode-webview.md#17100022-webhttpbodystream初始化失败) |

## isChunked

```TypeScript
isChunked(): boolean
```

WebHttpBodyStream是否采用分块传输。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isEof

```TypeScript
isEof(): boolean
```

判断WebHttpBodyStream中的所有数据是否都已被读取。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isInMemory

```TypeScript
isInMemory(): boolean
```

判断WebHttpBodyStream中的上传数据是否在内存中。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## read

```TypeScript
read(size: number): Promise<ArrayBuffer>
```

读取WebHttpBodyStream中的数据。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
