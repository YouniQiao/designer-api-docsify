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
 | Interface/Struct | 说明 |
 |---|---|
 | **InputMethodListDialog** | 输入法切换列表弹窗组件，使用`@CustomDialog`装饰器声明。展示输入法列表和可选的模式切换入口，是本模块的核心UI组件。需要传入`CustomDialogController`控制弹窗的打开与关闭，可选传入`PatternOptions`配置模式切换功能。 |
 | **PatternOptions** | 输入法模式选项配置接口，定义模式选项的资源数组、默认选中索引和模式切换回调。仅系统预置输入法支持传入此参数。 |
 | **Pattern** | 单个输入法模式的图标定义接口，包含默认图标和选中状态图标两个资源属性。 |
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

| 名称 | 说明 |
| --- | --- |
| [InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md) | InputMethodListDialog({controller: CustomDialogController, patternOptions?: PatternOptions})  输入法切换列表弹窗控件。以弹窗形式展示当前系统中已安装的输入法应用列表，支持用户在输入法之间进行切换；对于默认输入法，还提供键盘模式（如单手模式、全屏模式等）的切换入口。  **使用场景：** 当系统应用或输入法应用需要为用户提供可视化的输入法选择和切换功能时使用此控件。例如，在系统设置应用中允许用户选择不同输入法，或在输入法应用中允许用户切换到其他输入法或切换当前输入法的键盘模式。  **使用后效果：** 调用此控件后，将弹出输入法切换列表弹窗。用户在弹窗中选择输入法后，系统将切换到指定的输入法；若用户选择了默认输入法的模式选项，系统将按指定模式显示键盘布局。  **相似接口差异点及选取原则：** 与[inputMethod.switchInputMethod]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_接口相比，本控件提供了可视化的输入法选择界面，适用于需要交互式选择界面的场景；switchInputMethod接口适用于程序化切换输入法的场景，无需用户手动选择。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [Pattern](arkts-ime-inputmethodlist-pattern-i.md) | 输入法模式选项的图标资源定义，用于配置键盘模式在弹窗中的视觉表现。仅当前输入法（即系统预置输入法）可使用。 |
| [PatternOptions](arkts-ime-inputmethodlist-patternoptions-i.md) | 输入法模式选项配置，用于定义键盘模式的切换选项。 |

