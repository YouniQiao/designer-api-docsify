# @ohos.selectionInput.selectionManager

本模块提供划词管理能力，包括创建面板、显示面板、移动面板、隐藏面板、销毁面板、监听鼠标/触控板划词事件、获取选中文本等。典型使用流程如下： 1. 调用[on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted)订阅划词完成事件。 2. 在回调中调用[getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md#getselectioncontent系统接口)获取选中文本。 3. 调用[createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口)创建划词面板。 4. 调用[setUiContent](arkts-basicservices-selectionmanager-panel-i-sys.md#setuicontent)加载页面内容。 5. 调用[moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)移动面板到指定位置。 6. 调用[show](arkts-basicservices-selectionmanager-panel-i-sys.md#show)显示面板。 7. 调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroypanel系统接口)销毁面板。 8. 调用[off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted)取消订阅划词完成事件。 > **说明：** > > - 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该功能。 > - 仅支持集成了划词扩展的应用调用，划词扩展的实现请参见 > [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#selectionextensionability系统接口)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace selectionManager--><!--Device-unnamed-declare namespace selectionManager-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md#offselectioncomplete) |
| [onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md#onselectioncomplete) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createpanel系统接口) |
| [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroypanel系统接口) |
| [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md#getselectioncontent系统接口) |
| [off_selectionCompleted](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted) |
| [on_selectionCompleted](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i-sys.md) |
| [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [SelectionType](arkts-basicservices-selectionmanager-selectiontype-e-sys.md) | 定义划词方式枚举值。 \| 名称 \| 值 \| 说明 \| \| ------------ \| -- \| ------------------ \| \| MOUSE_MOVE \| 1 \| 鼠标或触控板滑动划词。 \| \| DOUBLE_CLICK \| 2 \| 鼠标或触控板双击划词。 \| \| TRIPLE_CLICK \| 3 \| 鼠标或触控板三击划词。 \|
<!--DelEnd-->
