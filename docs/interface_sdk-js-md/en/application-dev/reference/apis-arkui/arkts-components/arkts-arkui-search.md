# Search

搜索框组件，支持搜索图标、清除按钮、搜索按钮、placeholder提示文本、自定义键盘等功能配置，适用于浏览器的搜索内容输入框、应用内搜索等场景。

> **说明：**
>
> 该组件仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor]{@link ./rich_editor}组件。

## 子组件

无

## Search

```TypeScript
Search(options?: SearchOptions)
```

定义搜索组件构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchInterface-(options?: SearchOptions): SearchAttribute--><!--Device-SearchInterface-(options?: SearchOptions): SearchAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SearchOptions](arkts-arkui-searchoptions-i.md) | No | 搜索框组件初始化选项。当需要设置搜索框的初始值、提示文本、图标或控制器时传入此参数，不传入时使用默认配置。 |

## Summary

- [CancelButtonOptions](arkts-arkui-search-cancelbuttonoptions-i.md)
- [CancelButtonSymbolOptions](arkts-arkui-search-cancelbuttonsymboloptions-i.md)
- [IconOptions](arkts-arkui-search-iconoptions-i.md)
- [SearchButtonOptions](arkts-arkui-search-searchbuttonoptions-i.md)
- [SearchOptions](arkts-arkui-search-searchoptions-i.md)
- [SearchSubmitCallback](arkts-arkui-search-searchsubmitcallback-t.md)
- [CancelButtonStyle](arkts-arkui-search-cancelbuttonstyle-e.md)
- [SearchType](arkts-arkui-search-searchtype-e.md)
