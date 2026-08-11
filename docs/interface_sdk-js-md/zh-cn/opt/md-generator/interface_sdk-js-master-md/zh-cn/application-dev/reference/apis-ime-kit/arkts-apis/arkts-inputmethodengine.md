# @ohos.inputMethodEngine(输入法服务)

**@ohos.inputMethodEngine**模块是面向输入法应用（包括系统输入法和第三方输入法）的服务端API模块，提供了输入法应用与系统输入法框架之间的交互能力。

本模块是输入法应用的服务端接口，定义了输入法应用在运行期间所需的全部开放能力，包括输入法生命周期管理、软键盘面板的创建与控制、文本编辑操作（插入、删除、选中文本）、光标控制、物理键盘事件监听、安全模式管理、私有数据通信等。

输入法应用通过本模块可以：1）订阅输入法绑定/解绑事件，感知编辑框的连接与断开；2）创建和管理软键盘面板（固定态、悬浮态、候选态）及状态栏面板，控制面板的显示、隐藏、大小调整、位置移动、沉浸模式等；3）通过InputClient对编辑框进行文本插入、删除、选中文本、移动光标、发送功能键和扩展编辑动作等操作；4）通过KeyboardDelegate监听物理键盘按键事件、光标位置变化、文本选择变化、文本内容变化、编辑框属性变化等；5）管理安全模式（基础模式/完全访问模式），支持隐私面板设置；6）与编辑框应用进行私有数据通信和自定义消息通信。

当开发输入法应用时使用本模块。本模块需在InputMethodExtensionAbility中使用，适用于系统输入法开发、第三方输入法开发、自定义键盘布局等场景。

本模块的核心开放能力由以下关键Interface承载：

| Interface/Class | 说明 |
|---|---|
| **InputMethodAbility** | 输入法能力对象，是输入法应用的核心入口。提供输入法生命周期事件订阅（绑定/解绑/键盘显示隐藏/子类型切换/安全模式变化等）、面板创建与销毁、安全模式获取等能力。通过`getInputMethodAbility()`获取实例。 |
| **KeyboardDelegate** | 键盘代理对象，提供物理键盘按键事件监听、光标位置变化监听、文本选择变化监听、文本内容变化监听、编辑框属性变化监听等能力。通过`getKeyboardDelegate()`获取实例。 |
| **InputClient** | 输入客户端对象，提供对编辑框的文本操作能力，包括插入文本、删除文本（前删/后删）、获取光标前后文本、移动光标、选中文本、发送功能键和扩展编辑动作、设置预览文本、发送私有数据、自定义消息通信等。通过订阅`inputStart`事件在回调中获取实例。 |
| **KeyboardController** | 键盘控制器对象，提供隐藏键盘、退出当前输入类型等能力。通过订阅`inputStart`事件在回调中获取实例。 |
| **Panel** | 输入法面板对象，提供面板页面内容加载、大小调整、位置移动、显示/隐藏、面板状态切换、隐私模式设置、沉浸模式与效果设置、面板矩形区域预设置、热区更新等能力。通过`createPanel()`获取实例。 |
| **MessageHandler** |

输入法应用的典型使用流程涉及多个API的组合调用，核心流程为：获取InputMethodAbility实例 -> 订阅inputStart事件 -> 在回调中获取KeyboardController和InputClient -> 创建Panel -> 加载面板页面内容 -> 通过InputClient操作编辑框文本 -> 通过KeyboardController控制键盘显隐。

**起始版本：** 8

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 汇总

### 函数

| 名称 |
| --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md#createkeyboarddelegate) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability) |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getinputmethodengine) |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate) |

### 接口

