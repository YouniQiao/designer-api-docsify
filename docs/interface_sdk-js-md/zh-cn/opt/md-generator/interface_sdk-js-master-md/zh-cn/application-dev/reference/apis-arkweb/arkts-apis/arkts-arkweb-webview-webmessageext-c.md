# WebMessageExt

The message received or sent from web message port.

**起始版本：** 10

<!--Device-webview-class WebMessageExt--><!--Device-webview-class WebMessageExt-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getArray

```TypeScript
getArray(): Array<string | number | boolean>
```

获取数据对象的数组类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getArray(): Array<string | number | boolean>--><!--Device-WebMessageExt-getArray(): Array<string | number | boolean>-End-->

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

获取数据对象的原始二进制数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer--><!--Device-WebMessageExt-getArrayBuffer(): ArrayBuffer-End-->

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

获取数据对象的布尔类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getBoolean(): boolean--><!--Device-WebMessageExt-getBoolean(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getError

```TypeScript
getError(): Error
```

获取数据对象的错误类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getError(): Error--><!--Device-WebMessageExt-getError(): Error-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Error |

**错误码：**

| 错误码ID |
| --- |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## getNumber

```TypeScript
getNumber(): number
```

获取数据对象的数值类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getNumber(): number--><!--Device-WebMessageExt-getNumber(): number-End-->

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

获取数据对象的字符串类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getString(): string--><!--Device-WebMessageExt-getString(): string-End-->

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
getType(): WebMessageType
```

获取数据对象的类型。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-getType(): WebMessageType--><!--Device-WebMessageExt-getType(): WebMessageType-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md) |

## setArray

```TypeScript
setArray(message: Array<string | number | boolean>): void
```

设置数据对象的数组类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setArray(message: Array<string | number | boolean>): void--><!--Device-WebMessageExt-setArray(message: Array<string | number | boolean>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Array & lt;string \ | number \| boolean & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setArrayBuffer

```TypeScript
setArrayBuffer(message: ArrayBuffer): void
```

设置数据对象的原始二进制数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void--><!--Device-WebMessageExt-setArrayBuffer(message: ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setBoolean

```TypeScript
setBoolean(message: boolean): void
```

设置数据对象的布尔类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setBoolean(message: boolean): void--><!--Device-WebMessageExt-setBoolean(message: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setError

```TypeScript
setError(message: Error): void
```

设置数据对象的错误对象类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setError(message: Error): void--><!--Device-WebMessageExt-setError(message: Error): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Error | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setNumber

```TypeScript
setNumber(message: number): void
```

设置数据对象的数值类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setNumber(message: number): void--><!--Device-WebMessageExt-setNumber(message: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setString

```TypeScript
setString(message: string): void
```

设置数据对象的字符串类型数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setString(message: string): void--><!--Device-WebMessageExt-setString(message: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |

## setType

```TypeScript
setType(type: WebMessageType): void
```

设置数据对象的类型。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebMessageExt-setType(type: WebMessageType): void--><!--Device-WebMessageExt-setType(type: WebMessageType): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100014](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100014-类型和值不匹配) |
