# StyledStringUnmarshallCallback (System API)

```TypeScript
declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue
```

属性字符串反序列化ArrayBuffer得到[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)回调类型。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue--><!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md)序列化后的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md) | 反序列化得到的自定义数据片段对象，用于恢复用户自定义的样式数据。 |

