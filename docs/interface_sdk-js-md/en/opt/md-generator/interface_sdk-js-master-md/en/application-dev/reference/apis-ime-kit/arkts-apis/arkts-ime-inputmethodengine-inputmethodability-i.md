# InputMethodAbility

In the following API examples, you must first use   
[getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md#getInputMethodAbility) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance.

**Since:** 9

<!--Device-inputMethodEngine-interface InputMethodAbility--><!--Device-inputMethodEngine-interface InputMethodAbility-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void
```

Creates an input method panel. This API can be called only by the input method application in the   
[InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md#InputMethodExtensionAbility) class. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Only one [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) panel and one
> [STATUS_BAR](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) panel can be created for a single input method.

> The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such
> as
> [window.createWindow](../../apis-arkui/arkts-apis/arkts-arkui-window-createwindow-f.md#createWindow)
> , [bindContextMenu](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindContextMenu),
> and [CustomDialog](./@internal/component/ets/custom_dialog_controller). You are advised to adopt
> alternative solutions to sub-windows, such as using a [dialog box](@ohos.arkui.advanced.Dialog) or
> [bindMenu](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindMenu), or set
> **showInSubwindow** to **false**.

**Since:** 10

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| info | [PanelInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Panel&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800004-not-an-input-method) |

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

Creates an input method panel. This API can be called only by the input method application in the   
[InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md#InputMethodExtensionAbility) class. This API uses a promise to return the result.

> **NOTE：**
> 
> Only one [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) panel and one
> [STATUS_BAR](arkts-ime-inputmethodengine-paneltype-e.md#PanelType) panel can be created for a single input method.

> The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such
> as
> [window.createWindow](../../../windowmanager/application-window-fa.md#setting-the-child-window-of-an-application)
> , [bindContextMenu](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindContextMenu),
> and [CustomDialog](./@internal/component/ets/custom_dialog_controller). You are advised to adopt
> alternative solutions to sub-windows, such as using a [dialog box](@ohos.arkui.advanced.Dialog) or
> [bindMenu](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindMenu), or set
> **showInSubwindow** to **false**.

**Since:** 10

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](../../apis-arkui/arkts-apis/arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| info | [PanelInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Panel & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800004-not-an-input-method) |

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

Destroys the specified input method panel. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void--><!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| panel | [Panel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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

Destroys the specified input method panel. This API uses a promise to return the result.

**Since:** 10

<!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>--><!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| panel | [Panel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-selectionmanager-panel-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

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

Obtains the current security mode of the input method.

**Since:** 11

<!--Device-InputMethodAbility-getSecurityMode(): SecurityMode--><!--Device-InputMethodAbility-getSecurityMode(): SecurityMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800004-not-an-input-method) |

## Examples

```TypeScript
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

## off('inputStart')

```TypeScript
off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

Disables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStart' | Yes |
| callback | (kbController: KeyboardController, inputClient: InputClient) = & gt; void | No |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

## off('inputStop')

```TypeScript
off(type: 'inputStop', callback: () => void): void
```

Disables listening for the input method stop event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStop' | Yes |
| callback | () = & gt; void | Yes |

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

Disables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setCallingWindow' | Yes |
| callback | (wid: number) = & gt; void | Yes |

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

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | No |

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

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | No |

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

Disables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setSubtype' | Yes |
| callback | (inputMethodSubtype: InputMethodSubtype) = & gt; void | No |

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

Disables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'securityModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | No |

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

Disables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'privateCommand' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, CommandDataType&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [12800010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

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

Disables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void--><!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

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

Unsubscribes from the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void--><!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discardTypingText' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

## on('inputStart')

```TypeScript
on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

Enables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStart' | Yes |
| callback | (kbController: KeyboardController, inputClient: InputClient) = & gt; void | Yes |

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

Enables listening for the input method unbinding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStop' | Yes |
| callback | () = & gt; void | Yes |

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

Enables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setCallingWindow' | Yes |
| callback | (wid: number) = & gt; void | Yes |

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

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | Yes |

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

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | Yes |

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

Enables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setSubtype' | Yes |
| callback | (inputMethodSubtype: InputMethodSubtype) = & gt; void | Yes |

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

Enables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'securityModeChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | Yes |

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

Enables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'privateCommand' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, CommandDataType&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

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

Enables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void--><!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

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

Subscribes to the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void--><!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discardTypingText' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```
