# JsMessageExt

该消息用于指示JavaScript代码执行结果的状态。

**起始版本：** 10

<!--Device-webview-class JsMessageExt--><!--Device-webview-class JsMessageExt-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getArray

```TypeScript
getArray(): Array<string | number | boolean>
```

获取JavaScript代码执行结果的数组类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getArray(): Array<string | number | boolean>--><!--Device-JsMessageExt-getArray(): Array<string | number | boolean>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array & lt;string \ | number \| boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getArrayBuffer

```TypeScript
getArrayBuffer(): ArrayBuffer
```

获取JavaScript代码执行结果的原始二进制数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-JsMessageExt-getArrayBuffer(): ArrayBuffer-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getBoolean

```TypeScript
getBoolean(): boolean
```

获取JavaScript代码执行结果的布尔类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getBoolean(): boolean--><!--Device-JsMessageExt-getBoolean(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getErrorDescription

```TypeScript
getErrorDescription(): string | null
```

获取JS执行的异常信息，并将其序列化为字符串。

**起始版本：** 22

<!--Device-JsMessageExt-getErrorDescription(): string | null--><!--Device-JsMessageExt-getErrorDescription(): string | null-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string | If an exception occurs, or the returned type is object, return the serialized string in the format of "Not support type: & lt;{exception\ |

## getNumber

```TypeScript
getNumber(): number
```

获取JavaScript代码执行结果的数值类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getNumber(): number--><!--Device-JsMessageExt-getNumber(): number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getString

```TypeScript
getString(): string
```

获取JavaScript代码执行结果的字符串类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getString(): string--><!--Device-JsMessageExt-getString(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getType

```TypeScript
getType(): JsMessageType
```

获取数据对象的类型。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-JsMessageExt-getType(): JsMessageType--><!--Device-JsMessageExt-getType(): JsMessageType-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [JsMessageType](arkts-arkweb-webview-jsmessagetype-e.md) |
