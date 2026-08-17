# @ohos.inputMethod

The **inputMethod** module is oriented to common foreground applications (system applications such as Notes, Messaging, and Settings). It provides input method control and management capabilities, including displaying or hiding the soft keyboard, switching between input methods, and obtaining the list of all input methods.

**Since:** 23

<!--Device-unnamed-declare namespace inputMethod--><!--Device-unnamed-declare namespace inputMethod-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'inputMethod';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller) | Input method controller |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod) | Get current input method |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md#getcurrentinputmethodsubtype) | Get the current input method subtype |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f.md#getdefaultinputmethod) | Get default input method |
| [getInputMethodController](arkts-ime-inputmethod-getinputmethodcontroller-f.md#getinputmethodcontroller) | Input method controller |
| [getInputMethodSetting](arkts-ime-inputmethod-getinputmethodsetting-f.md#getinputmethodsetting) | Input method setting |
| [getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting) | Input method setting |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md#getsysteminputmethodconfigability) | Get system input method config ability |
| [offAttachmentDidFail](arkts-ime-inputmethod-offattachmentdidfail-f.md#offattachmentdidfail) | Unsubscribe the attachment failure event. |
| [onAttachmentDidFail](arkts-ime-inputmethod-onattachmentdidfail-f.md#onattachmentdidfail) | Subscribe the attachment failure event. |
| [setSimpleKeyboardEnabled](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md#setsimplekeyboardenabled) | Set simple keyboard mode. |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype) | Switch input method and subtype. The caller must be the current inputmethod. |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype) | Switch input method and subtype. The caller must be the current inputmethod. |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype) | Switch current input method subtype. The caller must be the current inputmethod. |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype) | Switch current input method subtype. The caller must be the current inputmethod. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod) | Switch input method. The caller must be the current inputmethod. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod) | Switch input method. The caller must be the current inputmethod. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md#getcurrentinputmethod-system-api) | Get the current input method of a specified user. |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md#getcurrentinputmethodsubtype-system-api) | Get the current input method subtype of a specified user. |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md#getdefaultinputmethod-system-api) | Get the default input method of a specified user. |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md#getsysteminputmethodconfigability-system-api) | Get the system input method config ability of a specified user. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f-sys.md#switchinputmethod-system-api) | Switches to another input method. This API uses a promise to return the result. |
| [switchInputMethodWithUserId](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md#switchinputmethodwithuserid) | Switch input method and subtype of a specified user. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | Attach options. |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | Information of Cursor. |
| [FunctionKey](arkts-ime-inputmethod-functionkey-i.md) | FunctionKey of Input. |
| [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | Attribute of Input. |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | A control class that encapsulates APIs for input method management, which can only be invoked after an **InputMethodController** instance is obtained via [getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller). |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | input method property |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md) | Information of input window. |
| [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | &lt;p&gt;Custom message handler.&lt;/p&gt; &lt;p&gt;Implement this interface to respond to custom messages.&lt;/p&gt; |
| [Movement](arkts-ime-inputmethod-movement-i.md) | Movement of cursor. |
| [Range](arkts-ime-inputmethod-range-i.md) | Range of selected text. |
| [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Config of editor. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) | A control class that encapsulates APIs for input method management, which can only be invoked after an **InputMethodController** instance is obtained via [getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller). |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) | In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) | Information of input window. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md) | Enumerates the specific reasons for attachment failure |
| [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md) | Enumerates the capitalization mode. |
| [Direction](arkts-ime-inputmethod-direction-e.md) | Enumerates the moving direction of cursor |
| [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | Enumerates the enabled state. |
| [EnterKeyType](arkts-ime-inputmethod-enterkeytype-e.md) | Enumerates the enter key type. |
| [ExtendAction](arkts-ime-inputmethod-extendaction-e.md) | Enumerates the extend action. |
| [KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md) | Enumerates the keyboard status. |
| [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | requestKeyboardReason of input click |
| [TextInputType](arkts-ime-inputmethod-textinputtype-e.md) | Enumerates the text input type. |

### Types

| Name | Description |
| --- | --- |
| [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | The callback of 'getLeftTextOfCursor' or 'getRightTextOfCursor' event. |
| [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | The callback of 'getTextIndexAtCursor' event. |
| [ImeChangeCallback](arkts-ime-inputmethod-imechangecallback-t.md) | The callback of 'imeChange' event. |
| [OnMessageCallback](arkts-ime-inputmethod-onmessagecallback-t.md) | Callback function on receiving a custom message. |
| [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | The callback of 'setPreviewText' event. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | The callback of the inputmethod change event which carries the user ID whose inputmethod is changed. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md#maxtypenum) | Keyboard max number. Max value is 128. |

