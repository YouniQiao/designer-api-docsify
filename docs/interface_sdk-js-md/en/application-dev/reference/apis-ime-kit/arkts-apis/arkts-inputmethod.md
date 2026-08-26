# @ohos.inputMethod(Input Method Framework)

###### Constant
 <br>
 <br>Provides the constants.
 <br>
 | Name| Type| Value| Description|
 | -------- | -------- | -------- | -------- |
| MAX_TYPE_NUM<sup>8+</sup> | number | 128 | Maximum number of supported input methods.|


**Since:** 6

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import inputMethod from '@kit.IMEKit';
import inputMethodEngine from '@kit.IMEKitEngine';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKitList';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit.Panel';
import { InputMethodExtraConfig } from '@kit.IMEKit.ExtraConfig';
import inputMethodSystemPanelManager from '@kit.IMEKitSystemPanelManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getController(Input Method Framework)](arkts-ime-inputmethod-getcontroller-f.md) | Obtains an [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) instance. |
| [getCurrentInputMethod(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethod-f.md) | Obtains the current input method. This API returns the result synchronously. |
| [getCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md) | Obtains the current input method subtype. |
| [getDefaultInputMethod(Input Method Framework)](arkts-ime-inputmethod-getdefaultinputmethod-f.md) | Obtains the default input method. |
| [getInputMethodController(Input Method Framework)](arkts-ime-inputmethod-getinputmethodcontroller-f.md) | Obtains an [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) instance. |
| [getInputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-getinputmethodsetting-f.md) | Obtains an [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) instance. |
| [getSetting(Input Method Framework)](arkts-ime-inputmethod-getsetting-f.md) | Obtains an [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) instance. |
| [getSystemInputMethodConfigAbility(Input Method Framework)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md) | Obtains the information about the input method configuration page ability. |
| [offAttachmentDidFail(Input Method Framework)](arkts-ime-inputmethod-offattachmentdidfail-f.md) | Unsubscribes from attachment failure events. This API uses an asynchronous callback to return the result. |
| [onAttachmentDidFail(Input Method Framework)](arkts-ime-inputmethod-onattachmentdidfail-f.md) | Subscribes to attachment failure events. This API uses an asynchronous callback to return the result. |
| [setSimpleKeyboardEnabled(Input Method Framework)](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md) | Enables or disables the simple keyboard. |
| [switchCurrentInputMethodAndSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) | Switches to a specified subtype of a specified input method. This API uses an asynchronous callback to return the result.  > **NOTE：**   >    > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodAndSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) | Switches to a specified subtype of a specified input method. This API uses a promise to return the result.  > **NOTE：**   >    > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) | Switches to another subtype of this input method. This API uses an asynchronous callback to return the result.  > **NOTE：**   >    > - In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT_IME_ABILITY** permission is required.   >    > - Since API version 11, this API can only be called by the current input method application. |
| [switchCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) | Switches to another subtype of this input method. This API uses a promise to return the result.  > **NOTE：**   >    > - In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT_IME_ABILITY** permission is required.   >    > - Since API version 11, this API can only be called by the current input method application. |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f.md) | Switches to another input method. This API uses an asynchronous callback to return the result.  > **NOTE：**   >    > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - Since API version 11, this API can only be called by the current input method application. |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f.md) | Switches to another input method. This API uses a promise to return the result.  > **NOTE：**   >    > - In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT_IME_ABILITY** permission.   >    > - Since API version 11, this API can only be called by the current input method application. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getCurrentInputMethod(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md) | Get the current input method of a specified user. |
| [getCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md) | Get the current input method subtype of a specified user. |
| [getDefaultInputMethod(Input Method Framework)](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md) | Get the default input method of a specified user. |
| [getSystemInputMethodConfigAbility(Input Method Framework)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md) | Get the system input method config ability of a specified user. |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f-sys.md) | Switches to another input method. This API uses a promise to return the result. |
| [switchInputMethodWithUserId(Input Method Framework)](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md) | Switch input method and subtype of a specified user. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AttachOptions(Input Method Framework)](arkts-ime-inputmethod-attachoptions-i.md) | Defines additional options for binding an input method. |
| [CursorInfo(Input Method Framework)](arkts-ime-inputmethod-cursorinfo-i.md) | Represents the cursor information. |
| [FunctionKey(Input Method Framework)](arkts-ime-inputmethod-functionkey-i.md) | Describes the type of the input method function key. |
| [InputAttribute(Input Method Framework)](arkts-ime-inputmethod-inputattribute-i.md) | Describes the attributes of the edit box, including the text input type and Enter key function type. |
| [InputMethodController(Input Method Framework)](arkts-ime-inputmethod-inputmethodcontroller-i.md) | In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance. |
| [InputMethodProperty(Input Method Framework)](arkts-ime-inputmethod-inputmethodproperty-i.md) | Describes the input method application attributes. |
| [InputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-inputmethodsetting-i.md) | In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo(Input Method Framework)](arkts-ime-inputmethod-inputwindowinfo-i.md) | Describes the window information of the input method keyboard. |
| [MessageHandler(Input Method Framework)](arkts-ime-inputmethod-messagehandler-i.md) | Represents a custom communication object.  > **NOTE：**   >    > You can register this object to receive custom communication data sent by the input method application. When the custom communication data is received, the [onMessage](arkts-ime-inputmethod-messagehandler-i.md#onmessage) callback in this object is triggered.   >    > This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback of the penultimate registered object is triggered.   >    > If this object is unregistered, its [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback will be triggered. |
| [Movement(Input Method Framework)](arkts-ime-inputmethod-movement-i.md) | Describes the direction in which the cursor moves when the text is selected. |
| [Range(Input Method Framework)](arkts-ime-inputmethod-range-i.md) | Describes the range of the selected text. |
| [TextConfig(Input Method Framework)](arkts-ime-inputmethod-textconfig-i.md) | Describes the configuration of the edit box. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [InputMethodController(Input Method Framework)](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) | In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance. |
| [InputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) | In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance. |
| [InputWindowInfo(Input Method Framework)](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) | Describes the window information of the input method keyboard. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AttachFailureReason(Input Method Framework)](arkts-ime-inputmethod-attachfailurereason-e.md) | Enumerates the reasons for attachment failure. |
| [CapitalizeMode(Input Method Framework)](arkts-ime-inputmethod-capitalizemode-e.md) | Enumerates the modes of capitalizing the first letter of a text.   \| Name\| Value\| Description\| \| -------- \| -- \| -------- \| \| NONE \| 0 \| The first letter is not capitalized.\| \| SENTENCES \| 1 \| The first letter of each sentence is capitalized.\| \| WORDS \| 2 \| The first letter of each word is capitalized.\| \| CHARACTERS \| 3 \| All letters are capitalized.\| |
| [Direction(Input Method Framework)](arkts-ime-inputmethod-direction-e.md) | Enumerates the directions of cursor movement of the input method. |
| [EnabledState(Input Method Framework)](arkts-ime-inputmethod-enabledstate-e.md) | Indicates whether the input method is enabled. |
| [EnterKeyType(Input Method Framework)](arkts-ime-inputmethod-enterkeytype-e.md) | Enumerates the function types represented by the Enter key of the input method. |
| [ExtendAction(Input Method Framework)](arkts-ime-inputmethod-extendaction-e.md) | Describes the type of the extended edit action on the text box. |
| [KeyboardStatus(Input Method Framework)](arkts-ime-inputmethod-keyboardstatus-e.md) | Enumerates the soft keyboard states of the input method. |
| [RequestKeyboardReason(Input Method Framework)](arkts-ime-inputmethod-requestkeyboardreason-e.md) | Enumerates the reasons for requesting the keyboard. |
| [TextInputType(Input Method Framework)](arkts-ime-inputmethod-textinputtype-e.md) | Enumerates the text input types. |

### Types

| Name | Description |
| --- | --- |
| [SetPreviewTextCallback(Input Method Framework)](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | Callback triggered when the input method framework needs to display the text preview. |

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [ImeChangeWithUserIdCallback(Input Method Framework)](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | The callback of the inputmethod change event which carries the user ID whose inputmethod is changed. |
<!--DelEnd-->

### Constants

| Name | Description |
| --- | --- |
| [MAX_TYPE_NUM(Input Method Framework)](arkts-ime-inputmethod-con.md#max_type_num) | Keyboard max number. Max value is 128. |
