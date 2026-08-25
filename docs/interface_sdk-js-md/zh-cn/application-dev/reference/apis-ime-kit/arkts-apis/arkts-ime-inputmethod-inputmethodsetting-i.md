# InputMethodSetting

InputMethodSetting提供输入法配置与查询能力，面向前台应用提供以下功能：   
- 输入法变化订阅：通过 on('imeChange') 订阅输入法及子类型变化事件，当用户切换输入法时收到通知。   
- 输入法列表查询：通过 [getInputMethods](#getinputmethods) 查询已激活/未激活输入法列表，通过 [getAllInputMethods](#getallinputmethods) 查询所有已安装输入法列表，通过 [listInputMethodSubtype](#listinputmethodsubtype) 查询指定输入法的子类型列表。   
- 面板可见性查询：通过isPanelShown查询输入法面板是否显示。   
- 输入法选择对话框：通过showOptionalInputMethods显示输入法选择对话框（已废弃，建议使用InputMethodListDialog）。   
 需通过[getSetting](arkts-ime-inputmethod-getsetting-f.md)获取InputMethodSetting实例后使用。 下列API均需使用[getSetting](arkts-ime-inputmethod-getsetting-f.md)获取到InputMethodSetting实例后，通过实例调用。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(callback: AsyncCallback<void>): void
```

显示输入法选择对话框。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(): Promise<void>
```

显示输入法选择对话框。使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## getAllInputMethods

```TypeScript
getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

获取所有输入法应用列表。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getAllInputMethods

```TypeScript
getAllInputMethods(): Promise<Array<InputMethodProperty>>
```

获取所有输入法应用列表。使用promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(): Array<InputMethodProperty>
```

获取所有输入法应用列表。同步接口。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getInputMethods

```TypeScript
getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void
```

获取已激活/未激活的输入法应用列表。使用callback异步回调。   
> **说明：**
   
> 
   
> 已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。
   
> 
   
> 已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getInputMethods

```TypeScript
getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>
```

获取已激活/未激活的输入法应用列表。使用promise异步回调。   
> **说明：**
   
> 
   
> 已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。
   
> 
   
> 已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean): Array<InputMethodProperty>
```

获取已激活/未激活的输入法应用列表。同步接口。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。
   
> 
   
> 已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。
   
> 
   
> 已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## getInputMethodState

```TypeScript
getInputMethodState(): Promise<EnabledState>
```

查询输入法的启用状态。使用promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EnabledState](arkts-ime-inputmethod-enabledstate-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800004](../errorcode-inputmethod-framework.md#12800004-不是输入法应用) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void
```

查询当前输入法应用的所有子类型。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>
```

查询当前输入法应用的所有子类型。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## listInputMethod

```TypeScript
listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

查询已安装的输入法列表。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getInputMethods](#getinputmethods)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | 是 |

## listInputMethod

```TypeScript
listInputMethod(): Promise<Array<InputMethodProperty>>
```

查询已安装的输入法列表。使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getInputMethods](#getinputmethods)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(
      inputMethodProperty: InputMethodProperty,
      callback: AsyncCallback<Array<InputMethodSubtype>>
    ): void
```

获取指定输入法应用的所有子类型。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>
```

获取指定输入法应用的所有子类型。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-包管理服务异常) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## off('imeChange')

```TypeScript
off(
      type: 'imeChange',
      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

取消订阅输入法及子类型变化监听事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeChange' | 是 |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | 否 |

## on('imeChange')

```TypeScript
on(
      type: 'imeChange',
      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

订阅输入法及子类型变化监听事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imeChange' | 是 |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | 是 |

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(callback: AsyncCallback<boolean>): void
```

显示输入法选择对话框。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(): Promise<boolean>
```

显示输入法选择对话框。使用promise异步回调。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
