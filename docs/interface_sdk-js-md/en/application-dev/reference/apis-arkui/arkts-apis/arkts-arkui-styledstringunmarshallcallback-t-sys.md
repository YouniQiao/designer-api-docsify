# StyledStringUnmarshallCallback (System API)

```TypeScript
declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue
```

Defines a callback for unmarshalling an ArrayBuffer to obtain [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md#styledstringmarshallingvalue-system-api).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue--><!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | Marshaled data of [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md#styledstringmarshallingvalue-system-api). |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md) | [StyledStringMarshallingValue]{ |

