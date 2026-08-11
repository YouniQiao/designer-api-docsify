# @ohos.inputMethod

The **inputMethod** module is oriented to common foreground applications (system applications such as Notes, Messaging, and Settings). It provides input method control and management capabilities, including displaying or hiding the soft keyboard, switching between input methods, and obtaining the list of all input methods.

**Since:** 6

<!--Device-unnamed-declare namespace inputMethod--><!--Device-unnamed-declare namespace inputMethod-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getController](arkts-ime-inputmethod-getcontroller-f.md#getcontroller) |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md#getcurrentinputmethod) |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md#getcurrentinputmethodsubtype) |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f.md#getdefaultinputmethod) |
| [getInputMethodController](arkts-ime-inputmethod-getinputmethodcontroller-f.md#getinputmethodcontroller) |
| [getInputMethodSetting](arkts-ime-inputmethod-getinputmethodsetting-f.md#getinputmethodsetting) |
| [getSetting](arkts-ime-inputmethod-getsetting-f.md#getsetting) |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md#getsysteminputmethodconfigability) |
| [offAttachmentDidFail](arkts-ime-inputmethod-offattachmentdidfail-f.md#offattachmentdidfail) |
| [onAttachmentDidFail](arkts-ime-inputmethod-onattachmentdidfail-f.md#onattachmentdidfail) |
| [setSimpleKeyboardEnabled](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md#setsimplekeyboardenabled) |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype) |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md#switchcurrentinputmethodandsubtype-1) |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype) |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md#switchcurrentinputmethodsubtype-1) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md#switchinputmethod-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md#getcurrentinputmethod-1) |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md#getcurrentinputmethodsubtype-1) |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md#getdefaultinputmethod-1) |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md#getsysteminputmethodconfigability-1) |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f-sys.md#switchinputmethod-2) |
| [switchInputMethodWithUserId](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md#switchinputmethodwithuserid) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) |
| [FunctionKey](arkts-ime-inputmethod-functionkey-i.md) |
| [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md) |
| [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) |
| [Movement](arkts-ime-inputmethod-movement-i.md) |
| [Range](arkts-ime-inputmethod-range-i.md) |
| [TextConfig](arkts-ime-inputmethod-textconfig-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md) |
| [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md) |
| [Direction](arkts-ime-inputmethod-direction-e.md) |
| [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) |
| [EnterKeyType](arkts-ime-inputmethod-enterkeytype-e.md) |
| [ExtendAction](arkts-ime-inputmethod-extendaction-e.md) |
| [KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md) |
| [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) |
| [TextInputType](arkts-ime-inputmethod-textinputtype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) |
<!--DelEnd-->

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md#max_type_num) |
