# StyledString

StyledString

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class StyledString--><!--Device-unnamed-export declare class StyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## marshalling

```TypeScript
static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):
        ArrayBuffer | undefined
```

Returns ArrayBuffer from the serialized styled string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):        ArrayBuffer | undefined--><!--Device-StyledString-static marshalling(styledString: StyledString, callback: StyledStringMarshallCallback):        ArrayBuffer | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | StyledString parameter. |
| callback | [StyledStringMarshallCallback](arkts-arkui-styledstringmarshallcallback-t-sys.md) | Yes | When marshalling StyledStringMarshingValue, will trigger this callback to get ArrayBuffer |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer |  |

## marshalling

```TypeScript
static marshalling(styledString: StyledString): ArrayBuffer | undefined
```

Returns ArrayBuffer from the serialized styled string.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer | undefined--><!--Device-StyledString-static marshalling(styledString: StyledString): ArrayBuffer | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | StyledString parameter. |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer |  |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):
        Promise<StyledString | undefined>
```

Returns StyledString from the deserialized ArrayBuffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):        Promise<StyledString | undefined>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer, callback: StyledStringUnmarshallCallback):        Promise<StyledString | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | The buffer will be deserialized to a StyledString. |
| callback | [StyledStringUnmarshallCallback](arkts-arkui-styledstringunmarshallcallback-t-sys.md) | Yes | When unmarshalling ArrayBuffer, will trigger this callback to get StyledStringMarshingValue. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [170002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-styled-string.md#170002-styled-string-decoding-error) | Styled string decode error. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## unmarshalling

```TypeScript
static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>
```

Returns StyledString from the deserialized ArrayBuffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>--><!--Device-StyledString-static unmarshalling(buffer: ArrayBuffer): Promise<StyledString | undefined>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | The buffer will be deserialized to a StyledString. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[StyledString](arkts-arkui-styledstring-styledstring-c.md) \| undefined&gt; |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [170002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-styled-string.md#170002-styled-string-decoding-error) | Styled string decode error. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

