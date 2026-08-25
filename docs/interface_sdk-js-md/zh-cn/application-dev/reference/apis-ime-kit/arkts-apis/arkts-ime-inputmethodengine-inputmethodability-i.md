# InputMethodAbility

InputMethodAbility是输入法应用的核心能力对象，提供输入法生命周期管理、面板创建与销毁、事件订阅等功能。输入法应用通过 [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md)获取该实例。 <br> <br>核心功能概述： <br> <br>- 生命周期事件订阅：通过on('inputStart')订阅输入法绑定事件获取[KeyboardController](arkts-ime-inputmethodengine-keyboardcontroller-i.md)和 [InputClient](arkts-ime-inputmethodengine-inputclient-i.md)实例，通过on('inputStop')订阅输入法解绑事件，通过on('keyboardShow'|'keyboardHide') 订阅软键盘显示/隐藏事件。 <br>- 面板管理：通过 [createPanel](#createpanel) 创建输入法面板，通过 [destroyPanel](#destroypanel) 销毁面板。createPanel与destroyPanel需配对调用，防止资源泄漏。 <br>- 子类型与安全模式：通过on('setSubtype')订阅输入法子类型变化事件，通过on('securityModeChange')订阅安全模式变化事件，通过 [getSecurityMode](#getsecuritymode)获取当前安全模式。 <br>- 私有通信：通过on('privateCommand')订阅应用私有数据事件，用于输入法应用与绑定应用之间的私有数据交互。 <br>- 屏幕与窗口信息：通过on('setCallingWindow')订阅调用方窗口变化事件，通过on('callingDisplayDidChange')订阅屏幕ID变化事件，通过on('discardTypingText')订阅 丢弃文本事件。 <br> <br>典型调用顺序： <br> <br>1. 输入法应用在[InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md)的onCreate生命周期中调用getInputMethodAbility()获取实例。 <br>2. 订阅on('inputStart')事件，在回调中获取KeyboardController和InputClient实例。 <br>3. 在on('inputStart')回调中调用createPanel()创建面板，并调用panel.setUiContent()加载键盘页面。 <br>4. 订阅on('keyboardShow'|'keyboardHide')事件，在回调中调用panel.show()/panel.hide()显示/隐藏面板。 <br>5. 在InputMethodExtensionAbility的onDestroy生命周期中调用destroyPanel()销毁面板，取消所有事件订阅。下列API均需使用[getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md)获取到InputMethodAbility实例后，通过实例调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void
```

创建输入法面板，仅支持输入法应用在 [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md)（输入法扩展能力）类中调用。使 用callback异步回调。 <br> <br>配对调用： <br> <br>- 调用createPanel()创建面板后，必须在使用完毕后调用 [destroyPanel](#destroypanel) 销毁面板以释放资源。 <br>- 未调用destroyPanel()会导致面板资源泄漏，影响系统资源使用。 <br>- 单个输入法应用仅允许创建一个软键盘类型和一个状态栏类型的面板。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 单个输入法应用仅允许创建一个[软键盘类型](arkts-ime-inputmethodengine-paneltype-e.md)和一个[状态栏类型](arkts-ime-inputmethodengine-paneltype-e.md)的面板。 &lt;br
&gt; 
> &lt;br
&gt; 
> 输入法面板不支持创建子窗口。例如：不支持使用window.createWindow[设置应用子窗口](../../../windowmanager/application-window-fa.md#设置应用子窗口)、 &lt;br
&gt; 
> bindContextMenu &lt;br
&gt; 
> 、CustomDialog等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如 &lt;br
&gt; 
> 弹出框、 &lt;br
&gt; 
> bindMenu或设置 &lt;br
&gt; 
> showInSubwindow为false。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| info | [PanelInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Panel&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800004](../errorcode-inputmethod-framework.md#12800004-不是输入法应用) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

// 创建面板信息，设置面板类型为软键盘，状态为固定态
let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

class InputMethodExt extends InputMethodExtensionAbility {
    onCreate(want: Want): void {
        console.info(`onCreate, want: ${want.abilityName}`);
        // context为InputMethodExtensionAbility类提供的上下文对象，无需额外获取
        if (this.context) {
            // 创建输入法面板
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

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

// 创建面板信息，设置面板类型为软键盘，状态为固定态
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

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>
```

创建输入法面板，仅支持输入法应用在 [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md)类中调用。使用promise异 步回调。 <br> <br>   
> **说明：** &lt;br
&gt; 
> &lt;br
&gt; 
> 单个输入法应用仅允许创建一个[软键盘类型](arkts-ime-inputmethodengine-paneltype-e.md)和一个[状态栏类型](arkts-ime-inputmethodengine-paneltype-e.md)的面板。 &lt;br
&gt; 
> &lt;br
&gt; 
> 输入法面板不支持创建子窗口。例如：不支持使用window.createWindow[设置应用子窗口](../../../windowmanager/application-window-fa.md#设置应用子窗口)、 &lt;br
&gt; 
> bindContextMenu &lt;br
&gt; 
> 、CustomDialog等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如 &lt;br
&gt; 
> 弹出框、 &lt;br
&gt; 
> bindMenu或设置 &lt;br
&gt; 
> showInSubwindow为false。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| info | [PanelInfo](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Panel & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800004](../errorcode-inputmethod-framework.md#12800004-不是输入法应用) |

**示例**

参见 [createPanel](#createpanel)

## destroyPanel

```TypeScript
destroyPanel(panel: Panel, callback: AsyncCallback<void>): void
```

销毁输入法面板。需先通过 [createPanel](#createpanel) 创建面板后调用。使用callback异步回调。 <br> <br>配对调用： <br> <br>- 必须与 [createPanel](#createpanel) 方法配合使用，用于销毁由createPanel()创建的输入法面板。 <br>- 销毁的面板必须是已成功创建的面板对象。 <br>- 未正确销毁面板会导致资源泄漏，建议在面板使用完毕后及时调用destroyPanel()释放资源。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| panel | [Panel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 创建面板信息，设置面板类型为软键盘，状态为固定态
let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

// 在InputMethodExtensionAbility类中使用
let inputPanel: inputMethodEngine.Panel | undefined = undefined;
inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
  if (err) {
    console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  inputPanel = panel;
  console.info('Succeed in creating panel.');
  // 创建成功后再销毁
  if (inputPanel) {
    inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('Succeed in destroying panel.');
    });
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 创建面板信息，设置面板类型为软键盘，状态为固定态
let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
// context为InputMethodExtensionAbility类提供的上下文对象，无需额外获取
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

## destroyPanel

```TypeScript
destroyPanel(panel: Panel): Promise<void>
```

销毁输入法面板。使用promise异步回调。 <br> <br>配对调用： <br> <br>- 必须与 [createPanel](#createpanel) 方法配合使用，用于销毁由createPanel()创建的输入法面板。 <br>- 销毁的面板必须是已成功创建的面板对象。 <br>- 未正确销毁面板会导致资源泄漏，建议在面板使用完毕后及时调用destroyPanel()释放资源。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| panel | [Panel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [destroyPanel](#destroypanel)

## getSecurityMode

```TypeScript
getSecurityMode(): SecurityMode
```

获取输入法应用的当前安全模式。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800004](../errorcode-inputmethod-framework.md#12800004-不是输入法应用) |

**示例**

```TypeScript
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

## off('inputStart')

```TypeScript
off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

取消订阅输入法绑定成功事件。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStart' | 是 |
| callback | (kbController: KeyboardController, inputClient: InputClient) = & gt; void | 否 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

## off('inputStop')

```TypeScript
off(type: 'inputStop', callback: () => void): void
```

取消订阅停止输入法应用事件。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStop' | 是 |
| callback | () = & gt; void | 是 |

**示例**

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

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setCallingWindow' | 是 |
| callback | (wid: number) = & gt; void | 是 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (windowId: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 否 |

**示例**

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

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 否 |

**示例**

参见 off

## off('setSubtype')

```TypeScript
off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void
```

取消订阅设置输入法子类型事件。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setSubtype' | 是 |
| callback | (inputMethodSubtype: InputMethodSubtype) = & gt; void | 否 |

**示例**

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'securityModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | 否 |

**示例**

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

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'privateCommand' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

**示例**

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (const key in record) {
      console.info(`private command key: ${key}, value: ${record[key]}`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

## off('callingDisplayDidChange')

```TypeScript
off(type: 'callingDisplayDidChange', callback?: Callback<number>): void
```

取消订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callingDisplayDidChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (displayId: number) => {
  console.info('InputMethodAbility delete calling display notification.');
});
```

## off('discardTypingText')

```TypeScript
off(type: 'discardTypingText', callback?: Callback<void>): void
```

取消订阅编辑框应用发送\u201c清空候选词\u201d事件到输入法。使用callback异步回调。 <br> <br>使用场景：编辑框应用需要通知输入法清空当前候选词列表时使用（如用户切换输入框、提交表单后等场景）。 <br> <br>使用后效果：当编辑框应用发送清空候选词请求时触发回调，输入法应用应在回调中清空候选词列表和预输入文本。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discardTypingText' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**示例**

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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 否 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

console.info(`unregist calling display changed `);
inputMethodAbility!.offCallingDisplayDidChange((num: int) => {
  console.info('inputMethodAbility delete calling display  notification.');
});
```

## offDiscardTypingText

```TypeScript
offDiscardTypingText(callback?: Callback<void>): void
```

取消订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import inputMethodEngine from '@ohos.inputMethodEngine';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
console.info(`discard the typing text`);
inputMethodAbility!.offDiscardTypingText(() => {
  console.info('inputMethodAbility discard the typing text.');
});
```

## offInputStart

```TypeScript
offInputStart(callback?: IMAInputStartCallback): void
```

取消订阅输入法绑定成功事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | 否 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!
  .offInputStart((kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.InputClient) => {
  console.info('delete inputStart notification.');
});
```

## offInputStop

```TypeScript
offInputStop(callback: Callback<void>): void
```

取消订阅输入法输入停止（[inputStop](#oninputstop)）事件，停止监听 系统要求输入法终止输入流程的触发动作。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.offInputStop(() => {
  console.info('inputMethodAbility delete inputStop notification.');
});
```

## offKeyboardHide

```TypeScript
offKeyboardHide(callback?: Callback<void>): void
```

取消订阅输入法键盘隐藏（[keyboardHide](#onkeyboardshow-keyboardhide)）事 件，停止监听输入法键盘隐藏的触发动作。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.offKeyboardShow(() => {
  console.info('inputMethodAbility delete keyboardShow notification.');
});
inputMethodAbility!.offKeyboardHide(() => {
  console.info('inputMethodAbility delete keyboardHide notification.');
});
```

## offKeyboardShow

```TypeScript
offKeyboardShow(callback?: Callback<void>): void
```

取消订阅输入法事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!.offKeyboardShow(() => {
  console.info('inputMethodAbility delete keyboardShow notification.');
});
inputMethodAbility!.offKeyboardHide(() => {
  console.info('inputMethodAbility delete keyboardHide notification.');
});
```

## offPrivateCommand

```TypeScript
offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void
```

取消订阅输入法私有数据事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
let privateCommandCallback = (record: Record<string, inputMethodEngine.CommandDataType>) => {
  record.forEach((key, value) => {
    console.info(`private command key: ${key}, value: ${value}`);
  });
}
console.info(`regist private command `);
inputMethodAbility!.offPrivateCommand(privateCommandCallback);
```

## offSecurityModeChange

```TypeScript
offSecurityModeChange(callback?: Callback<SecurityMode>): void
```

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | 否 |

**示例**

```TypeScript
let InputMethodEngine = inputMethodEngine.getInputMethodAbility();
let securityChangeCallback = (securityMode: inputMethodEngine.SecurityMode) => {
  console.info(`inputMethodAbility securityModeChange, security is ${securityMode}`);
};
InputMethodEngine.onSecurityModeChange(securityChangeCallback);
InputMethodEngine.offSecurityModeChange(securityChangeCallback);
```

## offSetCallingWindow

```TypeScript
offSetCallingWindow(callback: Callback<int>): void
```

取消订阅编辑框设置调用窗口 ID（ [setCallingWindow](#onsetcallingwindow)）事件，停止监 听编辑框设置调用窗口标识的触发动作。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.offSetCallingWindow((wid: int) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

## offSetSubtype

```TypeScript
offSetSubtype(callback?: Callback<InputMethodSubtype>): void
```

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | 否 |

**示例**

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!.offSetSubtype((inputMethodSubtype: InputMethodSubtype) => {
  console.info('inputMethodAbility setSubtype.');
});
```

## on('inputStart')

```TypeScript
on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

订阅输入法绑定成功事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在编辑框获得焦点并绑定输入法时，获取KeyboardController和InputClient实例以进行后续的键盘操作和文本交互。 <br> <br>使用后效果：当编辑框绑定到输入法应用时，触发回调并返回KeyboardController和InputClient实例。输入法应用可在回调中创建面板、加载键盘页面、订阅KeyboardDelegate事件等。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStart' | 是 |
| callback | (kbController: KeyboardController, inputClient: InputClient) = & gt; void | 是 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (keyboardController: inputMethodEngine.KeyboardController, inputClient: inputMethodEngine.InputClient) => {
      // 使用kbController和client进行相关操作
    });
```

## on('inputStop')

```TypeScript
on(type: 'inputStop', callback: () => void): void
```

订阅停止输入法应用事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在编辑框失去焦点或用户切换输入法时，执行清理操作（如隐藏面板、释放资源）。 <br> <br>使用后效果：当输入法应用被停止绑定时触发回调。输入法应用应在回调中隐藏面板、取消事件订阅、释放InputClient相关资源。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'inputStop' | 是 |
| callback | () = & gt; void | 是 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});
```

## on('setCallingWindow')

```TypeScript
on(type: 'setCallingWindow', callback: (wid: number) => void): void
```

订阅设置调用窗口事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在绑定应用的窗口发生变化时（如应用切换窗口、多窗口场景），调整面板位置或重新定位。 <br> <br>使用后效果：当调用方窗口发生变化时触发回调，返回新的窗口ID。输入法应用可根据窗口ID调整面板位置。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setCallingWindow' | 是 |
| callback | (wid: number) = & gt; void | 是 |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (windowId: number) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在软键盘显示/隐藏时，执行相应的界面更新操作（如调整面板布局、更新候选词区域）。 <br> <br>使用后效果：当软键盘显示请求触发时，'keyboardShow'回调被调用，输入法应用应在回调中调用panel.show()显示面板；当软键盘隐藏请求触发时，'keyboardHide'回调被调用，输入法应用应在回调中调用 panel.hide()隐藏面板。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 是 |

**示例**

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

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在软键盘显示/隐藏时，执行相应的界面更新操作（如调整面板布局、更新候选词区域）。 <br> <br>使用后效果：当软键盘显示请求触发时，'keyboardShow'回调被调用，输入法应用应在回调中调用panel.show()显示面板；当软键盘隐藏请求触发时，'keyboardHide'回调被调用，输入法应用应在回调中调用 panel.hide()隐藏面板。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | 是 |
| callback | () = & gt; void | 是 |

**示例**

参见 on

## on('setSubtype')

```TypeScript
on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void
```

订阅设置输入法子类型事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在子类型（如语言、输入模式）发生变化时，切换到对应的键盘布局或输入逻辑。 <br> <br>使用后效果：当输入法子类型变化时触发回调，返回新的输入法子类型信息。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'setSubtype' | 是 |
| callback | (inputMethodSubtype: InputMethodSubtype) = & gt; void | 是 |

**示例**

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

订阅输入法安全模式改变类型事件。使用callback异步回调。 <br> <br>使用场景：输入法应用需要在安全模式发生变化时（如编辑框切换到密码输入模式、隐私模式等），调整键盘行为（如禁止截图、切换到安全键盘布局等）。 <br> <br>使用后效果：当安全模式变化时触发回调，返回当前的安全模式值。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'securityModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | 是 |

**示例**

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

订阅输入法私有数据事件。使用callback异步回调。 <br> <br>使用场景：应用与输入法之间需要传递私有数据（如自定义命令、配置信息等）时使用。仅系统默认输入法应用可订阅此事件。 <br> <br>使用后效果：当绑定应用向输入法发送私有数据时触发回调，返回私有数据记录。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'privateCommand' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

**示例**

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (const key in record) {
      console.info(`private command key: ${key}, value: ${record[key]}`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

## on('callingDisplayDidChange')

```TypeScript
on(type: 'callingDisplayDidChange', callback: Callback<number>): void
```

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。 <br> <br>使用场景：多屏幕设备场景下，编辑框在不同屏幕间切换时，输入法应用需根据新的屏幕ID调整面板位置和大小。 <br> <br>使用后效果：当编辑框所在屏幕ID发生变化时触发回调，返回新的屏幕ID。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callingDisplayDidChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', (displayId: number) => {
  console.info(`display id: ${displayId}`);
});
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

## on('discardTypingText')

```TypeScript
on(type: 'discardTypingText', callback: Callback<void>): void
```

订阅编辑框应用发送\u201c清空候选词\u201d事件到输入法。使用callback异步回调。 <br> <br>使用场景：编辑框应用需要通知输入法清空当前候选词列表时使用（如用户切换输入框、提交表单后等场景）。 <br> <br>使用后效果：当编辑框应用发送清空候选词请求时触发回调，输入法应用应在回调中清空候选词列表和预输入文本。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'discardTypingText' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
let callingDisplayDidChangeCallback = (num: int) => {
  console.info(`display id: ${num}`);
}

console.info(`regist calling display changed`);
inputMethodAbility!.onCallingDisplayDidChange(callingDisplayDidChangeCallback);
```

## onDiscardTypingText

```TypeScript
onDiscardTypingText(callback: Callback<void>): void
```

订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import inputMethodEngine from '@ohos.inputMethodEngine';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
console.info(`discard the typing text`);
inputMethodAbility!.onDiscardTypingText(() => {
  console.info('inputMethodAbility discard the typing text.');
});
```

## onInputStart

```TypeScript
onInputStart(callback: IMAInputStartCallback): void
```

订阅输入法绑定成功事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!
.onInputStart((kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
  let keyboardController = kbController;
  let inputClient = client;
});
```

## onInputStop

```TypeScript
onInputStop(callback: Callback<void>): void
```

订阅停止输入法应用事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.onInputStop(() => {
  console.info('inputMethodAbility inputStop');
});
```

## onKeyboardHide

```TypeScript
onKeyboardHide(callback: Callback<void>): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.onKeyboardShow(() => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodAbility!.onKeyboardHide(() => {
  console.info('inputMethodEngine keyboardHide.');
});
```

## onKeyboardShow

```TypeScript
onKeyboardShow(callback: Callback<void>): void
```

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.onKeyboardShow(() => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodAbility!.onKeyboardHide(() => {
  console.info('inputMethodEngine keyboardHide.');
});
```

## onPrivateCommand

```TypeScript
onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void
```

订阅输入法私有数据事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

let privateCommandCallback = (record: Record<string, inputMethodEngine.CommandDataType>) => {
  record.forEach((key, value) => {
    console.info(`private command key: ${key}, value: ${value}`);
  });
}

console.info(`regist private command `);
inputMethodAbility!.onPrivateCommand(privateCommandCallback);
```

## onSecurityModeChange

```TypeScript
onSecurityModeChange(callback: Callback<SecurityMode>): void
```

订阅输入法安全模式改变类型事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!.onSecurityModeChange((securityMode: inputMethodEngine.SecurityMode) => {
  console.info(`inputMethodAbility securityModeChange, security is ${securityMode}`);
});
```

## onSetCallingWindow

```TypeScript
onSetCallingWindow(callback: Callback<int>): void
```

订阅设置调用窗口事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | 是 |

**示例**

```TypeScript
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility!.onSetCallingWindow((wid: int) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

## onSetSubtype

```TypeScript
onSetSubtype(callback: Callback<InputMethodSubtype>): void
```

订阅设置输入法子类型事件。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | 是 |

**示例**

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';
let inputMethodAbility = inputMethodEngine.getInputMethodAbility();

inputMethodAbility!.onSetSubtype((inputMethodSubtype: InputMethodSubtype) => {
  console.info('inputMethodAbility setSubtype.');
});
```
