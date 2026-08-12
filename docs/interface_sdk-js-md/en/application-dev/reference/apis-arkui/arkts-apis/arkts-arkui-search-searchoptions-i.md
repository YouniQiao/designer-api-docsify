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

Controller of the &lt;Search&gt; component.

Anonymous Object Rectification.

**Type:** [SearchController](arkts-arkui-search-searchcontroller-c.md)

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

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The icon data source can be a local or online image.&lt;ul&gt;&lt;li&gt;The supported formats include PNG, JPG, BMP, SVG, GIF, pixelmap, and HEIF.&lt;/li&gt;&lt;li&gt;The Base64 string is supported in the following format:data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data], where [base64 data] is a Base64 string.&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;If this attribute and the searchIcon attribute are both set, the searchIcon attribute takes precedence.&lt;/p&gt;

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

Text input in the search text box.

**Type:** string \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchOptions-value?: string | Bindable<string>--><!--Device-SearchOptions-value?: string | Bindable<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

