# @ohos.inputMethodEngine(Input Method Service)

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; &gt;The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKeyboardDelegate(Input Method Service)](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md) |
| [getInputMethodAbility(Input Method Service)](arkts-ime-inputmethodengine-getinputmethodability-f.md) |
| [getInputMethodAbility(Input Method Service)](arkts-ime-inputmethodengine-getinputmethodability-f.md) |
| [getInputMethodEngine(Input Method Service)](arkts-ime-inputmethodengine-getinputmethodengine-f.md) |
| [getKeyboardDelegate(Input Method Service)](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) |
| [getKeyboardDelegate(Input Method Service)](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachOptions(Input Method Service)](arkts-ime-inputmethodengine-attachoptions-i.md) |
| [EditorAttribute(Input Method Service)](arkts-ime-inputmethodengine-editorattribute-i.md) |
| [EnhancedPanelRect(Input Method Service)](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) |
| [ImmersiveEffect(Input Method Service)](arkts-ime-inputmethodengine-immersiveeffect-i.md) |
| [InputClient(Input Method Service)](arkts-ime-inputmethodengine-inputclient-i.md) |
| [InputMethodAbility(Input Method Service)](arkts-ime-inputmethodengine-inputmethodability-i.md) |
| [InputMethodEngine(Input Method Service)](arkts-ime-inputmethodengine-inputmethodengine-i.md) |
| [KeyboardArea(Input Method Service)](arkts-ime-inputmethodengine-keyboardarea-i.md) |
| [KeyboardController(Input Method Service)](arkts-ime-inputmethodengine-keyboardcontroller-i.md) |
| [KeyboardDelegate(Input Method Service)](arkts-ime-inputmethodengine-keyboarddelegate-i.md) |
| [KeyEvent(Input Method Service)](arkts-ime-inputmethodengine-keyevent-i.md) |
| [MessageHandler(Input Method Service)](arkts-ime-inputmethodengine-messagehandler-i.md) |
| [Movement(Input Method Service)](arkts-ime-inputmethodengine-movement-i.md) |
| [Panel(Input Method Service)](arkts-ime-inputmethodengine-panel-i.md) |
| [PanelInfo(Input Method Service)](arkts-ime-inputmethodengine-panelinfo-i.md) |
| [PanelRect(Input Method Service)](arkts-ime-inputmethodengine-panelrect-i.md) |
| [Range(Input Method Service)](arkts-ime-inputmethodengine-range-i.md) |
| [SystemPanelInsets(Input Method Service)](arkts-ime-inputmethodengine-systempanelinsets-i.md) |
| [TextInputClient(Input Method Service)](arkts-ime-inputmethodengine-textinputclient-i.md) |
| [WindowInfo(Input Method Service)](arkts-ime-inputmethodengine-windowinfo-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EditorAttribute(Input Method Service)](arkts-ime-inputmethodengine-editorattribute-i-sys.md) |
| [ImmersiveEffect(Input Method Service)](arkts-ime-inputmethodengine-immersiveeffect-i-sys.md) |
| [Panel(Input Method Service)](arkts-ime-inputmethodengine-panel-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CapitalizeMode(Input Method Service)](arkts-ime-inputmethodengine-capitalizemode-e.md) | Enumerates the modes of capitalizing the first letter of a text.<br> <br> \| Name\| Value\| Description\| \| -------- \| -- \| -------- \| \| NONE \| 0 \| The first letter is not capitalized.\| \| SENTENCES \| 1 \| The first letter of each sentence is capitalized.\| \| WORDS \| 2 \| The first letter of each word is capitalized.\| \| CHARACTERS \| 3 \| All letters are capitalized.\|
| [Direction(Input Method Service)](arkts-ime-inputmethodengine-direction-e.md) |
| [ExtendAction(Input Method Service)](arkts-ime-inputmethodengine-extendaction-e.md) |
| [GradientMode(Input Method Service)](arkts-ime-inputmethodengine-gradientmode-e.md) | Enumerates the gradient modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The gradient mode is not used.\| \| LINEAR_GRADIENT \| 1 \| Linear gradient.\|
| [ImmersiveMode(Input Method Service)](arkts-ime-inputmethodengine-immersivemode-e.md) | Enumerates the immersive modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE_IMMERSIVE \| 0 \| The immersive mode is not used.\| \| IMMERSIVE \| 1 \| The immersive mode is used. Its style is determined by the input method application.\| \| LIGHT_IMMERSIVE \| 2 \| Immersive style in light mode.\| \| DARK_IMMERSIVE \| 3 \| Immersive style in dark mode.\|
| [PanelFlag(Input Method Service)](arkts-ime-inputmethodengine-panelflag-e.md) | Enumerates the state types of the input method panel.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| FLG_FIXED \| 0 \| Fixed state type.\| \| FLG_FLOATING \| 1 \| Floating state type.\| \| FLAG_CANDIDATE & lt;sup & gt;15+ & lt;/sup & gt; \ | 2 \| Candidate state type.\|
| [PanelType(Input Method Service)](arkts-ime-inputmethodengine-paneltype-e.md) | Enumerates the types of the input method panel.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| SOFT_KEYBOARD \| 0 \| Soft keyboard type.\| \| STATUS_BAR \| 1 \| Status bar type.\|
| [RequestKeyboardReason(Input Method Service)](arkts-ime-inputmethodengine-requestkeyboardreason-e.md) | Enumerates the reasons for requesting keyboard input.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The keyboard request is triggered for no reason.\| \| MOUSE \| 1 \| The keyboard request is triggered by a mouse operation.\| \| TOUCH \| 2 \| The keyboard request is triggered by a touch operation.\| \| OTHER \| 20 \| The keyboard request is triggered by other reasons.\|
| [SecurityMode(Input Method Service)](arkts-ime-inputmethodengine-securitymode-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FluidLightMode(Input Method Service)](arkts-ime-inputmethodengine-fluidlightmode-e-sys.md) | Enumerates the fluid light modes of the input method.<br> <br> \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| NONE \| 0 \| The fluid light mode is not used.\| \| BACKGROUND_FLUID_LIGHT \| 1 \| When the background fluid light mode is enabled, the system panel turns transparent. The fluid light effect must be implemented by the host application of the edit box.\|
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CommandDataType(Input Method Service)](arkts-ime-inputmethodengine-commanddatatype-t.md) |
| [CursorContextChangeCallback(Input Method Service)](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) |
| [IMAInputStartCallback(Input Method Service)](arkts-ime-inputmethodengine-imainputstartcallback-t.md) |
| [InputKeyEventCallback(Input Method Service)](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) |
| [KeyEventCallback(Input Method Service)](arkts-ime-inputmethodengine-keyeventcallback-t.md) |
| [OnMessageCallback(Input Method Service)](arkts-ime-inputmethodengine-onmessagecallback-t.md) |
| [SelectionChangeCallback(Input Method Service)](arkts-ime-inputmethodengine-selectionchangecallback-t.md) |
| [SizeChangeCallback(Input Method Service)](arkts-ime-inputmethodengine-sizechangecallback-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SizeUpdateCallback(Input Method Service)](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CURSOR_DOWN(Input Method Service)](arkts-ime-inputmethodengine-con.md#cursor_down) |
| [CURSOR_LEFT(Input Method Service)](arkts-ime-inputmethodengine-con.md#cursor_left) |
| [CURSOR_RIGHT(Input Method Service)](arkts-ime-inputmethodengine-con.md#cursor_right) |
| [CURSOR_UP(Input Method Service)](arkts-ime-inputmethodengine-con.md#cursor_up) |
| [DISPLAY_MODE_FULL(Input Method Service)](arkts-ime-inputmethodengine-con.md#display_mode_full) |
| [DISPLAY_MODE_PART(Input Method Service)](arkts-ime-inputmethodengine-con.md#display_mode_part) |
| [ENTER_KEY_TYPE_DONE(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_done) |
| [ENTER_KEY_TYPE_GO(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_go) |
| [ENTER_KEY_TYPE_NEWLINE(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_newline) |
| [ENTER_KEY_TYPE_NEXT(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_next) |
| [ENTER_KEY_TYPE_PREVIOUS(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_previous) |
| [ENTER_KEY_TYPE_SEARCH(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_search) |
| [ENTER_KEY_TYPE_SEND(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_send) |
| [ENTER_KEY_TYPE_UNSPECIFIED(Input Method Service)](arkts-ime-inputmethodengine-con.md#enter_key_type_unspecified) |
| [FLAG_SELECTING(Input Method Service)](arkts-ime-inputmethodengine-con.md#flag_selecting) |
| [FLAG_SINGLE_LINE(Input Method Service)](arkts-ime-inputmethodengine-con.md#flag_single_line) |
| [OPTION_ASCII(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_ascii) |
| [OPTION_AUTO_CAP_CHARACTERS(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_auto_cap_characters) |
| [OPTION_AUTO_CAP_SENTENCES(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_auto_cap_sentences) |
| [OPTION_AUTO_WORDS(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_auto_words) |
| [OPTION_MULTI_LINE(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_multi_line) |
| [OPTION_NO_FULLSCREEN(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_no_fullscreen) |
| [OPTION_NONE(Input Method Service)](arkts-ime-inputmethodengine-con.md#option_none) |
| [PATTERN_DATETIME(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_datetime) |
| [PATTERN_EMAIL(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_email) |
| [PATTERN_NEW_PASSWORD(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_new_password) |
| [PATTERN_NULL(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_null) |
| [PATTERN_NUMBER(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_number) |
| [PATTERN_NUMBER_DECIMAL(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_number_decimal) |
| [PATTERN_ONE_TIME_CODE(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_one_time_code) |
| [PATTERN_PASSWORD(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_password) |
| [PATTERN_PASSWORD_NUMBER(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_password_number) |
| [PATTERN_PASSWORD_SCREEN_LOCK(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_password_screen_lock) |
| [PATTERN_PHONE(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_phone) |
| [PATTERN_TEXT(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_text) |
| [PATTERN_URI(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_uri) |
| [PATTERN_USER_NAME(Input Method Service)](arkts-ime-inputmethodengine-con.md#pattern_user_name) |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT(Input Method Service)](arkts-ime-inputmethodengine-con.md#window_type_input_method_float) |
