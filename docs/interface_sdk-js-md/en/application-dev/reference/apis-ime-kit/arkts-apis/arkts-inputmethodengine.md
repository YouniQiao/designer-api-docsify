# @ohos.inputMethodEngine

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace inputMethodEngine--><!--Device-unnamed-declare namespace inputMethodEngine-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'inputMethodEngine';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createKeyboardDelegate](arkts-ime-inputmethodengine-createkeyboarddelegate-f.md#createKeyboardDelegate) | Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md#KeyboardDelegate) instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more. |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) | Obtains an [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md#InputMethodAbility) instance for the input method. This API can be called only by an input method. The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event, create/ destroy an input method panel, and the like. |
| [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) | Get InputMethodAbility object to subscribe events about IME. |
| [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getInputMethodEngine) | Obtains an [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md#InputMethodEngine) instance for the input method. The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event. |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) | Obtains a [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md#KeyboardDelegate) instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more. |
| [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) | Get KeyboardDelegate object to subscribe key event or events about editor. |

### Interfaces

| Name | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethodengine-attachoptions-i.md) | Defines additional options for binding an input method. |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) | In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | Indicates the size of the enhanced input method panel, including the custom avoid area and touch area. |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i.md) | Describes the immersive effect. |
| [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | You must first use on('inputStart') to obtain a **InputClient** instance, and then use this instance to call the following APIs. |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | In the following API examples, you must first use [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance. |
| [InputMethodEngine](arkts-ime-inputmethodengine-inputmethodengine-i.md) | In the following API examples, you must first use [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md#getInputMethodEngine) to obtain an **InputMethodEngine** instance, and then call the APIs using the obtained instance. |
| [KeyEvent](arkts-ime-inputmethodengine-keyevent-i.md) | In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | Represents the keyboard area on the panel. |
| [KeyboardController](arkts-ime-inputmethodengine-keyboardcontroller-i.md) | In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [KeyboardDelegate](arkts-ime-inputmethodengine-keyboarddelegate-i.md) | In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md) | Represents a custom communication object. > **NOTE：**> > You can register this object to receive custom communication data sent by the edit box application attached to > the input method application. When the custom communication data is received, the > [onMessage](arkts-ime-inputmethodengine-messagehandler-i.md#onMessage) callback in > this object is triggered. > > This object is globally unique. After multiple registrations, only the last registered object is valid and > retained, and the [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onTerminated) callback of the > penultimate registered object is triggered. > > If this object is unregistered, its [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onTerminated) > callback will be triggered. |
| [Movement](arkts-ime-inputmethodengine-movement-i.md) | Describes the direction in which the cursor moves when the text is selected. |
| [Panel](arkts-ime-inputmethodengine-panel-i.md) | In the following API examples, you must first use [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createPanel) to obtain a **Panel** instance, and then call the APIs using the obtained instance. |
| [PanelInfo](arkts-ime-inputmethodengine-panelinfo-i.md) | Describes the attributes of the input method panel. |
| [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | Represents the size of the input method panel. |
| [Range](arkts-ime-inputmethodengine-range-i.md) | Describes the range of the selected text. |
| [SystemPanelInsets](arkts-ime-inputmethodengine-systempanelinsets-i.md) | Defines the offset area between the input method soft keyboard and the system panel. |
| [TextInputClient](arkts-ime-inputmethodengine-textinputclient-i.md) | In the following API examples, you must first use on('inputStart') to obtain a **TextInputClient** instance, and then call the APIs using the obtained instance. |
| [WindowInfo](arkts-ime-inputmethodengine-windowinfo-i.md) | Represents window information. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i-sys.md) | In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getKeyboardDelegate) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance. |
| [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i-sys.md) | Describes the immersive effect. |
| [Panel](arkts-ime-inputmethodengine-panel-i-sys.md) | In the following API examples, you must first use [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createPanel) to obtain a **Panel** instance, and then call the APIs using the obtained instance. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CapitalizeMode](arkts-ime-inputmethodengine-capitalizemode-e.md) | Enumerates the modes of capitalizing the first letter of a text. |
| [Direction](arkts-ime-inputmethodengine-direction-e.md) | Enumerates the directions of cursor movement of the input method. |
| [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Describes the type of the extended edit action on the text box. |
| [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md) | Enumerates the gradient modes of the input method. |
| [ImmersiveMode](arkts-ime-inputmethodengine-immersivemode-e.md) | Enumerates the immersive modes of the input method. |
| [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | Enumerates the state types of the input method panel. |
| [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) | Enumerates the types of the input method panel. |
| [RequestKeyboardReason](arkts-ime-inputmethodengine-requestkeyboardreason-e.md) | Enumerates the reasons for requesting keyboard input. |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) | Describes the security mode. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [FluidLightMode](arkts-ime-inputmethodengine-fluidlightmode-e-sys.md) | Enumerates the fluid light modes of the input method. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md) | Defines the private data type, which varies depending on its function. |
| [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | The callback of 'cursorContextChange' event. |
| [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | The callback of 'inputStart' event. |
| [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | The callback of 'keyEvent' event. |
| [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | The callback of 'keyDown' or 'keyUp' event. |
| [OnMessageCallback](arkts-ime-inputmethodengine-onmessagecallback-t.md) | Callback function on receiving a custom message. |
| [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | The callback of 'selectionChange' event. |
| [SizeChangeCallback](arkts-ime-inputmethodengine-sizechangecallback-t.md) | Callback triggered when the size of the input method panel changes. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | Callback triggered when the size of the input method panel changes. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [CURSOR_DOWN](arkts-ime-inputmethodengine-con.md#CURSOR_DOWN) | The caret moves downward. |
| [CURSOR_LEFT](arkts-ime-inputmethodengine-con.md#CURSOR_LEFT) | The caret moves leftward. |
| [CURSOR_RIGHT](arkts-ime-inputmethodengine-con.md#CURSOR_RIGHT) | The caret moves rightward. |
| [CURSOR_UP](arkts-ime-inputmethodengine-con.md#CURSOR_UP) | The caret moves upward. |
| [DISPLAY_MODE_FULL](arkts-ime-inputmethodengine-con.md#DISPLAY_MODE_FULL) | The edit box is displayed in full screen. |
| [DISPLAY_MODE_PART](arkts-ime-inputmethodengine-con.md#DISPLAY_MODE_PART) | The edit box is displayed in half-screen mode. |
| [ENTER_KEY_TYPE_DONE](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_DONE) | Key that indicates that a task or input is complete. |
| [ENTER_KEY_TYPE_GO](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_GO) | Key that executes a command or navigates to a specific location. |
| [ENTER_KEY_TYPE_NEWLINE](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_NEWLINE) | Key that inserts a new line. |
| [ENTER_KEY_TYPE_NEXT](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_NEXT) | Key that moves the focus to the next item in a sequence. |
| [ENTER_KEY_TYPE_PREVIOUS](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_PREVIOUS) | Key that moves the focus to the previous item in a sequence. |
| [ENTER_KEY_TYPE_SEARCH](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_SEARCH) | Key that initiates a search operation. |
| [ENTER_KEY_TYPE_SEND](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_SEND) | Key that sends the text to its target. |
| [ENTER_KEY_TYPE_UNSPECIFIED](arkts-ime-inputmethodengine-con.md#ENTER_KEY_TYPE_UNSPECIFIED) | No function is specified for the key. |
| [FLAG_SELECTING](arkts-ime-inputmethodengine-con.md#FLAG_SELECTING) | The edit box is being selected. |
| [FLAG_SINGLE_LINE](arkts-ime-inputmethodengine-con.md#FLAG_SINGLE_LINE) | The edit box allows only single-line input. |
| [OPTION_ASCII](arkts-ime-inputmethodengine-con.md#OPTION_ASCII) | ASCII values are allowed. |
| [OPTION_AUTO_CAP_CHARACTERS](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_CAP_CHARACTERS) | Characters are allowed. |
| [OPTION_AUTO_CAP_SENTENCES](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_CAP_SENTENCES) | Sentences are allowed. |
| [OPTION_AUTO_WORDS](arkts-ime-inputmethodengine-con.md#OPTION_AUTO_WORDS) | Words are allowed. |
| [OPTION_MULTI_LINE](arkts-ime-inputmethodengine-con.md#OPTION_MULTI_LINE) | Multiple lines are allowed. |
| [OPTION_NONE](arkts-ime-inputmethodengine-con.md#OPTION_NONE) | No input attribute is specified. |
| [OPTION_NO_FULLSCREEN](arkts-ime-inputmethodengine-con.md#OPTION_NO_FULLSCREEN) | Half-screen style. |
| [PATTERN_DATETIME](arkts-ime-inputmethodengine-con.md#PATTERN_DATETIME) | Date edit box. |
| [PATTERN_EMAIL](arkts-ime-inputmethodengine-con.md#PATTERN_EMAIL) | Email edit box. |
| [PATTERN_NEW_PASSWORD](arkts-ime-inputmethodengine-con.md#PATTERN_NEW_PASSWORD) | New password edit box. The value is fixed at 11. |
| [PATTERN_NULL](arkts-ime-inputmethodengine-con.md#PATTERN_NULL) | Any type of edit box. |
| [PATTERN_NUMBER](arkts-ime-inputmethodengine-con.md#PATTERN_NUMBER) | Number edit box. |
| [PATTERN_NUMBER_DECIMAL](arkts-ime-inputmethodengine-con.md#PATTERN_NUMBER_DECIMAL) | Edit box for numbers with decimal points. The value is fixed at 12. |
| [PATTERN_ONE_TIME_CODE](arkts-ime-inputmethodengine-con.md#PATTERN_ONE_TIME_CODE) | Verification code edit box. The value is fixed at 13. |
| [PATTERN_PASSWORD](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD) | Password edit box. |
| [PATTERN_PASSWORD_NUMBER](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD_NUMBER) | Numeric password edit box. |
| [PATTERN_PASSWORD_SCREEN_LOCK](arkts-ime-inputmethodengine-con.md#PATTERN_PASSWORD_SCREEN_LOCK) | Screen lock password edit box. |
| [PATTERN_PHONE](arkts-ime-inputmethodengine-con.md#PATTERN_PHONE) | Phone number edit box. |
| [PATTERN_TEXT](arkts-ime-inputmethodengine-con.md#PATTERN_TEXT) | Text edit box. |
| [PATTERN_URI](arkts-ime-inputmethodengine-con.md#PATTERN_URI) | URI edit box. |
| [PATTERN_USER_NAME](arkts-ime-inputmethodengine-con.md#PATTERN_USER_NAME) | User name edit box. The value is fixed at 10. |
| [WINDOW_TYPE_INPUT_METHOD_FLOAT](arkts-ime-inputmethodengine-con.md#WINDOW_TYPE_INPUT_METHOD_FLOAT) | The input method is displayed in a floating window. |

