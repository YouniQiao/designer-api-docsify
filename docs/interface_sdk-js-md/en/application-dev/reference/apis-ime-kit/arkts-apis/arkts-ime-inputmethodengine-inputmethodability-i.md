# InputMethodAbility

In the following API examples, you must first use [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance.

**Since:** 23

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

Creates an input method panel. This API can be called only by the input method application in the [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md) class. This API uses an asynchronous callback to return the result. > **NOTE：**> > Only one [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md) panel and one > [STATUS_BAR](arkts-ime-inputmethodengine-paneltype-e.md) panel can be created for a single input method. > The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such > as > [window.createWindow](../../apis-arkui/arkts-apis/arkts-arkui-window-createwindow-f.md) > , bindContextMenu, > and CustomDialog. You are advised to adopt > alternative solutions to sub-windows, such as using a dialog box or > bindMenu, or set > **showInSubwindow** to **false**.

**Since:** 23

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | Current context of the input method. |
| info | PanelInfo | Yes | Information about the input method panel. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Panel&gt; | Yes | Callback used to return the result. If the operation is successful, the created input method panel is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) | not an input method application. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

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
```

## createPanel

```TypeScript
createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>
```

Creates an input method panel. This API can be called only by the input method application in the [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md) class. This API uses a promise to return the result. > **NOTE：**> > Only one [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md) panel and one > [STATUS_BAR](arkts-ime-inputmethodengine-paneltype-e.md) panel can be created for a single input method. > The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such > as > [window.createWindow](../../../windowmanager/application-window-fa.md#setting-the-child-window-of-an-application) > , bindContextMenu, > and CustomDialog. You are advised to adopt > alternative solutions to sub-windows, such as using a dialog box or > bindMenu, or set > **showInSubwindow** to **false**.

**Since:** 23

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | Current context of the input method. |
| info | PanelInfo | Yes | Information about the input method panel. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Panel&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) | not an input method application. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

if (this.context) {
  inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
    .then((panel: inputMethodEngine.Panel) => {
      console.info('Succeed in creating panel.');
    }).catch((err: BusinessError) => {
    console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
  })
}
```

## destroyPanel

```TypeScript
destroyPanel(panel: Panel, callback: AsyncCallback<void>): void
```

Destroys the specified input method panel. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void--><!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | Panel | Yes | Input method panel to destroy. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**Examples**

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

**Since:** 23

<!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>--><!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | Panel | Yes | Input method panel to destroy. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**Examples**

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

**Since:** 23

<!--Device-InputMethodAbility-getSecurityMode(): SecurityMode--><!--Device-InputMethodAbility-getSecurityMode(): SecurityMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md) | Security mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) | not an input method application. |

**Examples**

