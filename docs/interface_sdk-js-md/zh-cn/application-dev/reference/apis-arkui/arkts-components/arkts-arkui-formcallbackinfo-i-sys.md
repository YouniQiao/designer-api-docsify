# FormCallbackInfo（系统接口）

Represents the parameters for obtaining a widget ID (**formId**) when querying or uninstalling a widget.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-unnamed-interface FormCallbackInfo--><!--Device-unnamed-interface FormCallbackInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## id

```TypeScript
id: number
```

Widget ID of the number type.

**NOTE：**

If the obtained ID is **-1**, the ID is greater than or equal to 2^53. In this case, you need to use **idString** to obtain the ID.

**类型：** number

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormCallbackInfo-id: number--><!--Device-FormCallbackInfo-id: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## idString

```TypeScript
idString: string
```

Widget ID of the string type.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormCallbackInfo-idString: string--><!--Device-FormCallbackInfo-idString: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## isLocked

```TypeScript
isLocked: boolean
```

Indicates whether the form is locked.

**类型：** boolean

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为22。

<!--Device-FormCallbackInfo-isLocked: boolean--><!--Device-FormCallbackInfo-isLocked: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

