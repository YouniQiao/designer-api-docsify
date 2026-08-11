# @ohos.inputMethodEngine

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events.

**Since:** 8

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md#createkeyboarddelegate) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability) |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getinputmethodengine) |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i-sys.md) |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i-sys.md) |
| [Panel](arkts-ime-inputmethodengine-panel-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CapitalizeMode](arkts-ime-inputmethodengine-capitalizemode-e.md) |
| [Direction](arkts-ime-inputmethodengine-direction-e.md) |
| [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) |
| [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md) |
| [ImmersiveMode](arkts-ime-inputmethodengine-immersivemode-e.md) |
| [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) |
| [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) |
| [RequestKeyboardReason](arkts-ime-inputmethodengine-requestkeyboardreason-e.md) |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FluidLightMode](arkts-ime-inputmethodengine-fluidlightmode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md) |
| [SizeChangeCallback](arkts-ime-inputmethodengine-sizechangecallback-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
