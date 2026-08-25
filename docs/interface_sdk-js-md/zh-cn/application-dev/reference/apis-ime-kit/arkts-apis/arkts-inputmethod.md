# @ohos.inputMethod(输入法框架)

@ohos.inputMethod模块是面向普通前台应用（如备忘录、短信、设置等应用）的输入法客户端模块，提供输入法控制和管理能力。 <br> <br>本模块是输入法框架的客户端接口，为编辑框应用提供与输入法服务的交互能力，包括输入法绑定/解绑、软键盘显示/隐藏、输入法切换、输入法列表查询、编辑框属性与光标更新、文本选择与操作事件监听、自定义消息通信等。 <br> <br>本模块提供两大核心能力集：1）通过`InputMethodController`实现编辑框应用与输入法之间的绑定、交互和事件监听——编辑框应用绑定输入法后可控制键盘显隐、更新光标和编辑属性、监听输入法发出的文本操作事件（插入、删除、选 中文本、移动光标、发送功能键和扩展动作等），以及通过自定义消息通道与输入法应用双向通信；2）通过`InputMethodSetting`实现输入法管理——获取输入法列表、查询当前输入法及子类型、订阅输入法切换事件、切换输入法及子类型、 查询面板显示状态等。 <br> <br>当开发带有文本编辑框的应用（需要与输入法交互）或系统应用（需要管理输入法）时使用本模块。典型场景包括：应用中编辑框获取焦点时绑定输入法并显示键盘、编辑框失去焦点时解绑输入法并隐藏键盘、系统设置应用中切换和配置输入法等。 <br> <br>本模块是IME Kit（输入法框架Kit）中的客户端控制模块，与IME Kit中的其他模块协同工作： <br> <br>- @ohos.inputMethodEngine：面向输入法应用的服务端模块，提供软键盘窗口创建、文本插入/删除、监听物理按键等能力。本模块（@ohos.inputMethod）发出的请求（如显示键盘、切换输入法）最终由@ ohos.inputMethodEngine侧的输入法应用响应和处理。 <br>- @ohos.inputMethodList：提供输入法列表选择对话框的显示与管理能力。 <br>- @ohos.inputMethod.Panel：定义输入法面板类型与状态信息，用于查询面板可见性等。 <br> <br>典型的客户端应用（如备忘录、设置）与输入法交互的调用序列如下： <br> <br>1. 通过`inputMethod.getController()`获取客户端控制器实例`InputMethodController`。 <br>2. 通过`InputMethodController.attach()`绑定输入法（对于自绘控件场景），或依赖系统原生编辑框自动绑定。 <br>3. 通过`InputMethodController.showTextInput()`拉起软键盘，进入文本编辑状态。 <br>4. 在编辑过程中，通过`updateCursor`、`changeSelection`、`updateAttribute`等接口向输入法同步编辑框状态。 <br>5. 通过`InputMethodController.hideTextInput()`隐藏软键盘，退出编辑状态。 <br>6. 通过`InputMethodController.detach()`解除与输入法的绑定。 <br> <br>配对约束： <br> <br>- `attach`与`detach`必须配对使用，未detach而直接退出可能导致资源泄漏。 <br>- `showTextInput`与`hideTextInput`必须配对使用，避免输入法状态不一致。 <br> <br>本模块的核心开放能力由以下关键Interface承载： <br> | Interface | 说明 | |---|---| | InputMethodController | 输入法控制器，编辑框应用与输入法交互的核心对象。提供绑定/解绑输入法（attach/detach）、显示/隐藏键盘（showTextInput/hideTextInput）、 更新光标和编辑属性（updateCursor/updateAttribute/changeSelection）、 监听输入法操作事件（insertText/deleteLeft/deleteRight/selectByRange/selectByMovement/moveCursor/sendFunctionKey/sendKeyboardStatus/handleExtendAction/setPreviewText/finishTextPreview）、 自定义消息通信（sendMessage/recvMessage）、停止输入会话等能力。通过`getController()`获取实例。 | | InputMethodSetting | 输入法设置管理对象，提供输入法查询和管理能力。包括获取已启用/已禁用/全部输入法列表（getInputMethods/getAllInputMethods）、 查询指定输入法的子类型列表（listInputMethodSubtype）、获取当前输入法及子类型、订阅输入法切换事件（on('imeChange')）、订阅面板显隐事件（on('imeShow')/on('imeHide')）、 查询面板显示状态（isPanelShown）、启用/禁用输入法（enableInputMethod）、获取输入法自身启用状态（getInputMethodState）等。通过`getSetting()`获取实例。 | <br> <br>此外，本模块还定义了多个关键数据类型： <br> | 类型 | 说明 | |---|---| | InputMethodProperty | 输入法属性信息，描述一个输入法的名称、ID、标签、图标、启用状态等。 | | InputMethodSubtype | 输入法子类型，描述输入法的语言、模式等子类型属性。 | | TextConfig | 编辑框文本配置，包含输入属性（InputAttribute）、光标信息（CursorInfo）、选区信息、窗口ID等。 | | InputAttribute | 输入属性，定义文本输入类型（TextInputType）和回车键类型（EnterKeyType）。 | | CursorInfo | 光标信息，定义光标的位置和尺寸。 | | MessageHandler | 自定义消息处理器，用于接收输入法应用发送的消息并提供终止通知。 | <br> <br>编辑框应用与输入法交互的典型流程涉及InputMethodController的多个API组合调用：获取控制器 -&gt; 绑定输入法 -&gt; 订阅输入法操作事件 -&gt; 在回调中处理文本操作 -&gt; 解绑输入法。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 订阅输入法操作事件（如insertText、deleteLeft等）应在`attach`之前完成，避免事件遗漏。`attach`是编辑框应用使用输入法能力的前提，必须先绑定才能进行后续操作。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getController(输入法框架)](arkts-ime-inputmethod-getcontroller-f.md) |
| [getCurrentInputMethod(输入法框架)](arkts-ime-inputmethod-getcurrentinputmethod-f.md) |
| [getCurrentInputMethodSubtype(输入法框架)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md) |
| [getDefaultInputMethod(输入法框架)](arkts-ime-inputmethod-getdefaultinputmethod-f.md) |
| [getInputMethodController(输入法框架)](arkts-ime-inputmethod-getinputmethodcontroller-f.md) |
| [getInputMethodSetting(输入法框架)](arkts-ime-inputmethod-getinputmethodsetting-f.md) |
| [getSetting(输入法框架)](arkts-ime-inputmethod-getsetting-f.md) |
| [getSystemInputMethodConfigAbility(输入法框架)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md) |
| [offAttachmentDidFail(输入法框架)](arkts-ime-inputmethod-offattachmentdidfail-f.md) |
| [onAttachmentDidFail(输入法框架)](arkts-ime-inputmethod-onattachmentdidfail-f.md) |
| [setSimpleKeyboardEnabled(输入法框架)](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md) |
| [switchCurrentInputMethodAndSubtype(输入法框架)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |
| [switchCurrentInputMethodAndSubtype(输入法框架)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |
| [switchCurrentInputMethodSubtype(输入法框架)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |
| [switchCurrentInputMethodSubtype(输入法框架)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |
| [switchInputMethod(输入法框架)](arkts-ime-inputmethod-switchinputmethod-f.md) |
| [switchInputMethod(输入法框架)](arkts-ime-inputmethod-switchinputmethod-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getCurrentInputMethod(输入法框架)](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md) |
| [getCurrentInputMethodSubtype(输入法框架)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md) |
| [getDefaultInputMethod(输入法框架)](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md) |
| [getSystemInputMethodConfigAbility(输入法框架)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md) |
| [switchInputMethod(输入法框架)](arkts-ime-inputmethod-switchinputmethod-f-sys.md) |
| [switchInputMethodWithUserId(输入法框架)](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AttachOptions(输入法框架)](arkts-ime-inputmethod-attachoptions-i.md) |
| [CursorInfo(输入法框架)](arkts-ime-inputmethod-cursorinfo-i.md) |
| [FunctionKey(输入法框架)](arkts-ime-inputmethod-functionkey-i.md) |
| [InputAttribute(输入法框架)](arkts-ime-inputmethod-inputattribute-i.md) |
| [InputMethodController(输入法框架)](arkts-ime-inputmethod-inputmethodcontroller-i.md) |
| [InputMethodProperty(输入法框架)](arkts-ime-inputmethod-inputmethodproperty-i.md) |
| [InputMethodSetting(输入法框架)](arkts-ime-inputmethod-inputmethodsetting-i.md) |
| [InputWindowInfo(输入法框架)](arkts-ime-inputmethod-inputwindowinfo-i.md) |
| [MessageHandler(输入法框架)](arkts-ime-inputmethod-messagehandler-i.md) |
| [Movement(输入法框架)](arkts-ime-inputmethod-movement-i.md) |
| [Range(输入法框架)](arkts-ime-inputmethod-range-i.md) |
| [TextConfig(输入法框架)](arkts-ime-inputmethod-textconfig-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [InputMethodController(输入法框架)](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) |
| [InputMethodSetting(输入法框架)](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) |
| [InputWindowInfo(输入法框架)](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AttachFailureReason(输入法框架)](arkts-ime-inputmethod-attachfailurereason-e.md) |
| [CapitalizeMode(输入法框架)](arkts-ime-inputmethod-capitalizemode-e.md) | 枚举，定义了文本首字母大写的不同模式。<br> \ | 名称 \| 值 \| 说明 \| \| -------- \| -- \| -------- \| \| NONE \| 0 \| 不进行任何首字母大写处理。<br>使用场景：适用于无需自动大写的输入框，如密码输入、验证码输入等。\ | \| SENTENCES \| 1 \| 每个句子的首字母大写。<br>使用场景：适用于普通文本输入框，如聊天、备忘录等，自动在句号等标点后将首字母大写。\ | \| WORDS \| 2 \| 每个单词首字母大写。<br>使用场景：适用于标题、人名等需要每个单词首字母大写的场景。\ | \| CHARACTERS \| 3 \| 每个字母都大写。<br>使用场景：适用于全大写输入场景，如缩写词输入（如URL中的域名部分）。\ |
| [Direction(输入法框架)](arkts-ime-inputmethod-direction-e.md) |
| [EnabledState(输入法框架)](arkts-ime-inputmethod-enabledstate-e.md) |
| [EnterKeyType(输入法框架)](arkts-ime-inputmethod-enterkeytype-e.md) |
| [ExtendAction(输入法框架)](arkts-ime-inputmethod-extendaction-e.md) |
| [KeyboardStatus(输入法框架)](arkts-ime-inputmethod-keyboardstatus-e.md) |
| [RequestKeyboardReason(输入法框架)](arkts-ime-inputmethod-requestkeyboardreason-e.md) |
| [TextInputType(输入法框架)](arkts-ime-inputmethod-textinputtype-e.md) |

### 类型

| 名称 |
| --- |
| [GetTextCallback(输入法框架)](arkts-ime-inputmethod-gettextcallback-t.md) |
| [GetTextIndexAtCursorCallback(输入法框架)](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) |
| [ImeChangeCallback(输入法框架)](arkts-ime-inputmethod-imechangecallback-t.md) |
| [OnMessageCallback(输入法框架)](arkts-ime-inputmethod-onmessagecallback-t.md) |
| [SetPreviewTextCallback(输入法框架)](arkts-ime-inputmethod-setpreviewtextcallback-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [ImeChangeWithUserIdCallback(输入法框架)](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [MAX_TYPE_NUM(输入法框架)](arkts-ime-inputmethod-con.md#max_type_num) |
