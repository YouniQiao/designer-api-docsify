# InputMethodAbility

InputMethodAbility是输入法应用的核心能力对象，提供输入法生命周期管理、面板创建与销毁、事件订阅等功能。输入法应用通过  
[getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability)获取该实例。

下列API均需使用[getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getinputmethodability)获取到InputMethodAbility实例后，通过实例调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-interface InputMethodAbility--><!--Device-inputMethodEngine-interface InputMethodAbility-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void
```

创建输入法面板，仅支持输入法应用在  
[InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md)（输入法扩展能力）类中调用。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | 当前输入法应用上下文信息。 |
| info | [PanelInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes | 输入法面板信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Panel&gt; | Yes | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

class InputMethodExt extends InputMethodExtensionAbility {
    onCreate(want: Want): void {
        console.info(`onCreate, want: ${want.abilityName}`);
        if (!this.context) {
            inputMethodEngine.getInputMethodAbility()
            .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
                if (err) {
                console.error(`Failed to createPanel. Code is ${err.code}, message is ${err.message}`);
                return;
              }
                console.info('Succeed in creating panel.');
            })
        }
    }
}
```

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>
```

创建输入法面板，仅支持输入法应用在  
[InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md)类中调用。使用promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | 当前输入法应用上下文信息。 |
| info | [PanelInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes | 输入法面板信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Panel&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

class InputMethodExt extends InputMethodExtensionAbility {
    onCreate(want: Want): void {
        console.info(`onCreate, want: ${want.abilityName}`);
        if (this.context) {
            inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
                .then((panel: inputMethodEngine.Panel) => {
                console.info('Succeed in creating panel.');
            }).catch((err: BusinessError) => {
                console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
            })
        }
    }
}
```

## destroyPanel

```TypeScript
destroyPanel(panel: Panel, callback: AsyncCallback<void>): void
```

销毁输入法面板。需先通过 createPanel 创建面板后调用。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void--><!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | [Panel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | Yes | 要销毁的面板对象。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当输入法面板销毁成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
    if (err !== undefined) {
      console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Succeed in destroying panel.');
  })
}
```

## destroyPanel

```TypeScript
destroyPanel(panel: Panel): Promise<void>
```

销毁输入法面板。使用promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>--><!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | [Panel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | Yes | 要销毁的面板对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel).then(() => {
    console.info('Succeed in destroying panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
  });
}
```

## getSecurityMode

```TypeScript
getSecurityMode(): SecurityMode
```

获取输入法应用的当前安全模式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-InputMethodAbility-getSecurityMode(): SecurityMode--><!--Device-InputMethodAbility-getSecurityMode(): SecurityMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) | 安全模式。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800004 | not an input method application. |

## Examples

```TypeScript
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

## off('inputStart')

```TypeScript
off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

取消订阅输入法绑定成功事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, inputClient: InputClient) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

## off('inputStop')

```TypeScript
off(type: 'inputStop', callback: () => void): void
```

取消订阅停止输入法应用事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStop' | Yes | 设置监听类型，固定取值为'inputStop'。 |
| callback | () =&gt; void | Yes | 取消订阅的回调函数，用于取消特定的键盘显示/隐藏事件订阅。传入callback时取消指定回调的订阅，不传入时取消type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
  console.info('inputMethodAbility delete inputStop notification.');
});
```

## off('setCallingWindow')

```TypeScript
off(type: 'setCallingWindow', callback: (wid: number) => void): void
```

取消订阅设置调用窗口事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setCallingWindow' | Yes | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid: number) =&gt; void | Yes | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;- 'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;- 'keyboardHide'表示隐 藏输入法软键盘。 |
| callback | () =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;- 'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;- 'keyboardHide'表示隐 藏输入法软键盘。 |
| callback | () =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

## off('setSubtype')

```TypeScript
off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void
```

取消订阅设置输入法子类型事件。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setSubtype' | Yes | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: InputMethodSubtype) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
  console.info('InputMethodAbility delete setSubtype notification.');
});
```

## off('securityModeChange')

```TypeScript
off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void
```

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'securityModeChange' | Yes | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SecurityMode&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
  (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  };
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('securityModeChange', securityChangeCallback);
inputMethodAbility.off('securityModeChange', securityChangeCallback);
```

## off('privateCommand')

```TypeScript
off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void
```

取消订阅输入法私有数据事件。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateCommand' | Yes | 设置监听类型，固定取值为'privateCommand'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

## Examples

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

## off('callingDisplayDidChange')

```TypeScript
off(type: 'callingDisplayDidChange', callback?: Callback<number>): void
```

取消订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void--><!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
  console.info('InputMethodAbility delete calling display  notification.');
});
```

