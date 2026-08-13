# @ohos.inputMethodEngine

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md#createKeyboardDelegate) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getInputMethodEngine) |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) |

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
| [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) |
| [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) |
| [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) |
| [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) |
| [OnMessageCallback](arkts-ime-inputmethodengine-onmessagecallback-t.md) |
| [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) |
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
| [CURSOR_DOWN](arkts-ime-inputmethodengine-con.md#CURSOR_DOWN) |
| [CURSOR_LEFT](arkts-ime-inputmethodengine-con.md#CURSOR_LEFT) |
| [CURSOR_RIGHT](arkts-ime-inputmethodengine-con.md#CURSOR_RIGHT) |
| [CURSOR_UP](arkts-ime-inputmethodengine-con.md#CURSOR_UP) |
| [DISPLAY_MODE_FULL](arkts-ime-inputmethodengine-con.md#DISPLAY_MODE_FULL) |
| [DISPLAY_MODE_PART](arkts-ime-inputmethodengine-con.md#DISPLAY_MODE_PART) |
| [ENTER_KEY_TYPE_DONE](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_DONE) |
| [ENTER_KEY_TYPE_GO](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_GO) |
| [ENTER_KEY_TYPE_NEWLINE](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_NEWLINE) |
| [ENTER_KEY_TYPE_NEXT](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_NEXT) |
| [ENTER_KEY_TYPE_PREVIOUS](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_PREVIOUS) |
| [ENTER_KEY_TYPE_SEARCH](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_SEARCH) |
| [ENTER_KEY_TYPE_SEND](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_SEND) |
| [ENTER_KEY_TYPE_UNSPECIFIED](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_UNSPECIFIED) |
| [FLAG_SELECTING](arkts-ime-inputmethodengine-con.md#FLAG_SELECTING) |
| [FLAG_SINGLE_LINE](arkts-ime-inputmethodengine-con.md#FLAG_SINGLE_LINE) |
| [OPTION_ASCII](arkts-ime-inputmethodengine-con.md#OPTION_ASCII) |
| [OPTION_AUTO_CAP_CHARACTERS](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_CAP_CHARACTERS) |
| [OPTION_AUTO_CAP_SENTENCES](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_CAP_SENTENCES) |
| [OPTION_AUTO_WORDS](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_WORDS) |
| [OPTION_MULTI_LINE](arkts-ime-inputmethodengine-con.md#OPTION_MULTI_LINE) |
| [OPTION_NONE](arkts-ime-inputmethodengine-con.md#OPTION_NONE) |
| [OPTION_NO_FULLSCREEN](arkts-ime-inputmethodengine-con.md#OPTION_NO_FULLSCREEN) |
| [PATTERN_DATETIME](arkts-ime-inputmethodengine-con.md#PATTERN_DATETIME) |
| [PATTERN_EMAIL](arkts-ime-inputmethodengine-con.md#PATTERN_EMAIL) |
| [PATTERN_NEW_PASSWORD](arkts-ime-inputmethodengine-con.md#PATTERN_NEW_PASSWORD) |
| [PATTERN_NULL](arkts-ime-inputmethodengine-con.md#PATTERN_NULL) |
| [PATTERN_NUMBER](arkts-ime-inputmethodengine-con.md#PATTERN_NUMBER) |
| [PATTERN_NUMBER_DECIMAL](arkts-ime-inputmethodengine-con.md#PATTERN_NUMBER_DECIMAL) |
| [PATTERN_ONE_TIME_CODE](arkts-ime-inputmethodengine-con.md#PATTERN_ONE_TIME_CODE) |
| [PATTERN_PASSWORD](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD) |
| [PATTERN_PASSWORD_NUMBER](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD_NUMBER) |
| [PATTERN_PASSWORD_SCREEN_LOCK](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD_SCREEN_LOCK) |
| [PATTERN_PHONE](arkts-ime-inputmethodengine-con.md#PATTERN_PHONE) |
| [PATTERN_TEXT](arkts-ime-inputmethodengine-con.md#PATTERN_TEXT) |
| [PATTERN_URI](arkts-ime-inputmethodengine-con.md#PATTERN_URI) |
| [PATTERN_USER_NAME](arkts-ime-inputmethodengine-con.md#PATTERN_USER_NAME) |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT](arkts-ime-inputmethodengine-con.md#WINDOW_TYPE_INPUT_METHOD_FLOAT) |
