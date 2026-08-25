# KeyboardController

下列API均需使用 on('inputStart') 获取到KeyboardController实例后，通过实例调用。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## exitCurrentInputType

```TypeScript
exitCurrentInputType(callback: AsyncCallback<void>): void
```

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用callback异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

## exitCurrentInputType

```TypeScript
exitCurrentInputType(): Promise<void>
```

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

隐藏输入法。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## hide

```TypeScript
hide(): Promise<void>
```

隐藏输入法。使用promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## hideKeyboard

```TypeScript
hideKeyboard(callback: AsyncCallback<void>): void
```

隐藏输入法。使用callback异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [hide](#hide)(callback: AsyncCallback&lt;void&gt;)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## hideKeyboard

```TypeScript
hideKeyboard(): Promise<void>
```

隐藏输入法。使用promise异步回调。   
> **说明：**
   
> 
   
> 从 API version 8开始支持，从API version 9开始废弃。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [hide](#hide)()

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
