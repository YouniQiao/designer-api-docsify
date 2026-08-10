# getInputMethodAbility

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility
```

获取输入法应用客户端实例[InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)（输入法能力对象），仅支持输入法应用调用。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | 输入法应用客户端。 |

## Examples

```TypeScript
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```


## getInputMethodAbility

```TypeScript
function getInputMethodAbility(): InputMethodAbility | null
```

获取输入法应用客户端实例[InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)（输入法能力对象），仅支持输入法应用调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null--><!--Device-inputMethodEngine-function getInputMethodAbility(): InputMethodAbility | null-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md) | 输入法应用客户端。 |

