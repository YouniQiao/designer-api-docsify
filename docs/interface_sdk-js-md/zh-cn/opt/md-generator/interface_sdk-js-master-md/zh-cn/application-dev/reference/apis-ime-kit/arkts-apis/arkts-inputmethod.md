# @ohos.inputMethod(输入法框架)

**@ohos.inputMethod**模块是面向普通前台应用（如备忘录、短信、设置等系统应用）的输入法客户端模块，提供输入法控制和管理能力。

本模块是输入法框架的客户端接口，为编辑框应用提供与输入法服务的交互能力，包括输入法绑定/解绑、软键盘显示/隐藏、输入法切换、输入法列表查询、编辑框属性与光标更新、文本选择与操作事件监听、自定义消息通信等。

本模块提供两大核心能力集：1）通过`InputMethodController`实现编辑框应用与输入法之间的绑定、交互和事件监听——编辑框应用绑定输入法后可控制键盘显隐、更新光标和编辑属性、监听输入法发出的文本操作事件（插入、删除、选中文本、移动光标、发送功能键和扩展动作等），以及通过自定义消息通道与输入法应用双向通信；2）通过`InputMethodSetting`实现输入法管理——获取输入法列表、查询当前输入法及子类型、订阅输入法切换事件、切换输入法及子类型、查询面板显示状态等。

当开发带有文本编辑框的应用（需要与输入法交互）或系统应用（需要管理输入法）时使用本模块。典型场景包括：应用中编辑框获取焦点时绑定输入法并显示键盘、编辑框失去焦点时解绑输入法并隐藏键盘、系统设置应用中切换和配置输入法等。

本模块是IME Kit（输入法框架Kit）中的客户端控制模块，与IME Kit中的其他模块协同工作：

- **@ohos.inputMethodEngine**：面向输入法应用的服务端模块，提供软键盘窗口创建、文本插入/删除、监听物理按键等能力。本模块（@ohos.inputMethod）发出的请求（如显示键盘、切换输入法）最终由@  
ohos.inputMethodEngine侧的输入法应用响应和处理。  
- **@ohos.inputMethodList**：提供输入法列表选择对话框的显示与管理能力。  
- **@ohos.inputMethod.Panel**：定义输入法面板类型与状态信息，用于查询面板可见性等。

典型的客户端应用（如备忘录、设置）与输入法交互的调用序列如下：

1. 通过`inputMethod.getController()`获取客户端控制器实例`InputMethodController`。2. 通过`InputMethodController.attach()`绑定输入法（对于自绘控件场景），或依赖系统原生编辑框自动绑定。3. 通过`InputMethodController.showTextInput()`拉起软键盘，进入文本编辑状态。4. 在编辑过程中，通过`updateCursor`、`changeSelection`、`updateAttribute`等接口向输入法同步编辑框状态。5. 通过`InputMethodController.hideTextInput()`隐藏软键盘，退出编辑状态。6. 通过`InputMethodController.detach()`解除与输入法的绑定。

**配对约束：**

- `attach`与`detach`必须配对使用，未detach而直接退出可能导致资源泄漏。  
- `showTextInput`与`hideTextInput`必须配对使用，避免输入法状态不一致。

本模块的核心开放能力由以下关键Interface承载：

| Interface | 说明 |
|---|---|
| **InputMethodController** | 输入法控制器，编辑框应用与输入法交互的核心对象。提供绑定/解绑输入法（attach/detach）、显示/隐藏键盘（showTextInput/hideTextInput/showSoftKeyboard/hideSoftKeyboard）、更新光标和编辑属性（updateCursor/updateAttribute/changeSelection）、监听输入法操作事件（insertText/deleteLeft/deleteRight/selectByRange/selectByMovement/moveCursor/sendFunctionKey/sendKeyboardStatus/handleExtendAction/setPreviewText/finishTextPreview）、自定义消息通信（sendMessage/recvMessage）、停止输入会话等能力。通过`getController()`获取实例。 |
| **InputMethodSetting** |

