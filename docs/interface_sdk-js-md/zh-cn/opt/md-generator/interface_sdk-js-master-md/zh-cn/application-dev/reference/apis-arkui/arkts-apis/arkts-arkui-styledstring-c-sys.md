# StyledString

属性字符串。

**起始版本：** 12

<!--Device-unnamed-declare class StyledString--><!--Device-unnamed-declare class StyledString-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## marshalling

```TypeScript
static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer
```

序列化属性字符串，通过定义回调来序列化属性字符串的[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)。

当属性字符串包含UserDataSpan等自定义样式，需要自定义序列化逻辑时使用此方法；不包含自定义样式时使用基础版marshalling方法即可。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer--><!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | 是 |
| callback | [StyledStringMarshallCallback](arkts-arkui-styledstringmarshallcallback-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## marshalling

```TypeScript
static marshalling(styledString: StyledString): ArrayBuffer
```

序列化属性字符串。适用于将属性字符串持久化存储或跨进程、跨组件传递时使用。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer--><!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>
```

反序列化后得到属性字符串，通过定义回调来反序列化[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)。

当需要从序列化数据中恢复包含UserDataSpan等自定义样式的属性字符串时使用此方法；恢复不含自定义样式的属性字符串时使用基础版unmarshalling方法即可。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| callback | [StyledStringUnmarshallCallback](arkts-arkui-styledstringunmarshallcallback-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-c-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [170002](../errorcode-styled-string.md#170002-属性字符串解码错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>
```

反序列化后得到属性字符串。

适用于从已序列化的数据中恢复属性字符串时使用，如从本地存储读取或接收跨进程传递的数据后恢复属性字符串。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-c-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [170002](../errorcode-styled-string.md#170002-属性字符串解码错误) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
