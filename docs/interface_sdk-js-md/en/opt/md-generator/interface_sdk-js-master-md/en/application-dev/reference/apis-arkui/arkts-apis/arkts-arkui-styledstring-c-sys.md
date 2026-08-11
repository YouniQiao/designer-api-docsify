# StyledString

StyledString

**Since:** 12

<!--Device-unnamed-declare class StyledString--><!--Device-unnamed-declare class StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marshalling

```TypeScript
static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer
```

Marshals a styled string by defining a callback to marshal  
[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer--><!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback): ArrayBuffer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | Yes |
| callback | [StyledStringMarshallCallback](arkts-arkui-styledstringmarshallcallback-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

## marshalling

```TypeScript
static marshalling(styledString: StyledString): ArrayBuffer
```

Marshals a styled string.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer--><!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>
```

Unmarshals a styled string by defining a callback to  
[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback): Promise<StyledString>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |
| callback | [StyledStringUnmarshallCallback](arkts-arkui-styledstringunmarshallcallback-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-c-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [170002](../errorcode-styled-string.md#170002-styled-string-decoding-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>
```

Unmarshals a buffer to obtain a styled string.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-c-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [170002](../errorcode-styled-string.md#170002-styled-string-decoding-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