```TypeScript
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

## offCallingDisplayDidChange

```TypeScript
offCallingDisplayDidChange(callback?: Callback<int>): void
```

Unsubscribe 'callingDisplayDidChange' event.

**Since:** 23

<!--Device-InputMethodAbility-offCallingDisplayDidChange(callback?: Callback<int>): void--><!--Device-InputMethodAbility-offCallingDisplayDidChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | optional, the callback called when calling display id changed. |

## offDiscardTypingText

```TypeScript
offDiscardTypingText(callback?: Callback<void>): void
```

Unsubscribe 'discardTypingText' event.

**Since:** 23

<!--Device-InputMethodAbility-offDiscardTypingText(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offDiscardTypingText(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | optional, the callback called when the edit box requests to discard typing text. |

## offInputStart

```TypeScript
offInputStart(callback?: IMAInputStartCallback): void
```

Unsubscribe 'inputStart' event.

**Since:** 23

<!--Device-InputMethodAbility-offInputStart(callback?: IMAInputStartCallback): void--><!--Device-InputMethodAbility-offInputStart(callback?: IMAInputStartCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | No | optional, the callback called when edit box requests keyboard. |

## offInputStop

```TypeScript
offInputStop(callback: Callback<void>): void
```

Unsubscribe 'inputStop'.

**Since:** 23

<!--Device-InputMethodAbility-offInputStop(callback: Callback<void>): void--><!--Device-InputMethodAbility-offInputStop(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when the system needs input method application to terminate itself. |

## offKeyboardHide

```TypeScript
offKeyboardHide(callback?: Callback<void>): void
```

Unsubscribe 'keyboardHide'.

**Since:** 23

<!--Device-InputMethodAbility-offKeyboardHide(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offKeyboardHide(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | optional, the callback called when hiding keyboard. |

## offKeyboardShow

```TypeScript
offKeyboardShow(callback?: Callback<void>): void
```

Unsubscribe 'keyboardShow'.

**Since:** 23

<!--Device-InputMethodAbility-offKeyboardShow(callback?: Callback<void>): void--><!--Device-InputMethodAbility-offKeyboardShow(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | optional, the callback called when showing keyboard. |

## offPrivateCommand

```TypeScript
offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void
```

Unsubscribe 'privateCommand'. This function can only be called by default input method configured by system.

**Since:** 23

<!--Device-InputMethodAbility-offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-offPrivateCommand(callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | No | optional, the callback called when receiving private command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) | not the preconfigured default input method. |

## offSecurityModeChange

```TypeScript
offSecurityModeChange(callback?: Callback<SecurityMode>): void
```

Unsubscribe 'securityModeChange' event.

**Since:** 23

<!--Device-InputMethodAbility-offSecurityModeChange(callback?: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-offSecurityModeChange(callback?: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | No | optional, the callback called when the security mode changes. |

## offSetCallingWindow

```TypeScript
offSetCallingWindow(callback: Callback<int>): void
```

Unsubscribe 'setCallingWindow'.

**Since:** 23

<!--Device-InputMethodAbility-offSetCallingWindow(callback: Callback<int>): void--><!--Device-InputMethodAbility-offSetCallingWindow(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback called when the edit box sets calling window id. |

## offSetSubtype

```TypeScript
offSetSubtype(callback?: Callback<InputMethodSubtype>): void
```

Unsubscribe 'setSubtype'.

**Since:** 23

<!--Device-InputMethodAbility-offSetSubtype(callback?: Callback<InputMethodSubtype>): void--><!--Device-InputMethodAbility-offSetSubtype(callback?: Callback<InputMethodSubtype>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | No | optional, the callback called when the system notify to switch subtype. |

## off_callingDisplayDidChange('callingDisplayDidChange')

```TypeScript
off(type: 'callingDisplayDidChange', callback?: Callback<number>): void
```

Disables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void--><!--Device-InputMethodAbility-off(type: 'callingDisplayDidChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes | Event type, which is **'callingDisplayDidChange'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
  console.info('InputMethodAbility delete calling display  notification.');
});
```

## off_discardTypingText('discardTypingText')

```TypeScript
off(type: 'discardTypingText', callback?: Callback<void>): void
```

