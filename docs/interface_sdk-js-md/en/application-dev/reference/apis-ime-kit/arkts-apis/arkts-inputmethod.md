# @ohos.inputMethod

@brief The **inputMethod** module is oriented to common foreground applications (third-party applications and system applications such as Notes, Messaging, and Settings). It provides input method control and management capabilities, including displaying or hiding the soft keyboard, switching between input methods, and obtaining the list of all input methods. <br> <br>   
> **NOTE：**&lt;br
&gt; 
> &lt;br
&gt; 
> The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Since:** 23

<!--Device-unnamed-declare namespace inputMethod--><!--Device-unnamed-declare namespace inputMethod-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getController](arkts-ime-inputmethod-getcontroller-f.md) | @brief Obtains an [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) instance. |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md) | @brief Obtains the current input method. This API returns the result synchronously. |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md) | @brief Obtains the current input method subtype. |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f.md) | @brief Obtains the default input method. |
| [getInputMethodController](arkts-ime-inputmethod-getinputmethodcontroller-f.md) | @brief Obtains an [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) instance. |
| [getInputMethodSetting](arkts-ime-inputmethod-getinputmethodsetting-f.md) | @brief Obtains an [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) instance. |
| [getSetting](arkts-ime-inputmethod-getsetting-f.md) | @brief Obtains an [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) instance. |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md) | @brief Obtains the information about the input method configuration page ability. |
| [offAttachmentDidFail](arkts-ime-inputmethod-offattachmentdidfail-f.md) | Unsubscribes from attachment failure events. This API uses an asynchronous callback to return the result. |
| [onAttachmentDidFail](arkts-ime-inputmethod-onattachmentdidfail-f.md) | @brief Subscribes to attachment failure events. This API uses an asynchronous callback to return the result. |
| [setSimpleKeyboardEnabled](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md) | @brief Enables or disables the simple keyboard. |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) | @brief Switches to a specified subtype of a specified input method. This API uses an asynchronous callback to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) | @brief Switches to a specified subtype of a specified input method. This API uses a promise to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) | @brief Switches to another subtype of this input method. This API uses an asynchronous callback to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT_IME_ABILITY** permission is required. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) | @brief Switches to another subtype of this input method. This API uses a promise to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT_IME_ABILITY** permission is required. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md) | @brief Switches to another input method. This API uses an asynchronous callback to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md) | @brief Switches to another input method. This API uses a promise to return the result. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission. &lt;br &gt;  > &lt;br &gt;  > - Since API version 11, this API can only be called by the current input method application. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md) | @brief Get the current input method of a specified user. |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md) | @brief Get the current input method subtype of a specified user. |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md) | @brief Get the default input method of a specified user. |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md) | @brief Get the system input method config ability of a specified user. |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f-sys.md) | @brief Switches to another input method. This API uses a promise to return the result. |
| [switchInputMethodWithUserId](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md) | @brief Switch input method and subtype of a specified user. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | @brief Defines additional options for binding an input method. |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | @brief Represents the cursor information. |
| [FunctionKey](arkts-ime-inputmethod-functionkey-i.md) | @brief Describes the type of the input method function key. |
| [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | @brief Describes the attributes of the edit box, including the text input type and Enter key function type. |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) | @brief In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance. |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | @brief Describes the input method application attributes. |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | @brief In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md) | @brief Describes the window information of the input method keyboard. |
| [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | @brief Represents a custom communication object. <br> <br>  > **NOTE：**&lt;br &gt;  > &lt;br &gt;  > You can register this object to receive custom communication data sent by the input method application. When the custom communication data is received, the [onMessage](arkts-ime-inputmethod-messagehandler-i.md#onmessage) callback in this object is triggered. &lt;br &gt;  > &lt;br &gt;  > This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback of the penultimate registered object is triggered. &lt;br &gt;  > &lt;br &gt;  > If this object is unregistered, its [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback will be triggered. |
| [Movement](arkts-ime-inputmethod-movement-i.md) | @brief Describes the direction in which the cursor moves when the text is selected. |
| [Range](arkts-ime-inputmethod-range-i.md) | @brief Describes the range of the selected text. |
| [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | @brief Describes the configuration of the edit box. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) | @brief In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance. |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) | @brief In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) | @brief Describes the window information of the input method keyboard. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md) | @brief Enumerates the reasons for attachment failure. |
| [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md) | @brief Enumerates the modes of capitalizing the first letter of a text. <br> \| Name\| Value\| Description\| \| -------- \| -- \| -------- \| \| NONE \| 0 \| The first letter is not capitalized.\| \| SENTENCES \| 1 \| The first letter of each sentence is capitalized.\| \| WORDS \| 2 \| The first letter of each word is capitalized.\| \| CHARACTERS \| 3 \| All letters are capitalized.\| |
| [Direction](arkts-ime-inputmethod-direction-e.md) | @brief Enumerates the directions of cursor movement of the input method. |
| [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | @brief Indicates whether the input method is enabled. |
| [EnterKeyType](arkts-ime-inputmethod-enterkeytype-e.md) | @brief Enumerates the function types represented by the Enter key of the input method. |
| [ExtendAction](arkts-ime-inputmethod-extendaction-e.md) | @brief Describes the type of the extended edit action on the text box. |
| [KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md) | @brief Enumerates the soft keyboard states of the input method. |
| [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | @brief Enumerates the reasons for requesting the keyboard. |
| [TextInputType](arkts-ime-inputmethod-textinputtype-e.md) | @brief Enumerates the text input types. |

### Types

| Name | Description |
| --- | --- |
| [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | @brief The callback of 'getLeftTextOfCursor' or 'getRightTextOfCursor' event. |
| [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | @brief The callback of 'getTextIndexAtCursor' event. |
| [ImeChangeCallback](arkts-ime-inputmethod-imechangecallback-t.md) | @brief The callback of 'imeChange' event. |
| [OnMessageCallback](arkts-ime-inputmethod-onmessagecallback-t.md) | @brief Callback function on receiving a custom message. |
| [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | @brief Callback triggered when the input method framework needs to display the text preview. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | The callback of the inputmethod change event which carries the user ID whose inputmethod is changed. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md#max_type_num) | @brief Keyboard max number. Max value is 128. |

