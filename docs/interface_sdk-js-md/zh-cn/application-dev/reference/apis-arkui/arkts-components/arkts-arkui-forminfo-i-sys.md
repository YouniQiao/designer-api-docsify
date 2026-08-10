# FormInfo（系统接口）

Provides the widget information.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-unnamed-declare interface FormInfo--><!--Device-unnamed-declare interface FormInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## ability

```TypeScript
ability: string
```

Ability name of the widget.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-ability: string--><!--Device-FormInfo-ability: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## bundle

```TypeScript
bundle: string
```

Bundle name of the widget.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-bundle: string--><!--Device-FormInfo-bundle: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## dimension

```TypeScript
dimension?: FormDimension
```

Dimensions of the widget. The 2 x 2, 4 x 4, 4 x 2, and more options are available.

Default value: **Dimension_2_2**

**类型：** [FormDimension](../../apis-form-kit/arkts-apis/arkts-form-forminfo-formdimension-e.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-dimension?: FormDimension--><!--Device-FormInfo-dimension?: FormDimension-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## exemptAppLock

```TypeScript
exemptAppLock?: boolean
```

Whether the widget is exempt from app lock. **true**: The widget is exempt from app lock management. No app lock overlay is displayed when an app lock is applied to the host application. **false**: The widget is managed by app lock. The app lock overlay is displayed when an app lock is applied to the host application.

Default value: **false**.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-FormInfo-exemptAppLock?: boolean--><!--Device-FormInfo-exemptAppLock?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## id

```TypeScript
id: number | string
```

Widget ID. Set this parameter to **0** for a new widget.

**NOTE：**

Different widget hosts cannot use the same ID.

If a widget host uses the same ID for two widgets, the one added later is displayed.

**类型：** number \| string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-id: number | string--><!--Device-FormInfo-id: number | string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## module

```TypeScript
module: string
```

Module name of the widget.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-module: string--><!--Device-FormInfo-module: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## name

```TypeScript
name: string
```

Widget name.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-name: string--><!--Device-FormInfo-name: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## renderingMode

```TypeScript
renderingMode?: FormRenderingMode
```

Widget rendering mode. Default value: **FULL_COLOR**. The options are as follows:

- **FULL_COLOR**: full color mode, where the widget framework does not change the widget effect, which means that   
the widget is displayed in the effect as you set it.  
- **SINGLE_COLOR**: single color mode, where the widget framework sets the widget background to transparent. In   
this mode you need to set the widget style based on the best practices.

**NOTE：**

If the system does not support unified rendering, the widget framework does not set the widget background to transparent in single color mode.

**类型：** [FormRenderingMode](../arkts-apis/arkts-arkui-formcomponent-formrenderingmode-e-sys.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-renderingMode?: FormRenderingMode--><!--Device-FormInfo-renderingMode?: FormRenderingMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## shape

```TypeScript
shape?: FormShape
```

The shape of the form.

**类型：** [FormShape](../../apis-form-kit/arkts-apis/arkts-form-forminfo-formshape-e.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-shape?: FormShape--><!--Device-FormInfo-shape?: FormShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## temporary

```TypeScript
temporary?: boolean
```

Whether the widget is a temporary widget. **true**: The widget is a temporary widget. **false**: The widget is not a temporary widget.

Default value: **false**.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-temporary?: boolean--><!--Device-FormInfo-temporary?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## want

```TypeScript
want?: import('../api/@ohos.app.ability.Want').default
```

The want of the form.

**类型：** import('../api/@ohos.app.ability.Want').default

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-FormInfo-want?: import('../api/@ohos.app.ability.Want').default--><!--Device-FormInfo-want?: import('../api/@ohos.app.ability.Want').default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