Unsubscribes from the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void--><!--Device-InputMethodAbility-off(type: 'discardTypingText', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discardTypingText' | Yes | Event type, which is **'discardTypingText'**. <br> - **'discardTypingText'**: indicates unsubscribing from the event of discarding candidate words and sending the event to the input method. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

## off_inputStart('inputStart')

```TypeScript
off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

Disables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: KeyboardController, inputClient: InputClient) =&gt; void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

## off_inputStop('inputStop')

```TypeScript
off(type: 'inputStop', callback: () => void): void
```

Disables listening for the input method stop event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-off(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStop' | Yes | Event type, which is **'inputStop'**. |
| callback | () =&gt; void | Yes | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
  console.info('inputMethodAbility delete inputStop notification.');
});
```

## off_keyboardHide('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | Event type. <br>- The value **'keyboardShow'** indicates the keyboard display event. <br>- The value **'keyboardHide'** indicates the keyboard hiding event. |
| callback | () =&gt; void | No | Callback used to return the result. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

## off_keyboardShow('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void--><!--Device-InputMethodAbility-off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | Event type. <br>- The value **'keyboardShow'** indicates the keyboard display event. <br>- The value **'keyboardHide'** indicates the keyboard hiding event. |
| callback | () =&gt; void | No | Callback used to return the result. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

## off_privateCommand('privateCommand')

```TypeScript
off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void
```

Disables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateCommand' | Yes | Event type, which is **'privateCommand'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) | not the preconfigured default input method. |

**Examples**

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

## off_securityModeChange('securityModeChange')

```TypeScript
off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void
```

Disables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'securityModeChange' | Yes | Event type, which is **'securityModeChange'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
  (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  };
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('securityModeChange', securityChangeCallback);
inputMethodAbility.off('securityModeChange', securityChangeCallback);
```

## off_setCallingWindow('setCallingWindow')

```TypeScript
off(type: 'setCallingWindow', callback: (wid: number) => void): void
```

Disables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-off(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setCallingWindow' | Yes | Event type, which is **'setCallingWindow'**. |
| callback | (wid: number) =&gt; void | Yes | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

## off_setSubtype('setSubtype')

```TypeScript
off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void
```

Disables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setSubtype' | Yes | Event type, which is **'setSubtype'**. |
| callback | (inputMethodSubtype: InputMethodSubtype) =&gt; void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
  console.info('InputMethodAbility delete setSubtype notification.');
});
```

## onCallingDisplayDidChange

```TypeScript
onCallingDisplayDidChange(callback: Callback<int>): void
```

Subscribe 'callingDisplayDidChange' event.

**Since:** 23

<!--Device-InputMethodAbility-onCallingDisplayDidChange(callback: Callback<int>): void--><!--Device-InputMethodAbility-onCallingDisplayDidChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback called when calling display id changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | capability not supported. |

## onDiscardTypingText

```TypeScript
onDiscardTypingText(callback: Callback<void>): void
```

Subscribe 'discardTypingText' event.

**Since:** 23

<!--Device-InputMethodAbility-onDiscardTypingText(callback: Callback<void>): void--><!--Device-InputMethodAbility-onDiscardTypingText(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when the edit box requests to discard typing text. |

## onInputStart

```TypeScript
onInputStart(callback: IMAInputStartCallback): void
```

Subscribe 'inputStart' event.

**Since:** 23

<!--Device-InputMethodAbility-onInputStart(callback: IMAInputStartCallback): void--><!--Device-InputMethodAbility-onInputStart(callback: IMAInputStartCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IMAInputStartCallback](arkts-ime-inputmethodengine-imainputstartcallback-t.md) | Yes | the callback called when edit box requests keyboard. |

## onInputStop

```TypeScript
onInputStop(callback: Callback<void>): void
```

Subscribe 'inputStop'.

**Since:** 23

<!--Device-InputMethodAbility-onInputStop(callback: Callback<void>): void--><!--Device-InputMethodAbility-onInputStop(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when the system needs input method application to terminate itself. |

## onKeyboardHide

```TypeScript
onKeyboardHide(callback: Callback<void>): void
```

Subscribe 'keyboardHide'.

**Since:** 23

<!--Device-InputMethodAbility-onKeyboardHide(callback: Callback<void>): void--><!--Device-InputMethodAbility-onKeyboardHide(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when hiding keyboard. |

## onKeyboardShow

```TypeScript
onKeyboardShow(callback: Callback<void>): void
```

Subscribe 'keyboardShow'.

**Since:** 23

<!--Device-InputMethodAbility-onKeyboardShow(callback: Callback<void>): void--><!--Device-InputMethodAbility-onKeyboardShow(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when showing keyboard. |

## onPrivateCommand

```TypeScript
onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void
```

Subscribe 'privateCommand'. This function can only be called by default input method configured by system.

**Since:** 23

<!--Device-InputMethodAbility-onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-onPrivateCommand(callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | Yes | the callback called when receiving private command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) | not the preconfigured default input method. |

## onSecurityModeChange

```TypeScript
onSecurityModeChange(callback: Callback<SecurityMode>): void
```

Subscribe 'securityModeChange' event.

**Since:** 23

<!--Device-InputMethodAbility-onSecurityModeChange(callback: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-onSecurityModeChange(callback: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | Yes | the callback called when the security mode changes. |

## onSetCallingWindow

```TypeScript
onSetCallingWindow(callback: Callback<int>): void
```

Subscribe 'setCallingWindow'.

**Since:** 23

<!--Device-InputMethodAbility-onSetCallingWindow(callback: Callback<int>): void--><!--Device-InputMethodAbility-onSetCallingWindow(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback called when the edit box sets calling window id. |

## onSetSubtype

```TypeScript
onSetSubtype(callback: Callback<InputMethodSubtype>): void
```

Subscribe 'setSubtype'.

**Since:** 23

<!--Device-InputMethodAbility-onSetSubtype(callback: Callback<InputMethodSubtype>): void--><!--Device-InputMethodAbility-onSetSubtype(callback: Callback<InputMethodSubtype>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; | Yes | the callback called when the system notify to switch subtype. |

## on_callingDisplayDidChange('callingDisplayDidChange')

```TypeScript
on(type: 'callingDisplayDidChange', callback: Callback<number>): void
```

Enables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**Since:** 18

<!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void--><!--Device-InputMethodAbility-on(type: 'callingDisplayDidChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callingDisplayDidChange' | Yes | Event type, which is **'callingDisplayDidChange'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | Callback used to return the screen ID of the window corresponding to the edit box. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | capability not supported. |

**Examples**

```TypeScript
let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
  console.info(`display id: ${num}`);
}
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

## on_discardTypingText('discardTypingText')

```TypeScript
on(type: 'discardTypingText', callback: Callback<void>): void
```

Subscribes to the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void--><!--Device-InputMethodAbility-on(type: 'discardTypingText', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discardTypingText' | Yes | Event type, which is **'discardTypingText'**. <br> - **'discardTypingText'** : indicates subscribing to the event of discarding candidate words and sending the event to the input method. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

## on_inputStart('inputStart')

```TypeScript
on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void
```

Enables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void--><!--Device-InputMethodAbility-on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStart' | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: KeyboardController, inputClient: InputClient) =&gt; void | Yes | Callback used to return instances related to input method operations. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
    });
```

## on_inputStop('inputStop')

```TypeScript
on(type: 'inputStop', callback: () => void): void
```

Enables listening for the input method unbinding event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'inputStop', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'inputStop' | Yes | Event type, which is **'inputStop'**. |
| callback | () =&gt; void | Yes | Callback used to return the result. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});
```

## on_keyboardHide('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | Event type. <br>- The value **'keyboardShow'** indicates the keyboard display event. <br>- The value **'keyboardHide'** indicates the keyboard hiding event. |
| callback | () =&gt; void | Yes | Callback used to return the result. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

## on_keyboardShow('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void--><!--Device-InputMethodAbility-on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes | Event type. <br>- The value **'keyboardShow'** indicates the keyboard display event. <br>- The value **'keyboardHide'** indicates the keyboard hiding event. |
| callback | () =&gt; void | Yes | Callback used to return the result. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

## on_privateCommand('privateCommand')

```TypeScript
on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void
```

Enables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void--><!--Device-InputMethodAbility-on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'privateCommand' | Yes | Event type, which is **'privateCommand'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, CommandDataType&gt;&gt; | Yes | Callback used to return the private data sent to the input method application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) | not the preconfigured default input method. |

**Examples**

```TypeScript
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

## on_securityModeChange('securityModeChange')

```TypeScript
on(type: 'securityModeChange', callback: Callback<SecurityMode>): void
```

Enables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void--><!--Device-InputMethodAbility-on(type: 'securityModeChange', callback: Callback<SecurityMode>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'securityModeChange' | Yes | Event type, which is **'securityModeChange'**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityMode](arkts-ime-inputmethodengine-securitymode-e.md)&gt; | Yes | Callback used to return the current security mode. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  });
```

## on_setCallingWindow('setCallingWindow')

```TypeScript
on(type: 'setCallingWindow', callback: (wid: number) => void): void
```

Enables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void--><!--Device-InputMethodAbility-on(type: 'setCallingWindow', callback: (wid: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setCallingWindow' | Yes | Event type, which is **'setCallingWindow'**. |
| callback | (wid: number) =&gt; void | Yes | Callback used to return the window ID of the caller. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

## on_setSubtype('setSubtype')

```TypeScript
on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void
```

Enables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void--><!--Device-InputMethodAbility-on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setSubtype' | Yes | Event type, which is **'setSubtype'**. |
| callback | (inputMethodSubtype: InputMethodSubtype) =&gt; void | Yes | Callback used to return the input method subtype. |

**Examples**

```TypeScript
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
  console.info('InputMethodAbility setSubtype.');
});
```

