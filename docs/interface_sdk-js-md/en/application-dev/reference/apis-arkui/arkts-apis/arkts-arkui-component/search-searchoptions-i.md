# SearchOptions

Options used to construct the search.

Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SearchOptions--><!--Device-unnamed-export declare interface SearchOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: SearchController
```

Controller of the \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ component.

Anonymous Object Rectification.

**Type:** SearchController

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-controller?: SearchController--><!--Device-SearchOptions-controller?: SearchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: string
```

Path to the search icon.

Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The icon data source can be a local or online image.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_The supported formats include PNG, JPG, BMP, SVG, GIF, pixelmap, and HEIF.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_The Base64 string is supported in the following format:data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data], where [base64 data] is a Base64 string.\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_If this attribute and the searchIcon attribute are both set, the searchIcon attribute takes precedence.\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_

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

Text displayed when there is no input.

Anonymous Object Rectification.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-placeholder?: ResourceStr--><!--Device-SearchOptions-placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: string | Bindable<string>
```

Text input in the search text box.

**Type:** string \| Bindable&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-value?: string | Bindable<string>--><!--Device-SearchOptions-value?: string | Bindable<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