## off('discardTypingText')

```TypeScript
off(type: 'discardTypingText', callback?: Callback<void>): void
```

取消订阅编辑框应用发送\u201c清空候选词\u201d事件到输入法。使用callback异步回调。

**使用场景：** 编辑框应用需要通知输入法清空当前候选词列表时使用（如用户切换输入框、提交表单后等场景）。

**使用后效果：** 当编辑框应用发送清空候选词请求时触发回调，输入法应用应在回调中清空候选词列表和预输入文本。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void--><!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discardTypingText' | Yes | 设置监听类型，固定取值为'discardTypingText'。&lt;br/&gt; - 'discardTypingText'：表示取消订阅编辑框应用发送“清 空候选词”事件到输入法。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

## offCallingDisplayDidChange

```TypeScript
offCallingDisplayDidChange(callback?: Callback<int>): void
```

取消编辑框对应窗口所在屏幕ID变化。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offCallingDisplayDidChange(callback?: Callback<int>): void--><!--Device-InputMethodAbility-offCallingDisplayDidChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offDiscardTypingText

```TypeScript
offDiscardTypingText(callback?: Callback<void>): void
```

取消订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offDiscardTypingText(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offDiscardTypingText(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## offInputStart

```TypeScript
offInputStart(callback?: IMAInputStartCallback): void
```

取消订阅输入法绑定成功事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offInputStart(callback?: IMAInputStartCallback): void--><!--Device-InputMethodAbility-offInputStart(callback?: IMAInputStartCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## offInputStop

```TypeScript
offInputStop(callback: Callback<void>): void
```

取消订阅输入法输入停止（inputStop）事件，停止监听系统要求输入法终止输入流程的触发动作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offInputStop(callback: Callback<void>): void--><!--Device-InputMethodAbility-offInputStop(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 to terminate itself. |

## offKeyboardHide

```TypeScript
offKeyboardHide(callback?: Callback<void>): void
```

取消订阅输入法键盘隐藏（keyboardHide）事件，停止监听输入法键盘隐藏的触发动作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offKeyboardHide(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offKeyboardHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 回调函数。 |

## offKeyboardShow

```TypeScript
offKeyboardShow(callback?: Callback<void>): void
```

取消订阅输入法事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offKeyboardShow(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offKeyboardShow(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | 回调函数。 |

## offPrivateCommand

```TypeScript
offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void
```

取消订阅输入法私有数据事件。使用callback异步回调。该接口只能被系统预置输入法调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | No | 回调函数，返回向输入法应用发送的私有数据。 参数不填写时，取消订阅type对应的所有回调事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

## offSecurityModeChange

```TypeScript
offSecurityModeChange(callback?: Callback<SecurityMode>): void
```

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offSecurityModeChange(callback?: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-offSecurityModeChange(callback?: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SecurityMode&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## offSetCallingWindow

```TypeScript
offSetCallingWindow(callback: Callback<int>): void
```

取消订阅编辑框设置调用窗口 ID（setCallingWindow）事件，停止监听编辑框设置调用窗口标识的触发动作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offSetCallingWindow(callback: Callback<int>): void--><!--Device-InputMethodAbility-offSetCallingWindow(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## offSetSubtype

```TypeScript
offSetSubtype(callback?: Callback<InputMethodSubtype>): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-offSetSubtype(callback?: Callback<InputMethodSubtype>): void--><!--Device-InputMethodAbility-offSetSubtype(callback?: Callback<InputMethodSubtype>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 to switch subtype. |

## on('inputStart')

```TypeScript
on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

订阅输入法绑定成功事件。使用callback异步回调。

**使用场景：** 输入法应用需要在编辑框获得焦点并绑定输入法时，获取KeyboardController和InputClient实例以进行后续的键盘操作和文本交互。

**使用后效果：** 当编辑框绑定到输入法应用时，触发回调并返回KeyboardController和InputClient实例。输入法应用可在回调中创建面板、加载键盘页面、订阅KeyboardDelegate事件等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, inputClient: InputClient) =&gt; void | Yes | 回调函数，返回输入法操作相关实例。kbController为键盘控制器实例，用于控制键盘显示/隐藏；inputClient为输入客户端实例，用于与编辑框进行文本交 互。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
    });
```

## on('inputStop')

```TypeScript
on(type: 'inputStop', callback: () => void): void
```

订阅停止输入法应用事件。使用callback异步回调。

**使用场景：** 输入法应用需要在编辑框失去焦点或用户切换输入法时，执行清理操作（如隐藏面板、释放资源）。

**使用后效果：** 当输入法应用被停止绑定时触发回调。输入法应用应在回调中隐藏面板、取消事件订阅、释放InputClient相关资源。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStop' | Yes | 设置监听类型，固定取值为'inputStop'。 |
| callback | () =&gt; void | Yes | 回调函数，无返回参数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});
```

## on('setCallingWindow')

```TypeScript
on(type: 'setCallingWindow', callback: (wid: number) => void): void
```

订阅设置调用窗口事件。使用callback异步回调。

**使用场景：** 输入法应用需要在绑定应用的窗口发生变化时（如应用切换窗口、多窗口场景），调整面板位置或重新定位。

**使用后效果：** 当调用方窗口发生变化时触发回调，返回新的窗口ID。输入法应用可根据窗口ID调整面板位置。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setCallingWindow' | Yes | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid: number) =&gt; void | Yes | 回调函数，参数为调用方窗口的Id。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**使用场景：** 输入法应用需要在软键盘显示/隐藏时，执行相应的界面更新操作（如调整面板布局、更新候选词区域）。

**使用后效果：** 当软键盘显示请求触发时，'keyboardShow'回调被调用，输入法应用应在回调中调用panel.show()显示面板；当软键盘隐藏请求触发时，'keyboardHide'回调被调用，输入法应用应在回调中调用panel.hide()隐藏面板。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;- 'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;- 'keyboardHide'表示隐 藏输入法软键盘。 |
| callback | () =&gt; void | Yes | 回调函数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**使用场景：** 输入法应用需要在软键盘显示/隐藏时，执行相应的界面更新操作（如调整面板布局、更新候选词区域）。

**使用后效果：** 当软键盘显示请求触发时，'keyboardShow'回调被调用，输入法应用应在回调中调用panel.show()显示面板；当软键盘隐藏请求触发时，'keyboardHide'回调被调用，输入法应用应在回调中调用panel.hide()隐藏面板。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | 设置监听类型。&lt;br/&gt;- 'keyboardShow'表示显示输入法软键盘。&lt;br/&gt;- 'keyboardHide'表示隐 藏输入法软键盘。 |
| callback | () =&gt; void | Yes | 回调函数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

## on('setSubtype')

```TypeScript
on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void
```

订阅设置输入法子类型事件。使用callback异步回调。

**使用场景：** 输入法应用需要在子类型（如语言、输入模式）发生变化时，切换到对应的键盘布局或输入逻辑。

**使用后效果：** 当输入法子类型变化时触发回调，返回新的输入法子类型信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setSubtype' | Yes | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: InputMethodSubtype) =&gt; void | Yes | 回调函数，返回设置的输入法子类型（InputMethodSubtype，输入法子类型）。 |

## Examples

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
  console.info('InputMethodAbility setSubtype.');
});
```

## on('securityModeChange')

```TypeScript
on(type: 'securityModeChange', callback: Callback<SecurityMode>): void
```

订阅输入法安全模式改变类型事件。使用callback异步回调。

**使用场景：** 输入法应用需要在安全模式发生变化时（如编辑框切换到密码输入模式、隐私模式等），调整键盘行为（如禁止截图、切换到安全键盘布局等）。

**使用后效果：** 当安全模式变化时触发回调，返回当前的安全模式值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'securityModeChange' | Yes | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SecurityMode&gt; | Yes | 回调函数，返回当前输入法应用的安全模式。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  });
```

## on('privateCommand')

```TypeScript
on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void
```

订阅输入法私有数据事件。使用callback异步回调。

**使用场景：** 应用与输入法之间需要传递私有数据（如自定义命令、配置信息等）时使用。仅系统默认输入法应用可订阅此事件。

**使用后效果：** 当绑定应用向输入法发送私有数据时触发回调，返回私有数据记录。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateCommand' | Yes | 设置监听类型，固定取值为'privateCommand'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | Yes | 回调函数，返回向输入法应用发送的私有数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

## Examples

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

## on('callingDisplayDidChange')

```TypeScript
on(type: 'callingDisplayDidChange', callback: Callback<number>): void
```

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**使用场景：** 多屏幕设备场景下，编辑框在不同屏幕间切换时，输入法应用需根据新的屏幕ID调整面板位置和大小。

**使用后效果：** 当编辑框所在屏幕ID发生变化时触发回调，返回新的屏幕ID。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void--><!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | 回调函数，返回编辑框设置对应窗口屏幕ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | capability not supported. |

## Examples

```TypeScript
let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
  console.info(`display id: ${num}`);
}
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

## on('discardTypingText')

```TypeScript
on(type: 'discardTypingText', callback: Callback<void>): void
```

订阅编辑框应用发送\u201c清空候选词\u201d事件到输入法。使用callback异步回调。

**使用场景：** 编辑框应用需要通知输入法清空当前候选词列表时使用（如用户切换输入框、提交表单后等场景）。

**使用后效果：** 当编辑框应用发送清空候选词请求时触发回调，输入法应用应在回调中清空候选词列表和预输入文本。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void--><!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discardTypingText' | Yes | 设置监听类型，固定取值为'discardTypingText'。&lt;br/&gt; - 'discardTypingText'：表示订阅编辑框应用发送“清空候 选词”事件到输入法。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

## onCallingDisplayDidChange

```TypeScript
onCallingDisplayDidChange(callback: Callback<int>): void
```

订阅编辑框对应窗口所在屏幕ID变化。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onCallingDisplayDidChange(callback: Callback<int>): void--><!--Device-InputMethodAbility-onCallingDisplayDidChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 回调函数，返回编辑框设置对应窗口屏幕ID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | capability not supported. |

## onDiscardTypingText

```TypeScript
onDiscardTypingText(callback: Callback<void>): void
```

订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onDiscardTypingText(callback: Callback<void>): void--><!--Device-InputMethodAbility-onDiscardTypingText(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

## onInputStart

```TypeScript
onInputStart(callback: IMAInputStartCallback): void
```

订阅输入法绑定成功事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onInputStart(callback: IMAInputStartCallback): void--><!--Device-InputMethodAbility-onInputStart(callback: IMAInputStartCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | Yes | 回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。 |

## onInputStop

```TypeScript
onInputStop(callback: Callback<void>): void
```

订阅停止输入法应用事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onInputStop(callback: Callback<void>): void--><!--Device-InputMethodAbility-onInputStop(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 系统要求输入法终止输入流程时触发的回调函数，无入参，用于执行输入停止后的清理逻辑（如隐藏键盘、释放资源等）。 to terminate itself. |

## onKeyboardHide

```TypeScript
onKeyboardHide(callback: Callback<void>): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onKeyboardHide(callback: Callback<void>): void--><!--Device-InputMethodAbility-onKeyboardHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

## onKeyboardShow

```TypeScript
onKeyboardShow(callback: Callback<void>): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onKeyboardShow(callback: Callback<void>): void--><!--Device-InputMethodAbility-onKeyboardShow(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 回调函数。 |

## onPrivateCommand

```TypeScript
onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void
```

订阅输入法私有数据事件。使用callback异步回调。该接口只能被系统预置输入法调用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | Yes | 回调函数，返回向输入法应用发送的私有数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

## onSecurityModeChange

```TypeScript
onSecurityModeChange(callback: Callback<SecurityMode>): void
```

订阅输入法安全模式改变类型事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onSecurityModeChange(callback: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-onSecurityModeChange(callback: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SecurityMode&gt; | Yes | 回调函数，返回当前输入法应用的安全模式。 |

## onSetCallingWindow

```TypeScript
onSetCallingWindow(callback: Callback<int>): void
```

订阅设置调用窗口事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onSetCallingWindow(callback: Callback<int>): void--><!--Device-InputMethodAbility-onSetCallingWindow(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 回调函数，返回调用方窗口的Id。 |

## onSetSubtype

```TypeScript
onSetSubtype(callback: Callback<InputMethodSubtype>): void
```

订阅设置输入法子类型事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-InputMethodAbility-onSetSubtype(callback: Callback<InputMethodSubtype>): void--><!--Device-InputMethodAbility-onSetSubtype(callback: Callback<InputMethodSubtype>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | Yes | 回调函数，返回设置的输入法子类型。 to switch subtype. |

