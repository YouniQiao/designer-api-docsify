# @ohos.inputMethod

**起始版本：** 23

<!--Device-unnamed-declare namespace inputMethod--><!--Device-unnamed-declare namespace inputMethod-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
import { InputMethodExtraConfig } from '@kit.IMEKit';
import { inputMethodSystemPanelManager } from '@kit.IMEKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getController](arkts-ime-inputmethod-getcontroller-f.md) |  |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f.md) |  |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f.md) |  |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f.md) |  |
| [getInputMethodController](arkts-ime-inputmethod-getinputmethodcontroller-f.md) |  |
| [getInputMethodSetting](arkts-ime-inputmethod-getinputmethodsetting-f.md) |  |
| [getSetting](arkts-ime-inputmethod-getsetting-f.md) |  |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f.md) |  |
| [offAttachmentDidFail](arkts-ime-inputmethod-offattachmentdidfail-f.md) |  |
| [onAttachmentDidFail](arkts-ime-inputmethod-onattachmentdidfail-f.md) |  |
| [setSimpleKeyboardEnabled](arkts-ime-inputmethod-setsimplekeyboardenabled-f.md) |  |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |  |
| [switchCurrentInputMethodAndSubtype](arkts-ime-inputmethod-switchcurrentinputmethodandsubtype-f.md) |  |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |  |
| [switchCurrentInputMethodSubtype](arkts-ime-inputmethod-switchcurrentinputmethodsubtype-f.md) |  |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md) |  |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f.md) |  |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getCurrentInputMethod](arkts-ime-inputmethod-getcurrentinputmethod-f-sys.md) |  |
| [getCurrentInputMethodSubtype](arkts-ime-inputmethod-getcurrentinputmethodsubtype-f-sys.md) |  |
| [getDefaultInputMethod](arkts-ime-inputmethod-getdefaultinputmethod-f-sys.md) |  |
| [getSystemInputMethodConfigAbility](arkts-ime-inputmethod-getsysteminputmethodconfigability-f-sys.md) |  |
| [switchInputMethod](arkts-ime-inputmethod-switchinputmethod-f-sys.md) |  |
| [switchInputMethodWithUserId](arkts-ime-inputmethod-switchinputmethodwithuserid-f-sys.md) |  |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |  |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) |  |
| [FunctionKey](arkts-ime-inputmethod-functionkey-i.md) |  |
| [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) |  |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i.md) |  |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |  |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |  |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md) |  |
| [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) |  |
| [Movement](arkts-ime-inputmethod-movement-i.md) |  |
| [Range](arkts-ime-inputmethod-range-i.md) |  |
| [TextConfig](arkts-ime-inputmethod-textconfig-i.md) |  |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [InputMethodController](arkts-ime-inputmethod-inputmethodcontroller-i-sys.md) |  |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i-sys.md) |  |
| [InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i-sys.md) |  |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md) |  |
| [CapitalizeMode](arkts-ime-inputmethod-capitalizemode-e.md) |  |
| [Direction](arkts-ime-inputmethod-direction-e.md) |  |
| [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) |  |
| [EnterKeyType](arkts-ime-inputmethod-enterkeytype-e.md) |  |
| [ExtendAction](arkts-ime-inputmethod-extendaction-e.md) |  |
| [KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md) |  |
| [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) |  |
| [TextInputType](arkts-ime-inputmethod-textinputtype-e.md) |  |

### 类型

| 名称 | 说明 |
| --- | --- |
| [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) |  |
| [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) |  |
| [ImeChangeCallback](arkts-ime-inputmethod-imechangecallback-t.md) |  |
| [OnMessageCallback](arkts-ime-inputmethod-onmessagecallback-t.md) |  |
| [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) |  |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) |  |
<!--DelEnd-->

### 常量

| 名称 | 说明 |
| --- | --- |
| [MAX_TYPE_NUM](arkts-ime-inputmethod-con.md#max_type_num) |  |

