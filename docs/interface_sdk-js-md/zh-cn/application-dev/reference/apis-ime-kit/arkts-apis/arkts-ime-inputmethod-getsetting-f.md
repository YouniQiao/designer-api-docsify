# getSetting

## 导入模块

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## getSetting

```TypeScript
function getSetting(): InputMethodSetting
```

获取客户端设置实例[InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md)。 <br> <br>含义/功能：获取输入法设置实例，用于查询输入法列表、订阅输入法变化事件、查询面板可见性等配置管理操作。 <br> <br>使用场景：当应用需要查询已安装/已激活输入法列表、订阅输入法切换事件、或显示输入法选择对话框时，必须先通过此接口获取InputMethodSetting实例。 <br> <br>使用后效果：返回一个InputMethodSetting实例，后续可通过该实例调用getInputMethods、listInputMethodSubtype、on('imeChange')等接口。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [InputMethodSetting](arkts-ime-inputmethod-inputmethodsetting-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800007](../errorcode-inputmethod-framework.md#12800007-输入法设置器异常) |

**示例**

```TypeScript
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```