| 名称 |
| --- |
| [AttachOptions](arkts-ime-inputmethodengine-attachoptions-i.md) |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) |
| [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i.md) |
| [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) |
| [KeyEvent](arkts-ime-inputmethodengine-keyevent-i.md) |
| [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) |
| [KeyboardController](arkts-ime-inputmethodengine-keyboardcontroller-i.md) |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | KeyboardDelegate是键盘事件监听代理对象，用于输入法应用监听物理键盘按键事件和编辑框文本/光标/选区变化事件。输入法应用通过  [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate)获取该实例。  **核心功能概述：**  - **物理键盘按键事件**：通过on('keyDown'\|'keyUp')订阅物理按键的按下/抬起事件，通过on('keyEvent')订阅更完整的按键事件（含组合键信息）。callback返回true表示按键事件被消费，返回  false表示不消费。  - **光标与选区变化事件**：通过on('cursorContextChange')订阅光标位置变化事件，通过on('selectionChange')订阅文本选区变化事件。输入法应用可根据这些事件调整候选词位置或输入策略。  - **文本变化事件**：通过on('textChange')订阅编辑框文本内容变化事件，输入法应用可据此更新候选词或输入建议。  - **编辑框属性变化事件**：通过on('editorAttributeChanged')订阅编辑框属性变化事件，输入法应用可根据编辑框属性变化动态调整键盘布局。  **使用场景：**  - 开发物理键盘快捷键处理功能时，订阅on('keyDown'\|
| [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md) |
| [Movement](arkts-ime-inputmethodengine-movement-i.md) |
| [Panel](arkts-ime-inputmethodengine-panel-i.md) |
| [PanelInfo](arkts-ime-inputmethodengine-panelinfo-i.md) |
| [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) |
| [Range](arkts-ime-inputmethodengine-range-i.md) |
| [SystemPanelInsets](arkts-ime-inputmethodengine-systempanelinsets-i.md) |
| [TextInputClient](arkts-ime-inputmethodengine-textinputclient-i.md) |
| [WindowInfo](arkts-ime-inputmethodengine-windowinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i-sys.md) |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i-sys.md) |
| [Panel](arkts-ime-inputmethodengine-panel-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [CapitalizeMode](arkts-ime-inputmethodengine-capitalizemode-e.md) | 枚举，定义了文本首字母大写的不同模式。  \| 名称 \| 值 \| 说明 \|  \| -------- \| -- \| -------- \|  \| NONE \| 0 \| 不进行任何首字母大写处理。\|  \| SENTENCES \| 1 \| 每个句子的首字母大写。\|  \| WORDS \| 2 \| 每个单词的首字母大写。\|  \| CHARACTERS \| 3 \| 每个字母都大写。\|
| [Direction](arkts-ime-inputmethodengine-direction-e.md) |
| [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) |
| [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md) | 枚举，输入法渐变模式。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| NONE \| 0 \| 不使用渐变模式。 \|  \| LINEAR_GRADIENT \| 1 \| 线性渐变。 \|
| [ImmersiveMode](arkts-ime-inputmethodengine-immersivemode-e.md) | 枚举，输入法沉浸模式。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| NONE_IMMERSIVE \| 0 \| 不使用沉浸模式。 \|  \| IMMERSIVE \| 1 \| 沉浸模式，由输入法应用确定沉浸模式类型。 \|  \| LIGHT_IMMERSIVE \| 2 \| 浅色沉浸模式。 \|  \| DARK_IMMERSIVE \| 3 \| 深色沉浸模式。 \|
| [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 输入法面板状态类型枚举。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| FLG_FIXED \| 0 \| 固定态面板类型。 \|  \| FLG_FLOATING \| 1 \| 悬浮态面板类型。 \|  \| FLAG_CANDIDATE&lt;sup&gt;15+&lt;/sup&gt; \| 2 \| 候选词态面板类型。 \|
| [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) | 输入法面板类型枚举。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| SOFT_KEYBOARD \| 0 \| 软键盘类型。 \|  \| STATUS_BAR \| 1 \| 状态栏类型。 \|
| [RequestKeyboardReason](arkts-ime-inputmethodengine-requestkeyboardreason-e.md) | 枚举，请求键盘输入的原因。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| NONE \| 0 \| 表示没有特定的原因触发键盘请求。 \|  \| MOUSE \| 1 \| 表示键盘请求是由鼠标操作触发的。 \|  \| TOUCH \| 2 \| 表示键盘请求是由触摸操作触发的。 \|  \| OTHER \| 20 \| 表示键盘请求是由其他原因触发的。 \|
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [FluidLightMode](arkts-ime-inputmethodengine-fluidlightmode-e-sys.md) | 枚举，输入法流光模式。  \| 名称 \| 值 \| 说明 \|  \| ------------ \| -- \| ------------------ \|  \| NONE \| 0 \| 不使用流光模式。 \|  \| BACKGROUND_FLUID_LIGHT \| 1 \| 开启背景流光模式。系统面板变为透明，流光效果由编辑框宿主应用实现。 \|
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md) |
| [SizeChangeCallback](arkts-ime-inputmethodengine-sizechangecallback-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) |
<!--DelEnd-->

### 常量

| 名称 |
| --- |
| [CURSOR_DOWN](arkts-ime-inputmethodengine-con.md#cursor_down) |
| [CURSOR_LEFT](arkts-ime-inputmethodengine-con.md#cursor_left) |
| [CURSOR_RIGHT](arkts-ime-inputmethodengine-con.md#cursor_right) |
| [CURSOR_UP](arkts-ime-inputmethodengine-con.md#cursor_up) |
| [DISPLAY_MODE_FULL](arkts-ime-inputmethodengine-con.md#display_mode_full) |
| [DISPLAY_MODE_PART](arkts-ime-inputmethodengine-con.md#display_mode_part) |
| [ENTER_KEY_TYPE_DONE](arkts-ime-inputmethodengine-con.md#enter_key_type_done) |
| [ENTER_KEY_TYPE_GO](arkts-ime-inputmethodengine-con.md#enter_key_type_go) |
| [ENTER_KEY_TYPE_NEWLINE](arkts-ime-inputmethodengine-con.md#enter_key_type_newline) |
| [ENTER_KEY_TYPE_NEXT](arkts-ime-inputmethodengine-con.md#enter_key_type_next) |
| [ENTER_KEY_TYPE_PREVIOUS](arkts-ime-inputmethodengine-con.md#enter_key_type_previous) |
| [ENTER_KEY_TYPE_SEARCH](arkts-ime-inputmethodengine-con.md#enter_key_type_search) |
| [ENTER_KEY_TYPE_SEND](arkts-ime-inputmethodengine-con.md#enter_key_type_send) |
| [ENTER_KEY_TYPE_UNSPECIFIED](arkts-ime-inputmethodengine-con.md#enter_key_type_unspecified) |
| [FLAG_SELECTING](arkts-ime-inputmethodengine-con.md#flag_selecting) |
| [FLAG_SINGLE_LINE](arkts-ime-inputmethodengine-con.md#flag_single_line) |
| [OPTION_ASCII](arkts-ime-inputmethodengine-con.md#option_ascii) |
| [OPTION_AUTO_CAP_CHARACTERS](arkts-ime-inputmethodengine-con.md#option_auto_cap_characters) |
| [OPTION_AUTO_CAP_SENTENCES](arkts-ime-inputmethodengine-con.md#option_auto_cap_sentences) |
| [OPTION_AUTO_WORDS](arkts-ime-inputmethodengine-con.md#option_auto_words) |
| [OPTION_MULTI_LINE](arkts-ime-inputmethodengine-con.md#option_multi_line) |
| [OPTION_NONE](arkts-ime-inputmethodengine-con.md#option_none) |
| [OPTION_NO_FULLSCREEN](arkts-ime-inputmethodengine-con.md#option_no_fullscreen) |
| [PATTERN_DATETIME](arkts-ime-inputmethodengine-con.md#pattern_datetime) |
| [PATTERN_EMAIL](arkts-ime-inputmethodengine-con.md#pattern_email) |
| [PATTERN_NEW_PASSWORD](arkts-ime-inputmethodengine-con.md#pattern_new_password) |
| [PATTERN_NULL](arkts-ime-inputmethodengine-con.md#pattern_null) |
| [PATTERN_NUMBER](arkts-ime-inputmethodengine-con.md#pattern_number) |
| [PATTERN_NUMBER_DECIMAL](arkts-ime-inputmethodengine-con.md#pattern_number_decimal) |
| [PATTERN_ONE_TIME_CODE](arkts-ime-inputmethodengine-con.md#pattern_one_time_code) |
| [PATTERN_PASSWORD](arkts-ime-inputmethodengine-con.md#pattern_password) |
| [PATTERN_PASSWORD_NUMBER](arkts-ime-inputmethodengine-con.md#pattern_password_number) |
| [PATTERN_PASSWORD_SCREEN_LOCK](arkts-ime-inputmethodengine-con.md#pattern_password_screen_lock) |
| [PATTERN_PHONE](arkts-ime-inputmethodengine-con.md#pattern_phone) |
| [PATTERN_TEXT](arkts-ime-inputmethodengine-con.md#pattern_text) |
| [PATTERN_URI](arkts-ime-inputmethodengine-con.md#pattern_uri) |
| [PATTERN_USER_NAME](arkts-ime-inputmethodengine-con.md#pattern_user_name) |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT](arkts-ime-inputmethodengine-con.md#window_type_input_method_float) |
