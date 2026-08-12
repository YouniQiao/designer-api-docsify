# StyledStringUnmarshallCallback (System API)

```TypeScript
declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue
```

Defines a callback for unmarshalling an ArrayBuffer to obtain  
[StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md#StyledStringMarshallingValue).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue--><!--Device-unnamed-declare type StyledStringUnmarshallCallback = (buf: ArrayBuffer) => StyledStringMarshallingValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StyledStringMarshallingValue](arkts-arkui-styledstringmarshallingvalue-t-sys.md) |
