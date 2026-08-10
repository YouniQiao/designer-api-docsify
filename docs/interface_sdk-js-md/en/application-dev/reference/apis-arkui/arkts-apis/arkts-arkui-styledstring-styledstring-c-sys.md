# StyledString

属性字符串

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class StyledString--><!--Device-unnamed-export declare class StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marshalling

```TypeScript
static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):
        ArrayBuffer | undefined
```

序列化属性字符串，通过定义回调来序列化属性字符串的[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):        ArrayBuffer | undefined--><!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):        ArrayBuffer | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | Yes | 属性字符串参数。 |
| callback | [StyledStringMarshallCallback](arkts-arkui-styledstringmarshallcallback-t-sys.md) | Yes | 如何序列化[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer |  |

## marshalling

```TypeScript
static marshalling(styledString: StyledString): ArrayBuffer | undefined
```

序列化属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer | undefined--><!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | Yes | 属性字符串参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer |  |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):
        Promise<StyledString | undefined>
```

反序列化后得到属性字符串，通过定义回调来反序列化[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):        Promise<StyledString | undefined>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):        Promise<StyledString | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | 属性字符串序列化后的数据。 |
| callback | [StyledStringUnmarshallCallback](arkts-arkui-styledstringunmarshallcallback-t-sys.md) | Yes | 如何反序列化ArrayBuffer的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;StyledString \| undefined&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 170002 | Styled string decode error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>
```

反序列化后得到属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | 属性字符串序列化后的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;StyledString \| undefined&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 170002 | Styled string decode error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