此外，本模块还定义了多个关键数据类型：

| [类型](#类型) | 说明 |
|---|---|
| **InputMethodProperty** | 输入法属性信息，描述一个输入法的名称、ID、标签、图标、启用状态等。 |
| **InputMethodSubtype** | 输入法子类型，描述输入法的语言、模式等子类型属性。 |
| **TextConfig** | 编辑框文本配置，包含输入属性（InputAttribute）、光标信息（CursorInfo）、选区信息、窗口ID等。 |
| **InputAttribute** | 输入属性，定义文本输入类型（TextInputType）和回车键类型（EnterKeyType）。 |
| **CursorInfo** | 光标信息，定义光标的位置和尺寸。 |
| **MessageHandler** |

编辑框应用与输入法交互的典型流程涉及InputMethodController的多个API组合调用：获取控制器 -> 绑定输入法 -> 订阅输入法操作事件 -> 在回调中处理文本操作 -> 解绑输入法。

**起始版本：** 6

<!--Device-unnamed-declare namespace inputMethod--><!--Device-unnamed-declare namespace inputMethod-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 汇总

### 函数

| 名称 |
| --- |
| [getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller) |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod) |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md#getcurrentinputmethodsubtype) |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f.md#getdefaultinputmethod) |
| [getInputMethodController](arkts-ime-inputmethod-getinputmethodcontroller-f.md#getinputmethodcontroller) |
| [getInputMethodSetting](arkts-ime-inputmethod-getinputmethodsetting-f.md#getinputmethodsetting) |
| [getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting) |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md#getsysteminputmethodconfigability) |
| [offAttachmentDidFail](arkts-ime-inputmethod-offattachmentdidfail-f.md#offattachmentdidfail) |
| [onAttachmentDidFail](arkts-ime-inputmethod-onattachmentdidfail-f.md#onattachmentdidfail) |
| [setSimpleKeyboardEnabled](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md#setsimplekeyboardenabled) |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype) |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype-1) |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype) |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype-1) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod-1) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md#getcurrentinputmethod-1) |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md#getcurrentinputmethodsubtype-1) |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md#getdefaultinputmethod-1) |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md#getsysteminputmethodconfigability-1) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f-sys.md#switchinputmethod-2) |
| [switchInputMethodWithUserId](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md#switchinputmethodwithuserid) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) |
| [FunctionKey](arkts-ime-inputmethod-functionkey-i.md) |
| [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md) |
| [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) |
| [Movement](arkts-ime-inputmethod-movement-i.md) |
| [Range](arkts-ime-inputmethod-range-i.md) |
| [TextConfig](arkts-ime-inputmethod-textconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md) |
| [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md) | 枚举，定义了文本首字母大写的不同模式。  \| 名称 \| 值 \| 说明 \|  \| -------- \| -- \| -------- \|  \| NONE \| 0 \| 不进行任何首字母大写处理。  **使用场景：**适用于无需自动大写的输入框，如密码输入、验证码输入等。\|  \| SENTENCES \| 1 \| 每个句子的首字母大写。  **使用场景：**适用于普通文本输入框，如聊天、备忘录等，自动在句号等标点后将首字母大写。\|  \| WORDS \| 2 \| 每个单词首字母大写。  **使用场景：**适用于标题、人名等需要每个单词首字母大写的场景。\|  \| CHARACTERS \| 3 \| 每个字母都大写。  **使用场景：**适用于全大写输入场景，如缩写词输入（如URL中的域名部分）。\|
| [Direction](arkts-ime-inputmethod-direction-e.md) |
| [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) |
| [EnterKeyType](arkts-ime-inputmethod-enterkeytype-e.md) |
| [ExtendAction](arkts-ime-inputmethod-extendaction-e.md) |
| [KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md) |
| [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) |
| [TextInputType](arkts-ime-inputmethod-textinputtype-e.md) |

### 类型

| 名称 |
| --- |
| [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md#max_type_num) |
