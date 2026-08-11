# @ohos.inputMethodList(输入法切换列表控件)

**@ohos.inputMethodList**模块是面向系统应用和输入法应用的UI控件模块，提供了输入法切换列表弹窗组件。
 本模块是一个声明式UI组件模块，提供`InputMethodListDialog`自定义弹窗组件，用于展示系统默认输入法子类型和第三方输入法应用列表，并可选地提供输入法模式切换入口（如单手模式、全屏模式等）。
 通过本模块提供的弹窗组件，用户可以在输入法列表中查看当前系统中已安装的所有输入法，并从默认输入法切换到其他输入法；对于系统预置输入法，还可在列表中展示模式选项（如单手模式、全屏模式），供用户切换输入法键盘的显示模式。
 当系统应用或输入法应用需要提供输入法切换入口时使用本模块。典型场景包括：系统设置应用中的输入法管理页面、输入法应用自身的设置界面、或其他需要让用户选择和切换输入法的系统级界面。本组件仅系统应用和输入法应用可调用，
 `patternOptions`参数仅系统预置输入法支持。
 本模块与输入法框架其他模块的关系如下：
 — [@ohos.inputMethod](arkts-inputmethod.md)：面向普通前台应用，提供输入法的控制与管理能力（如显示/隐藏软键盘、切换输入法等），可通过程序化接口
 `switchInputMethod`切换输入法，适用于无需交互式选择界面的场景。
 — [@ohos.inputMethodEngine](arkts-inputmethodengine.md)：面向输入法应用，提供创建软键盘窗口、插入/删除字符等输入法服务端能力。
 — **@ohos.inputMethodList（本模块）**：面向系统应用和输入法应用，提供可视化的输入法切换列表弹窗控件，适用于需要交互式选择界面的场景。
 本模块包含以下关键组件和接口：
| Interface/Struct |
|---|
| **InputMethodListDialog** |
| **PatternOptions** |
| **Pattern** |
 使用`InputMethodListDialog`需要多个API组合配合：创建`CustomDialogController` -> 配置`PatternOptions`（可选） -> 在
 `CustomDialogController`的builder中构建`InputMethodListDialog` -> 通过`CustomDialogController.open()`打开弹窗。
 ###### 子组件
 无
 ###### 属性
 不支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)
 ######  事件
 不支持[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)


## 汇总

### 结构体

| 名称 |
| --- |
| [InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md) |

### 接口

| 名称 |
| --- |
| [Pattern](arkts-ime-inputmethodlist-pattern-i.md) |
| [PatternOptions](arkts-ime-inputmethodlist-patternoptions-i.md) |
