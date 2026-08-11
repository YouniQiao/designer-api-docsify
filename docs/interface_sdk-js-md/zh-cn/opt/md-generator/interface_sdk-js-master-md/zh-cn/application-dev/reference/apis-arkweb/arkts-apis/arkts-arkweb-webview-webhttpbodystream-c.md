# WebHttpBodyStream

The http body stream of the request.

**起始版本：** 12

<!--Device-webview-class WebHttpBodyStream--><!--Device-webview-class WebHttpBodyStream-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getPosition

```TypeScript
getPosition(): number
```

读取WebHttpBodyStream中当前的读取位置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebHttpBodyStream-getPosition(): number--><!--Device-WebHttpBodyStream-getPosition(): number-End-->

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

<!--Device-WebHttpBodyStream-getSize(): number--><!--Device-WebHttpBodyStream-getSize(): number-End-->

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

<!--Device-WebHttpBodyStream-initialize(): Promise<void>--><!--Device-WebHttpBodyStream-initialize(): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

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

<!--Device-WebHttpBodyStream-isChunked(): boolean--><!--Device-WebHttpBodyStream-isChunked(): boolean-End-->

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

<!--Device-WebHttpBodyStream-isEof(): boolean--><!--Device-WebHttpBodyStream-isEof(): boolean-End-->

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

<!--Device-WebHttpBodyStream-isInMemory(): boolean--><!--Device-WebHttpBodyStream-isInMemory(): boolean-End-->

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

<!--Device-WebHttpBodyStream-read(size: number): Promise<ArrayBuffer>--><!--Device-WebHttpBodyStream-read(size: number): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;ArrayBuffer&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
