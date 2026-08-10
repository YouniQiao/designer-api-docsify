# StyledStringMarshallCallback (System API)

```TypeScript
declare type StyledStringMarshallCallback = (marshallableVal: StyledStringMarshallingValue) => ArrayBuffer
```

属性字符串[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)序列化回调类型。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type StyledStringMarshallCallback = (marshallableVal: StyledStringMarshallingValue) => ArrayBuffer--><!--Device-unnamed-declare type StyledStringMarshallCallback = (marshallableVal: StyledStringMarshallingValue) => ArrayBuffer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| marshallableVal | [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md) | Yes | 属性字符串中需要自定义序列化的UserDataSpan对象。开发者在回调函数中根据此参数的类型，选择对应的序列化接口将 其转换为ArrayBuffer。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArrayBuffer | [StyledStringMarshallingValue]{ |

