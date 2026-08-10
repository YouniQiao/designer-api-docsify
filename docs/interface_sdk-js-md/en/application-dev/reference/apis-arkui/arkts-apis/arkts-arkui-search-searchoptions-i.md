# SearchOptions

Search初始化参数。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SearchOptions--><!--Device-unnamed-export declare interface SearchOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: SearchController
```

设置Search组件控制器。

**Type:** [SearchController](../arkts-components/arkts-arkui-searchcontroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-controller?: SearchController--><!--Device-SearchOptions-controller?: SearchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: string
```

设置搜索图标路径，默认使用系统搜索图标。

**说明：**

icon的数据源支持[使用相对路径显示图片](../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#示例25使用相对路径显示图片)和网络图片。

- 支持的图片格式包括png、jpg、bmp、svg、gif、pixelmap和heif。

- 支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data], 其中[base64 data]为Base64字符串数据。

如果与属性searchIcon同时设置，则searchIcon优先。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-icon?: string--><!--Device-SearchOptions-icon?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

设置无输入时的提示文本。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-placeholder?: ResourceStr--><!--Device-SearchOptions-placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: string | Bindable<string>
```

设置当前显示的搜索文本内容。

该属性支持Bindable双向绑定变量。

**Type:** string \| Bindable&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-value?: string | Bindable<string>--><!--Device-SearchOptions-value?: string | Bindable<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

