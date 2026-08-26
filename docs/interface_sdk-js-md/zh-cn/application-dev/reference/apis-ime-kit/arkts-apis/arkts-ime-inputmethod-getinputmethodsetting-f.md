# getInputMethodSetting

## 导入模块

```TypeScript
import inputMethod from '@kit.IMEKit';
import inputMethodEngine from '@kit.IMEKitEngine';
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKitList';
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit.Panel';
import { InputMethodExtraConfig } from '@kit.IMEKit.ExtraConfig';
import inputMethodSystemPanelManager from '@kit.IMEKitSystemPanelManager';
```

## getInputMethodSetting

```TypeScript
function getInputMethodSetting(): InputMethodSetting
```

获取客户端设置实例[InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getSetting](arkts-ime-inputmethod-getsetting-f.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) | 返回当前客户端设置实例。 |

**示例**

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();
```
