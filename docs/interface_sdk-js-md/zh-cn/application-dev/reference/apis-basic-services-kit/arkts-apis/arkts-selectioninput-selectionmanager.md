# @ohos.selectionInput.selectionManager(划词管理)

本模块提供划词管理能力，包括创建面板、显示面板、移动面板、隐藏面板、销毁面板、监听鼠标/触控板划词事件、获取选中文本等。典型使用流程如下：
1. 调用[on('selectionCompleted')](arkts-basicservices-selectionmanager-on-f.md#onselectioncompleted)订阅划词完成事件。
2. 在回调中调用[getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f.md)获取选中文本。
3. 调用[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md)创建划词面板。
4. 调用[setUiContent](arkts-basicservices-selectionmanager-panel-i.md#setuicontent)加载页面内容。
5. 调用[moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay)移动面板到指定位置。
6. 调用[show](arkts-basicservices-selectionmanager-panel-i.md#show)显示面板。
7. 调用[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md)销毁面板。
8. 调用[off('selectionCompleted')](arkts-basicservices-selectionmanager-off-f.md#offselectioncompleted)取消订阅划词完成事件。

> **说明：**&gt;
> - 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该功能。
> - 仅支持集成了划词扩展的应用调用，划词扩展的实现请参见
> [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.SelectionInput.Selection

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createPanel(划词管理)](arkts-basicservices-selectionmanager-createpanel-f.md) |
| [destroyPanel(划词管理)](arkts-basicservices-selectionmanager-destroypanel-f.md) |
| [getSelectionContent(划词管理)](arkts-basicservices-selectionmanager-getselectioncontent-f.md) |
| [off(划词管理)](arkts-basicservices-selectionmanager-off-f.md#offselectioncompleted) |
| [on(划词管理)](arkts-basicservices-selectionmanager-on-f.md#onselectioncompleted) |

### 接口

| 名称 |
| --- |
| [Panel(划词管理)](arkts-basicservices-selectionmanager-panel-i.md) |
| [SelectionInfo(划词管理)](arkts-basicservices-selectionmanager-selectioninfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Panel(划词管理)](arkts-basicservices-selectionmanager-panel-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SelectionType(划词管理)](arkts-basicservices-selectionmanager-selectiontype-e.md) | 定义划词方式枚举值。  \| 名称 \| 值 \| 说明 \| \| ------------ \| -- \| ------------------ \| \| MOUSE_MOVE \| 1 \| 鼠标或触控板滑动划词。 \| \| DOUBLE_CLICK \| 2 \| 鼠标或触控板双击划词。 \| \| TRIPLE_CLICK \| 3 \| 鼠标或触控板三击划词。 \|
