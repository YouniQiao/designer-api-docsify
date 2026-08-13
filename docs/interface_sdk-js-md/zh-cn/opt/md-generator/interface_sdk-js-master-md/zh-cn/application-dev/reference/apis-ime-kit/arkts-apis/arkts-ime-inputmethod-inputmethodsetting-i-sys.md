# InputMethodSetting

InputMethodSetting提供输入法配置与查询能力，面向前台应用提供以下功能： - **输入法变化订阅**：通过 on('imeChange') 订阅输入法及子类型变化事件，当用户切换输入法时收到通知。 - **输入法列表查询**：通过 [getInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getInputMethods) 查询已激活/未激活输入法列表，通过 [getAllInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getAllInputMethods) 查询所有已安装输入法列表，通过 [listInputMethodSubtype](arkts-ime-inputmethod-inputmethodsetting-i.md#listInputMethodSubtype) 查询指定输入法的子类型列表。 - **面板可见性查询**：通过isPanelShown查询输入法面板是否显示。 - **输入法选择对话框**：通过showOptionalInputMethods显示输入法选择对话框（已废弃，建议使用InputMethodListDialog）。 需通过[getSetting](arkts-ime-inputmethod-getsetting-f.md#getSetting)获取InputMethodSetting实例后使用。 下列API均需使用[getSetting](arkts-ime-inputmethod-getsetting-f.md#getSetting)获取到InputMethodSetting实例后，通过实例调用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethod-interface InputMethodSetting--><!--Device-inputMethod-interface InputMethodSetting-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## enableInputMethod

```TypeScript
enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>
```

修改输入法的启用状态。使用promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>--><!--Device-InputMethodSetting-enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| extensionName | string | 是 |
| [enabledState](arkts-ime-inputmethod-inputmethodproperty-i.md) | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800019](../errorcode-inputmethod-framework.md#12800019-系统配置的默认输入法不支持此操作) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-输入法未找到) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableInputMethodSafely() {
  const currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
  if (!currentIme) {
    console.error("Failed to get current input method");
    return;
  }

  inputMethod.getSetting()
    .enableInputMethod(currentIme.name, currentIme.id, inputMethod.EnabledState.BASIC_MODE)
    .then(() => {
      console.info('Succeeded in enable inputmethod.');
    })
    .catch((err) => {
      if (err instanceof BusinessError) {
        console.error(`Failed to enableInputMethod. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.error(`Failed to enableInputMethod. Error: ${err}`);
      }
    });
}

enableInputMethodSafely();
```

## enableInputMethod

```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: number): Promise<void>
```

修改指定用户输入法的启用状态。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-enableInputMethod(      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>--><!--Device-InputMethodSetting-enableInputMethod(      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: int): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| extensionName | string | 是 |
| [enabledState](arkts-ime-inputmethod-inputmethodproperty-i.md) | [EnabledState](arkts-ime-inputmethod-enabledstate-e.md) | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800019](../errorcode-inputmethod-framework.md#12800019-系统配置的默认输入法不支持此操作) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-输入法未找到) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(userId?: number): Array<InputMethodProperty>
```

获取指定用户的所有输入法应用列表。同步接口。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getAllInputMethodsSync(userId?: int): Array<InputMethodProperty>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## getCursorInfo

```TypeScript
getCursorInfo(userId?: number): CursorInfo
```

获取指定用户的光标信息。当编辑框未给输入法服务通知光标信息时，返回所有属性值都为0。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo--><!--Device-InputMethodSetting-getCursorInfo(userId?: int): CursorInfo-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let cursorInfo: inputMethod.CursorInfo = inputMethod.getSetting().getCursorInfo();
  console.info(`get cursorInfo success, left: ${cursorInfo.left}, top: ${cursorInfo.top}, width: ${cursorInfo.width}, height: ${cursorInfo.height}, displayId: ${cursorInfo.displayId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get cursorInfo. Code: ${error.code}, message: ${error.message}`);
}
```

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

获取默认输入法能力。为优化性能，返回的InputMethodProperty对象仅保证能够唯一标识输入法能力的`name`和`id`属性正确，其他属性可能为空。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty--><!--Device-InputMethodSetting-getDefaultInputMethodAbility(): InputMethodProperty-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const defaultAbility: inputMethod.InputMethodProperty = inputMethod.getSetting().getDefaultInputMethodAbility();
  console.info('Succeeded in getting default input method ability, name: ' + defaultAbility.name + ', id: ' + defaultAbility.id);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getDefaultInputMethodAbility. Code: ${error.code}, message: ${error.message}`);
}
```

## getInputMethodSubtypes

```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: number): Array<InputMethodSubtype>
```

获取指定用户指定输入法的子类型列表。同步接口。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>--><!--Device-InputMethodSetting-getInputMethodSubtypes(bundleName: string, userId?: int): Array<InputMethodSubtype>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean, userId?: number): Array<InputMethodProperty>
```

获取指定用户已激活/未激活的输入法应用列表。同步接口

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>--><!--Device-InputMethodSetting-getInputMethodsSync(enable: boolean, userId?: int): Array<InputMethodProperty>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

查询指定类型的输入法面板是否处于显示状态。

**起始版本：** 23

**废弃版本：** -1

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo): boolean-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

let info: PanelInfo = {
  type: PanelType.SOFT_KEYBOARD,
  flag: PanelFlag.FLAG_FIXED
}

try {
  let result: boolean = inputMethod.getSetting().isPanelShown(info);
  console.info('Succeeded in querying isPanelShown, result: ' + result);
} catch (err) {
  console.error(`Failed to query isPanelShown. Code: ${err.code}, message: ${err.message}`);
}
```

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: number): boolean
```

查询指定类型的输入法面板在指定屏幕上是否处于显示状态。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean--><!--Device-InputMethodSetting-isPanelShown(panelInfo: PanelInfo, displayId: long): boolean-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| panelInfo | [PanelInfo](arkts-ime-inputmethod-panel-panelinfo-i.md) | 是 |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

let displayId: number = 10;
let info: PanelInfo = {
  type: PanelType.SOFT_KEYBOARD,
  flag: PanelFlag.FLAG_FIXED
}

try {
  let result: boolean = inputMethod.getSetting().isPanelShown(info, displayId);
  console.info('Succeeded in querying isPanelShown, result: ' + result);
} catch (err) {
  console.error(`Failed to query isPanelShown. Code: ${err.code}, message: ${err.message}`);
}
```

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

取消订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## offImeHide

```TypeScript
offImeHide(callback?: Callback<Array<InputWindowInfo>>): void
```

取消订阅输入法Panel固定态软键盘隐藏事件。

**起始版本：** 23

**废弃版本：** -1

<!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-offImeHide(callback?: Callback<Array<InputWindowInfo>>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | 否 |

## offImeShow

```TypeScript
offImeShow(callback?: Callback<Array<InputWindowInfo>>):void
```

取消订阅输入法Panel固定态软键盘显示事件。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-offImeShow(callback?: Callback<Array<InputWindowInfo>>):void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | 否 |

## off_imeHide

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md#Panel)固定态软键盘隐藏事件。

**起始版本：** 10

**废弃版本：** -1

<!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeHide' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 否 |

## 示例

```TypeScript
inputMethod.getSetting().off('imeHide');
```

## off_imeShow

```TypeScript
off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void
```

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md#Panel)固定态软键盘显示事件。

**起始版本：** 10

**废弃版本：** -1

<!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeShow' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 否 |

## 示例

```TypeScript
inputMethod.getSetting().off('imeShow');
```

## onImeChangeWithUserId

```TypeScript
onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void
```

订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void--><!--Device-InputMethodSetting-onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImeChangeWithUserIdCallback](arkts-ime-inputmethod-imechangewithuseridcallback-t-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onImeHide

```TypeScript
onImeHide(callback: Callback<Array<InputWindowInfo>>): void
```

订阅输入法Panel固定态软键盘隐藏事件。

**起始版本：** 23

**废弃版本：** -1

<!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void--><!--Device-InputMethodSetting-onImeHide(callback: Callback<Array<InputWindowInfo>>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## onImeShow

```TypeScript
onImeShow(callback: Callback<Array<InputWindowInfo>>):void
```

订阅输入法Panel固定态软键盘显示事件。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void--><!--Device-InputMethodSetting-onImeShow(callback: Callback<Array<InputWindowInfo>>):void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on_imeHide

```TypeScript
on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void
```

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md#Panel)固定态软键盘隐藏事件。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeHide' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
inputMethod.getSetting().on('imeHide', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeHide event.');
});
```

## on_imeShow

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md#Panel)固定态软键盘显示事件。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

<!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void--><!--Device-InputMethodSetting-on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeShow' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
inputMethod.getSetting().on('imeShow', (info: Array<inputMethod.InputWindowInfo>) => {
  console.info('Succeeded in subscribing imeShow event.');
});
```
