# @ohos.inputMethodEngine

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events.

**Since:** 23

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md#createkeyboarddelegate) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability) |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability) |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getinputmethodengine) |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate) |
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
| [CURSOR_DOWN](arkts-ime-inputmethodengine-con.md#cursordown) |
| [CURSOR_LEFT](arkts-ime-inputmethodengine-con.md#cursorleft) |
| [CURSOR_RIGHT](arkts-ime-inputmethodengine-con.md#cursorright) |
| [CURSOR_UP](arkts-ime-inputmethodengine-con.md#cursorup) |
| [DISPLAY_MODE_FULL](arkts-ime-inputmethodengine-con.md#displaymodefull) |
| [DISPLAY_MODE_PART](arkts-ime-inputmethodengine-con.md#displaymodepart) |
| [ENTER_KEY_TYPE_DONE](arkts-ime-inputmethodengine-con.md#enterkeytypedone) |
| [ENTER_KEY_TYPE_GO](arkts-ime-inputmethodengine-con.md#enterkeytypego) |
| [ENTER_KEY_TYPE_NEWLINE](arkts-ime-inputmethodengine-con.md#enterkeytypenewline) |
| [ENTER_KEY_TYPE_NEXT](arkts-ime-inputmethodengine-con.md#enterkeytypenext) |
| [ENTER_KEY_TYPE_PREVIOUS](arkts-ime-inputmethodengine-con.md#enterkeytypeprevious) |
| [ENTER_KEY_TYPE_SEARCH](arkts-ime-inputmethodengine-con.md#enterkeytypesearch) |
| [ENTER_KEY_TYPE_SEND](arkts-ime-inputmethodengine-con.md#enterkeytypesend) |
| [ENTER_KEY_TYPE_UNSPECIFIED](arkts-ime-inputmethodengine-con.md#enterkeytypeunspecified) |
| [FLAG_SELECTING](arkts-ime-inputmethodengine-con.md#flagselecting) |
| [FLAG_SINGLE_LINE](arkts-ime-inputmethodengine-con.md#flagsingleline) |
| [OPTION_ASCII](arkts-ime-inputmethodengine-con.md#optionascii) |
| [OPTION_AUTO_CAP_CHARACTERS](arkts-ime-inputmethodengine-con.md#optionautocapcharacters) |
| [OPTION_AUTO_CAP_SENTENCES](arkts-ime-inputmethodengine-con.md#optionautocapsentences) |
| [OPTION_AUTO_WORDS](arkts-ime-inputmethodengine-con.md#optionautowords) |
| [OPTION_MULTI_LINE](arkts-ime-inputmethodengine-con.md#optionmultiline) |
| [OPTION_NONE](arkts-ime-inputmethodengine-con.md#optionnone) |
| [OPTION_NO_FULLSCREEN](arkts-ime-inputmethodengine-con.md#optionnofullscreen) |
| [PATTERN_DATETIME](arkts-ime-inputmethodengine-con.md#patterndatetime) |
| [PATTERN_EMAIL](arkts-ime-inputmethodengine-con.md#patternemail) |
| [PATTERN_NEW_PASSWORD](arkts-ime-inputmethodengine-con.md#patternnewpassword) |
| [PATTERN_NULL](arkts-ime-inputmethodengine-con.md#patternnull) |
| [PATTERN_NUMBER](arkts-ime-inputmethodengine-con.md#patternnumber) |
| [PATTERN_NUMBER_DECIMAL](arkts-ime-inputmethodengine-con.md#patternnumberdecimal) |
| [PATTERN_ONE_TIME_CODE](arkts-ime-inputmethodengine-con.md#patternonetimecode) |
| [PATTERN_PASSWORD](arkts-ime-inputmethodengine-con.md#patternpassword) |
| [PATTERN_PASSWORD_NUMBER](arkts-ime-inputmethodengine-con.md#patternpasswordnumber) |
| [PATTERN_PASSWORD_SCREEN_LOCK](arkts-ime-inputmethodengine-con.md#patternpasswordscreenlock) |
| [PATTERN_PHONE](arkts-ime-inputmethodengine-con.md#patternphone) |
| [PATTERN_TEXT](arkts-ime-inputmethodengine-con.md#patterntext) |
| [PATTERN_URI](arkts-ime-inputmethodengine-con.md#patternuri) |
| [PATTERN_USER_NAME](arkts-ime-inputmethodengine-con.md#patternusername) |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT](arkts-ime-inputmethodengine-con.md#windowtypeinputmethodfloat) |
