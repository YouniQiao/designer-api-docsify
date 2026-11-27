# InputMethodAbility

```TypeScript
interface InputMethodAbility
```

In the following API examples, you must first use [getInputMethodAbility](arkts-ime-inputmethodengine-getinputmethodability-f.md) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance.

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

This interface is used to create an input method panel. The input method can be invoked only by the input method application in the [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md) class. Use the callback asynchronous callback. <br> <br> Pairing call: <br> <br> - After calling createPanel() to create a panel, you must call [destroyPanel](#destroypanel-1) to destroy the panel after using it to release resources. <br>- If destroyPanel() is not invoked, panel resources are leaked, affecting the use of system resources. <br>- A single input method application allows only one soft keyboard type and one status bar type panel to be created. <br> <br>  
> **Note:** <br>
> <br>
> Only one panel of [soft keyboard type] [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) and [status bar type] [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) can be created for a single input method application. <br>&gt;You are not allowed to create panels of the same type repeatedly. You must reuse existing panels or destroy existing panels before creating panels of the same type. <br> &gt;When a panel fails to be created, the historical error code 1 is used for dynamic implementation, and the error code 12800004 is used for static implementation. Locate the failure cause based on the error information and native logs. <br>
> <br>
> The input method panel does not support creating sub-windows. For example, the window.createWindow [Setting Application Subwindow](../../../windowmanager/application-window-fa.md# Setting Application Subwindow), <br>
> [bindContextMenu](../../apis-arkui/arkts-components/arkts-arkui-common-comp-commonmethod-c.md#bindcontextmenu-1) <br> &gt;, and [CustomDialog](../../apis-arkui/arkts-apis/arkts-arkui-customdialogcontroller.md#custom_dialog_controllercustomdialog) interfaces cannot be used to create subwindow pop-up windows. You are advised to use a non-subwindow alternative, for example, <br>
> [pop-up] [Dialog](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialog.md), <br>
> [bindMenu](../../apis-arkui/arkts-components/arkts-arkui-common-comp-commonmethod-c.md#bindmenu-1), or set <br>
> showInSubwindow to false.

**Since:** 10

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | Current context of the input method. |
| info | [PanelInfo](arkts-ime-inputmethodengine-panelinfo-i.md) | Yes | Information about the input method panel. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Panel](arkts-ime-inputmethodengine-panel-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, the created input method panel is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) | not an input method application. |

**Examples**

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

This interface is used to create an input method panel. This interface can be invoked only by the input method application in the [InputMethodExtensionAbility](arkts-ime-inputmethodextensionability-c.md) class. Use the promise asynchronous callback. <br> <br>  
> **Note:** <br>
> <br>
> Only one panel of [soft keyboard type] [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) and [status bar type] [PanelType](arkts-ime-inputmethodengine-paneltype-e.md) can be created for a single input method application. <br>&gt;You are not allowed to create panels of the same type repeatedly. You must reuse existing panels or destroy existing panels before creating panels of the same type. <br>&gt;When a panel fails to be created, the historical error code 1 is used for dynamic implementation, and the error code 12800004 is used for static implementation. Locate the failure cause based on the error information and native logs. <br>
> <br>
> The input method panel does not support creating sub-windows. For example, the window.createWindow

[Setting Application Subwindow](../../../windowmanager/application-window-fa.md# Setting Application Subwindow), <br>  
> [bindContextMenu](../../apis-arkui/arkts-components/arkts-arkui-common-comp-commonmethod-c.md#bindcontextmenu-1) <br> &gt;, and [CustomDialog](../../apis-arkui/arkts-apis/arkts-arkui-customdialogcontroller.md#custom_dialog_controllercustomdialog) interface cannot be used to create subwindow pop-up windows. You are advised to use a non-subwindow alternative, for example, <br>
> [pop-up] [Dialog](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialog.md), <br>
> [bindMenu](../../apis-arkui/arkts-components/arkts-arkui-common-comp-commonmethod-c.md#bindmenu-1), or set <br>
> showInSubwindow to false.

**Since:** 10

<!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>--><!--Device-InputMethodAbility-createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes | Current context of the input method. |
| info | [PanelInfo](arkts-ime-inputmethodengine-panelinfo-i.md) | Yes | Information about the input method panel. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Panel](arkts-ime-inputmethodengine-panel-i.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) | not an input method application. |

**Examples**

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

Destroy the input method panel. This interface must be invoked before creating a panel by calling [createPanel] _[createPanel](#createpanel-1)_. Use the callback asynchronous callback. <br> <br> Pair Call: <br> <br> - Must be used with the [createPanel](#createpanel-1) method to destroy the input method panel created by createPanel(). <br>- The panel to be destroyed must be a panel object that has been successfully created. <br>- If the panel is not destroyed correctly, resource leakage may occur. You are advised to call destroyPanel() to release resources after the panel is used. After being destroyed, the panel instance becomes invalid and cannot be reused. Destroying the old instance does not remove the registration information of the new panel of the same type. When the native layer fails to be destroyed, the encapsulation object that is still valid is not invalidated, and the registration information of the encapsulation object is not removed. You can handle the error and then try again. If the window fails to be destroyed, the error code mapping of the existing panel operation is used. Error code 1 is returned.

**Since:** 10

<!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void--><!--Device-InputMethodAbility-destroyPanel(panel: Panel, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | [Panel](arkts-ime-inputmethodengine-panel-i.md) | Yes | Input method panel to destroy. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | Failed to initialize or submit the asynchronous operation. |

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

Destroy the input method panel. Use the promise asynchronous callback. <br> <br> Pairing call: <br> <br> - Must be used with the [createPanel]_[createPanel](#createpanel-1) method to destroy the input method panel created by createPanel(). <br>- The destroyed panel must be a successfully created panel object. <br>- If the panel is not destroyed correctly, resource leakage may occur. You are advised to call destroyPanel() to release resources after the panel is used. After being destroyed, the panel instance becomes invalid and cannot be reused. Destroying the old instance does not remove the registration information of the new panel of the same type. When the native layer fails to be destroyed, the encapsulation object that is still valid is not invalidated, and its registration information is not removed. You can handle the error and try again. If the window fails to be destroyed, the error code mapping of the existing panel operation is used. Error code 1 is returned.

**Since:** 10

<!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>--><!--Device-InputMethodAbility-destroyPanel(panel: Panel): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| panel | [Panel](arkts-ime-inputmethodengine-panel-i.md) | Yes | Input method panel to destroy. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | Failed to initialize or submit the asynchronous operation. |

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

**Since:** 11

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

## off('inputStart')

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

## off('inputStop')

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

## off('setCallingWindow')

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

## off('keyboardShow' | 'keyboardHide')

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
| type | 'keyboardShow' &#124; 'keyboardHide' | Yes | Event type. <br> - The value **'keyboardShow'** indicates the keyboard display event. <br> - The value **'keyboardHide'** indicates the keyboard hiding event. |
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

## off('setSubtype')

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

## off('securityModeChange')

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

## off('privateCommand')

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md)&gt;&gt; | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

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

## off('callingDisplayDidChange')

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

## off('discardTypingText')

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

## on('inputStart')

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

## on('inputStop')

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

## on('setCallingWindow')

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

## on('keyboardShow' | 'keyboardHide')

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
| type | 'keyboardShow' &#124; 'keyboardHide' | Yes | Event type. <br> - The value **'keyboardShow'** indicates the keyboard display event. <br> - The value **'keyboardHide'** indicates the keyboard hiding event. |
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

## on('setSubtype')

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

## on('securityModeChange')

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

## on('privateCommand')

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
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, [CommandDataType](arkts-ime-inputmethodengine-commanddatatype-t.md)&gt;&gt; | Yes | Callback used to return the private data sent to the input method application. |

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

## on('callingDisplayDidChange')

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
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: 1. The hardware does not support the capability; 2. The chip does not support the capability; 3. A dependent service feature is not supported. |

**Examples**

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discardTypingText' | Yes | Event type, which is **'discardTypingText'**. <br> - **'discardTypingText'**: indicates subscribing to the event of discarding candidate words and sending the event to the input method. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```
