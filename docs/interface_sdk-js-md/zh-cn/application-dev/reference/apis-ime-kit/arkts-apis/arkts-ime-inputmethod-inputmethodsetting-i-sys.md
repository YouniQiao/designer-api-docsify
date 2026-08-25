# InputMethodSetting

InputMethodSetting提供输入法配置与查询能力，面向前台应用提供以下功能：   
- 输入法变化订阅：通过 on('imeChange') 订阅输入法及子类型变化事件，当用户切换输入法时收到通知。   
- 输入法列表查询：通过 [getInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getinputmethods) 查询已激活/未激活输入法列表，通过 [getAllInputMethods](arkts-ime-inputmethod-inputmethodsetting-i.md#getallinputmethods) 查询所有已安装输入法列表，通过 [listInputMethodSubtype](arkts-ime-inputmethod-inputmethodsetting-i.md#listinputmethodsubtype) 查询指定输入法的子类型列表。   
- 面板可见性查询：通过isPanelShown查询输入法面板是否显示。   
- 输入法选择对话框：通过showOptionalInputMethods显示输入法选择对话框（已废弃，建议使用InputMethodListDialog）。   
 需通过[getSetting](arkts-ime-inputmethod-getsetting-f.md)获取InputMethodSetting实例后使用。 下列API均需使用[getSetting](arkts-ime-inputmethod-getsetting-f.md)获取到InputMethodSetting实例后，通过实例调用。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## enableInputMethod

```TypeScript
enableInputMethod(bundleName: string, extensionName: string, enabledState: EnabledState): Promise<void>
```

修改输入法的启用状态。使用promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-输入法未找到) |
| [12800019](../errorcode-inputmethod-framework.md#12800019-系统配置的默认输入法不支持此操作) |

## enableInputMethod

```TypeScript
enableInputMethod(
      bundleName: string, extensionName: string, enabledState: EnabledState, userId?: number): Promise<void>
```

修改指定用户输入法的启用状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800018](../errorcode-inputmethod-framework.md#12800018-输入法未找到) |
| [12800019](../errorcode-inputmethod-framework.md#12800019-系统配置的默认输入法不支持此操作) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(userId?: number): Array<InputMethodProperty>
```

获取指定用户的所有输入法应用列表。同步接口。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |

## getCursorInfo

```TypeScript
getCursorInfo(userId?: number): CursorInfo
```

获取指定用户的光标信息。当编辑框未给输入法服务通知光标信息时，返回所有属性值都为0。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |

## getDefaultInputMethodAbility

```TypeScript
getDefaultInputMethodAbility(): InputMethodProperty
```

获取默认输入法能力。为优化性能，返回的InputMethodProperty对象仅保证能够唯一标识输入法能力的`name`和`id`属性正确，其他属性可能为空。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean, userId?: number): Array<InputMethodProperty>
```

获取指定用户已激活/未激活的输入法应用列表。同步接口。   
> **说明：**
   
> 
   
> 已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。
   
> 
   
> 已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |

## getInputMethodSubtypes

```TypeScript
getInputMethodSubtypes(bundleName: string, userId?: number): Array<InputMethodSubtype>
```

获取指定用户指定输入法的子类型列表。同步接口。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo): boolean
```

查询指定类型的输入法面板是否处于显示状态。

**起始版本：** 11

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## isPanelShown

```TypeScript
isPanelShown(panelInfo: PanelInfo, displayId: number): boolean
```

查询指定类型的输入法面板在指定屏幕上是否处于显示状态。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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

## off('imeShow')

```TypeScript
off(type: 'imeShow', callback?: (info: Array<InputWindowInfo>) => void): void
```

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘显示事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeShow' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 否 |

## off('imeHide')

```TypeScript
off(type: 'imeHide', callback?: (info: Array<InputWindowInfo>) => void): void
```

取消订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘隐藏事件。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeHide' | 是 |
| callback | (info: Array&lt;[InputWindowInfo](arkts-ime-inputmethod-inputwindowinfo-i.md)&gt;) =&gt; void | 否 |

## offImeChangeWithUserId

```TypeScript
offImeChangeWithUserId(callback?: ImeChangeWithUserIdCallback): void
```

取消订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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

## on('imeShow')

```TypeScript
on(type: 'imeShow', callback: (info: Array<InputWindowInfo>) => void): void
```

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘显示事件。使用callback异步回调。 配对调用：   
- 调用on('imeShow')订阅事件后，必须在使用完毕时调用对应的off('imeShow')取消订阅。   
- 取消订阅时可以传入callback参数取消指定回调，或不传参数取消type对应的所有回调。   
- 不取消订阅可能导致回调事件持续触发和内存泄漏。

**起始版本：** 10

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

## on('imeHide')

```TypeScript
on(type: 'imeHide', callback: (info: Array<InputWindowInfo>) => void): void
```

订阅输入法[Panel](arkts-ime-inputmethodengine-panel-i.md)固定态软键盘隐藏事件。使用callback异步回调。 配对调用：   
- 调用on('imeHide')订阅事件后，必须在使用完毕时调用对应的off('imeHide')取消订阅。   
- 取消订阅时可以传入callback参数取消指定回调，或不传参数取消type对应的所有回调。   
- 不取消订阅可能导致回调事件持续触发和内存泄漏。

**起始版本：** 10

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

## onImeChangeWithUserId

```TypeScript
onImeChangeWithUserId(callback: ImeChangeWithUserIdCallback): void
```

订阅输入法及子类型变化监听事件，携带发生输入法变更的用户ID。使用callback异步回调。 配对调用：   
- 调用onImeChangeWithUserId订阅事件后，必须在使用完毕时调用offImeChangeWithUserId取消订阅。   
- 取消订阅时可以传入callback参数取消指定回调，或不传参数取消所有监听事件。   
- 不取消订阅可能导致回调事件持续触发和内存泄漏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

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
