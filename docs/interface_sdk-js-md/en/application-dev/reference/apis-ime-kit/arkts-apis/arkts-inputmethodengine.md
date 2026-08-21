# @ohos.inputMethodEngine

@brief The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events. <br> <br>   
> **NOTE：**<br>
> <br> &gt;The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Since:** 23

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md) | @brief Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more. |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md) | @brief Obtains an [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) instance for the input method. This API can be called only by an input method. <br> <br>The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event, create/ destroy an input method panel, and the like. |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md) | @brief Get InputMethodAbility object to subscribe events about IME. |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md) | @brief Obtains an [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) instance for the input method. <br> <br>The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event. |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) | @brief Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) instance for the input method. <br> <br>The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more. |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) | @brief Get KeyboardDelegate object to subscribe key event or events about editor. |

### Interfaces

| Name | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethodengine-attachoptions-i.md) | @brief Defines additional options for binding an input method. |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) | @brief Represents the attributes of the edit box. |
| [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | @brief Indicates the size of the enhanced input method panel, including the custom avoid area and touch area. |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i.md) | @brief Describes the immersive effect. |
| [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | @brief You must first use on('inputStart') to obtain a **InputClient** instance, and then use this instance to call the following APIs. |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | @brief In the following API examples, you must first use [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance. |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) | @brief In the following API examples, you must first use [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md) to obtain an **InputMethodEngine** instance, and then call the APIs using the obtained instance. |
| [KeyEvent](arkts-ime-inputmethodengine-keyevent-i.md) | @brief Represents the attributes of a key. |
| [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | @brief Represents the keyboard area on the panel. |
| [KeyboardController](arkts-ime-inputmethodengine-keyboardcontroller-i.md) | @brief You must first use on('inputStart') to obtain a **KeyboardController** instance, and then use this instance to call the following APIs. |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | @brief In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md) | @brief Represents a custom communication object. <br> <br>  > **NOTE：**<br> > <br> > You can register this object to receive custom communication data sent by the edit box application attached to the input method application. When the custom communication data is received, the [onMessage](arkts-ime-inputmethodengine-messagehandler-i.md#onmessage) callback in this object is triggered. <br> > <br> > This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback of the penultimate registered object is triggered. <br> > <br> > If this object is unregistered, its [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback will be triggered. |
| [Movement](arkts-ime-inputmethodengine-movement-i.md) | @brief Describes the direction in which the cursor moves when the text is selected. |
| [Panel](arkts-ime-inputmethodengine-panel-i.md) | @brief You need to use [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) to obtain the panel instance and then call the following APIs through the instance. |
| [PanelInfo](arkts-ime-inputmethodengine-panelinfo-i.md) | @brief Describes the attributes of the input method panel. |
| [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | @brief Represents the size of the input method panel. |
| [Range](arkts-ime-inputmethodengine-range-i.md) | @brief Describes the range of the selected text. |
| [SystemPanelInsets](arkts-ime-inputmethodengine-systempanelinsets-i.md) | @brief Defines the offset area between the input method soft keyboard and the system panel. |
| [TextInputClient](arkts-ime-inputmethodengine-textinputclient-i.md) | @brief In the following API examples, you must first use on('inputStart') to obtain a **TextInputClient** instance, and then call the APIs using the obtained instance. |
| [WindowInfo](arkts-ime-inputmethodengine-windowinfo-i.md) | @brief Represents window information. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i-sys.md) | @brief Represents the attributes of the edit box. |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i-sys.md) | @brief Describes the immersive effect. |
| [Panel](arkts-ime-inputmethodengine-panel-i-sys.md) | @brief You need to use [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) to obtain the panel instance and then call the following APIs through the instance. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CapitalizeMode](arkts-ime-inputmethodengine-capitalizemode-e.md) | @brief Enumerates the modes of capitalizing the first letter of a text.<br> <br> \| Name\| Value\| Description\| \| -------- \| -- \| -------- \| \| NONE \| 0 \| The first letter is not capitalized.\| \| SENTENCES \| 1 \| The first letter of each sentence is capitalized.\| \| WORDS \| 2 \| The first letter of each word is capitalized.\| \| CHARACTERS \| 3 \| All letters are capitalized.\| |
| [Direction](arkts-ime-inputmethodengine-direction-e.md) | @brief Enumerates the directions of cursor movement of the input method. |
| [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | @brief Describes the type of the extended edit action on the text box. |
| [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md) | @brief Enumerates the gradient modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The gradient mode is not used.\| \| LINEAR_GRADIENT \| 1 \| Linear gradient.\| |
| [ImmersiveMode](arkts-ime-inputmethodengine-immersivemode-e.md) | @brief Enumerates the immersive modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE_IMMERSIVE \| 0 \| The immersive mode is not used.\| \| IMMERSIVE \| 1 \| The immersive mode is used. Its style is determined by the input method application.\| \| LIGHT_IMMERSIVE \| 2 \| Immersive style in light mode.\| \| DARK_IMMERSIVE \| 3 \| Immersive style in dark mode.\| |
| [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | @brief Enumerates the state types of the input method panel.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| FLG_FIXED \| 0 \| Fixed state type.\| \| FLG_FLOATING \| 1 \| Floating state type.\| \| FLAG_CANDIDATE&lt;sup&gt;15+&lt;/sup&gt; \| 2 \| Candidate state type.\| |
| [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) | @brief Enumerates the types of the input method panel.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| SOFT_KEYBOARD \| 0 \| Soft keyboard type.\| \| STATUS_BAR \| 1 \| Status bar type.\| |
| [RequestKeyboardReason](arkts-ime-inputmethodengine-requestkeyboardreason-e.md) | @brief Enumerates the reasons for requesting keyboard input.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The keyboard request is triggered for no reason.\| \| MOUSE \| 1 \| The keyboard request is triggered by a mouse operation.\| \| TOUCH \| 2 \| The keyboard request is triggered by a touch operation.\| \| OTHER \| 20 \| The keyboard request is triggered by other reasons.\| |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) | @brief Describes the security mode. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [FluidLightMode](arkts-ime-inputmethodengine-fluidlightmode-e-sys.md) | @brief Enumerates the fluid light modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The fluid light mode is not used.\| \| BACKGROUND_FLUID_LIGHT \| 1 \| When the background fluid light mode is enabled, the system panel turns transparent. The fluid light effect must be implemented by the host application of the edit box.\| |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md) | @brief Defines the private data type, which varies depending on its function. |
| [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | @brief The callback of 'cursorContextChange' event. |
| [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | @brief The callback of 'inputStart' event. |
| [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | @brief The callback of 'keyEvent' event. |
| [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | @brief The callback of 'keyDown' or 'keyUp' event. |
| [OnMessageCallback](arkts-ime-inputmethodengine-onmessagecallback-t.md) | @brief Callback function on receiving a custom message. |
| [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | @brief The callback of 'selectionChange' event. |
| [SizeChangeCallback](arkts-ime-inputmethodengine-sizechangecallback-t.md) | @brief Callback triggered when the size of the input method panel changes. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | @brief Callback triggered when the size of the input method panel changes. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [CURSOR_DOWN](arkts-ime-inputmethodengine-con.md#cursor_down) | @brief The caret moves downward. |
| [CURSOR_LEFT](arkts-ime-inputmethodengine-con.md#cursor_left) | @brief The caret moves leftward. |
| [CURSOR_RIGHT](arkts-ime-inputmethodengine-con.md#cursor_right) | @brief The caret moves rightward. |
| [CURSOR_UP](arkts-ime-inputmethodengine-con.md#cursor_up) | @brief The caret moves upward. |
| [DISPLAY_MODE_FULL](arkts-ime-inputmethodengine-con.md#display_mode_full) | @brief The edit box is displayed in full screen. |
| [DISPLAY_MODE_PART](arkts-ime-inputmethodengine-con.md#display_mode_part) | @brief The edit box is displayed in half-screen mode. |
| [ENTER_KEY_TYPE_DONE](arkts-ime-inputmethodengine-con.md#enter_key_type_done) | @brief Key that indicates that a task or input is complete. |
| [ENTER_KEY_TYPE_GO](arkts-ime-inputmethodengine-con.md#enter_key_type_go) | @brief Key that executes a command or navigates to a specific location. |
| [ENTER_KEY_TYPE_NEWLINE](arkts-ime-inputmethodengine-con.md#enter_key_type_newline) | @brief Key that inserts a new line. |
| [ENTER_KEY_TYPE_NEXT](arkts-ime-inputmethodengine-con.md#enter_key_type_next) | @brief Key that moves the focus to the next item in a sequence. |
| [ENTER_KEY_TYPE_PREVIOUS](arkts-ime-inputmethodengine-con.md#enter_key_type_previous) | @brief Key that moves the focus to the previous item in a sequence. |
| [ENTER_KEY_TYPE_SEARCH](arkts-ime-inputmethodengine-con.md#enter_key_type_search) | @brief Key that initiates a search operation. |
| [ENTER_KEY_TYPE_SEND](arkts-ime-inputmethodengine-con.md#enter_key_type_send) | @brief Key that sends the text to its target. |
| [ENTER_KEY_TYPE_UNSPECIFIED](arkts-ime-inputmethodengine-con.md#enter_key_type_unspecified) | @brief No function is specified for the key. |
| [FLAG_SELECTING](arkts-ime-inputmethodengine-con.md#flag_selecting) | @brief The edit box is being selected. |
| [FLAG_SINGLE_LINE](arkts-ime-inputmethodengine-con.md#flag_single_line) | @brief The edit box allows only single-line input. |
| [OPTION_ASCII](arkts-ime-inputmethodengine-con.md#option_ascii) | @brief ASCII values are allowed. |
| [OPTION_AUTO_CAP_CHARACTERS](arkts-ime-inputmethodengine-con.md#option_auto_cap_characters) | @brief Characters are allowed. |
| [OPTION_AUTO_CAP_SENTENCES](arkts-ime-inputmethodengine-con.md#option_auto_cap_sentences) | @brief Sentences are allowed. |
| [OPTION_AUTO_WORDS](arkts-ime-inputmethodengine-con.md#option_auto_words) | @brief Words are allowed. |
| [OPTION_MULTI_LINE](arkts-ime-inputmethodengine-con.md#option_multi_line) | @brief Multiple lines are allowed. |
| [OPTION_NONE](arkts-ime-inputmethodengine-con.md#option_none) | @brief No input attribute is specified. |
| [OPTION_NO_FULLSCREEN](arkts-ime-inputmethodengine-con.md#option_no_fullscreen) | @brief Half-screen style. |
| [PATTERN_DATETIME](arkts-ime-inputmethodengine-con.md#pattern_datetime) | @brief Date edit box. |
| [PATTERN_EMAIL](arkts-ime-inputmethodengine-con.md#pattern_email) | @brief Email edit box. |
| [PATTERN_NEW_PASSWORD](arkts-ime-inputmethodengine-con.md#pattern_new_password) | @brief New password edit box. |
| [PATTERN_NULL](arkts-ime-inputmethodengine-con.md#pattern_null) | @brief Any type of edit box. |
| [PATTERN_NUMBER](arkts-ime-inputmethodengine-con.md#pattern_number) | @brief Number edit box. |
| [PATTERN_NUMBER_DECIMAL](arkts-ime-inputmethodengine-con.md#pattern_number_decimal) | @brief Edit box for numbers with decimal points. |
| [PATTERN_ONE_TIME_CODE](arkts-ime-inputmethodengine-con.md#pattern_one_time_code) | @brief Verification code edit box. |
| [PATTERN_PASSWORD](arkts-ime-inputmethodengine-con.md#pattern_password) | @brief Password edit box. |
| [PATTERN_PASSWORD_NUMBER](arkts-ime-inputmethodengine-con.md#pattern_password_number) | @brief Numeric password edit box. |
| [PATTERN_PASSWORD_SCREEN_LOCK](arkts-ime-inputmethodengine-con.md#pattern_password_screen_lock) | @brief Screen lock password edit box. |
| [PATTERN_PHONE](arkts-ime-inputmethodengine-con.md#pattern_phone) | @brief Phone number edit box. |
| [PATTERN_TEXT](arkts-ime-inputmethodengine-con.md#pattern_text) | @brief Text edit box. |
| [PATTERN_URI](arkts-ime-inputmethodengine-con.md#pattern_uri) | @brief URI edit box. |
| [PATTERN_USER_NAME](arkts-ime-inputmethodengine-con.md#pattern_user_name) | @brief User name edit box. |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT](arkts-ime-inputmethodengine-con.md#window_type_input_method_float) | @brief The input method is displayed in a floating window. |

