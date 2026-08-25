# @ohos.inputMethod(Input Method Framework)

###### Constant
 <br>
 <br>Provides the constants.
 <br>
| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | [Value](../../apis-arkdata/arkts-apis/arkts-arkdata-distributeddata-value-i.md) |
| -------- | -------- | -------- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md)<sup>8+</sup> | number | 128 |


**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getController(Input Method Framework)](arkts-ime-inputmethod-getcontroller-f.md) |
| [getCurrentInputMethod(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethod-f.md) |
| [getCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md) |
| [getDefaultInputMethod(Input Method Framework)](arkts-ime-inputmethod-getdefaultinputmethod-f.md) |
| [getInputMethodController(Input Method Framework)](arkts-ime-inputmethod-getinputmethodcontroller-f.md) |
| [getInputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-getinputmethodsetting-f.md) |
| [getSetting(Input Method Framework)](arkts-ime-inputmethod-getsetting-f.md) |
| [getSystemInputMethodConfigAbility(Input Method Framework)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md) |
| [offAttachmentDidFail(Input Method Framework)](arkts-ime-inputmethod-offattachmentdidfail-f.md) |
| [onAttachmentDidFail(Input Method Framework)](arkts-ime-inputmethod-onattachmentdidfail-f.md) |
| [setSimpleKeyboardEnabled(Input Method Framework)](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md) |
| [switchCurrentInputMethodAndSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |
| [switchCurrentInputMethodAndSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |
| [switchCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |
| [switchCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f.md) |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCurrentInputMethod(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md) |
| [getCurrentInputMethodSubtype(Input Method Framework)](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md) |
| [getDefaultInputMethod(Input Method Framework)](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md) |
| [getSystemInputMethodConfigAbility(Input Method Framework)](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md) |
| [switchInputMethod(Input Method Framework)](arkts-ime-inputmethod-switchinputmethod-f-sys.md) |
| [switchInputMethodWithUserId(Input Method Framework)](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachOptions(Input Method Framework)](arkts-ime-inputmethod-attachoptions-i.md) |
| [CursorInfo(Input Method Framework)](arkts-ime-inputmethod-cursorinfo-i.md) |
| [FunctionKey(Input Method Framework)](arkts-ime-inputmethod-functionkey-i.md) |
| [InputAttribute(Input Method Framework)](arkts-ime-inputmethod-inputattribute-i.md) |
| [InputMethodController(Input Method Framework)](arkts-ime-inputmethod-inputmethodcontroller-i.md) |
| [InputMethodProperty(Input Method Framework)](arkts-ime-inputmethod-inputmethodproperty-i.md) |
| [InputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-inputmethodsetting-i.md) |
| [InputWindowInfo(Input Method Framework)](arkts-ime-inputmethod-inputwindowinfo-i.md) |
| [MessageHandler(Input Method Framework)](arkts-ime-inputmethod-messagehandler-i.md) |
| [Movement(Input Method Framework)](arkts-ime-inputmethod-movement-i.md) |
| [Range(Input Method Framework)](arkts-ime-inputmethod-range-i.md) |
| [TextConfig(Input Method Framework)](arkts-ime-inputmethod-textconfig-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InputMethodController(Input Method Framework)](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) |
| [InputMethodSetting(Input Method Framework)](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) |
| [InputWindowInfo(Input Method Framework)](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachFailureReason(Input Method Framework)](arkts-ime-inputmethod-attachfailurereason-e.md) |
| [CapitalizeMode(Input Method Framework)](arkts-ime-inputmethod-capitalizemode-e.md) | Enumerates the modes of capitalizing the first letter of a text.<br> \ | Name\| Value\| Description\| \| -------- \| -- \| -------- \| \| NONE \| 0 \| The first letter is not capitalized.\| \| SENTENCES \| 1 \| The first letter of each sentence is capitalized.\| \| WORDS \| 2 \| The first letter of each word is capitalized.\| \| CHARACTERS \| 3 \| All letters are capitalized.\|
| [Direction(Input Method Framework)](arkts-ime-inputmethod-direction-e.md) |
| [EnabledState(Input Method Framework)](arkts-ime-inputmethod-enabledstate-e.md) |
| [EnterKeyType(Input Method Framework)](arkts-ime-inputmethod-enterkeytype-e.md) |
| [ExtendAction(Input Method Framework)](arkts-ime-inputmethod-extendaction-e.md) |
| [KeyboardStatus(Input Method Framework)](arkts-ime-inputmethod-keyboardstatus-e.md) |
| [RequestKeyboardReason(Input Method Framework)](arkts-ime-inputmethod-requestkeyboardreason-e.md) |
| [TextInputType(Input Method Framework)](arkts-ime-inputmethod-textinputtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GetTextCallback(Input Method Framework)](arkts-ime-inputmethod-gettextcallback-t.md) |
| [GetTextIndexAtCursorCallback(Input Method Framework)](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) |
| [ImeChangeCallback(Input Method Framework)](arkts-ime-inputmethod-imechangecallback-t.md) |
| [OnMessageCallback(Input Method Framework)](arkts-ime-inputmethod-onmessagecallback-t.md) |
| [SetPreviewTextCallback(Input Method Framework)](arkts-ime-inputmethod-setpreviewtextcallback-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImeChangeWithUserIdCallback(Input Method Framework)](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_TYPE_NUM(Input Method Framework)](arkts-ime-inputmethod-con.md#max_type_num) |
