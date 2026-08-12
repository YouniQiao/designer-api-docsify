# KeyboardController

下列API均需使用  
[on('inputStart')](inputMethodEngine.InputMethodAbility.on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void))获取到KeyboardController实例后，通过实例调用。

**起始版本：** 8

<!--Device-inputMethodEngine-interface KeyboardController--><!--Device-inputMethodEngine-interface KeyboardController-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## exitCurrentInputType

```TypeScript
exitCurrentInputType(callback: AsyncCallback<void>): void
```

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用callback异步回调。

**起始版本：** 11

<!--Device-KeyboardController-exitCurrentInputType(callback: AsyncCallback<void>): void--><!--Device-KeyboardController-exitCurrentInputType(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType((err: BusinessError) => {
  if (err) {
    console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in exiting current input type.');
});
```

## exitCurrentInputType

```TypeScript
exitCurrentInputType(): Promise<void>
```

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用promise异步回调。

**起始版本：** 11

<!--Device-KeyboardController-exitCurrentInputType(): Promise<void>--><!--Device-KeyboardController-exitCurrentInputType(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800010-不是系统配置的默认输入法) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType().then(() => {
  console.info('Succeeded in exiting current input type.');
}).catch((err: BusinessError) => {
  console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
});
```

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

隐藏输入法。使用callback异步回调。

**起始版本：** 9

<!--Device-KeyboardController-hide(callback: AsyncCallback<void>): void--><!--Device-KeyboardController-hide(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

## hide

```TypeScript
hide(): Promise<void>
```

隐藏输入法。使用promise异步回调。

**起始版本：** 9

<!--Device-KeyboardController-hide(): Promise<void>--><!--Device-KeyboardController-hide(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800003-客户端应用异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
});
```

## hideKeyboard

```TypeScript
hideKeyboard(callback: AsyncCallback<void>): void
```

隐藏输入法。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [hide](inputMethodEngine.KeyboardController.hide(callback:)

<!--Device-KeyboardController-hideKeyboard(callback: AsyncCallback<void>): void--><!--Device-KeyboardController-hideKeyboard(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

## hideKeyboard

```TypeScript
hideKeyboard(): Promise<void>
```

隐藏输入法。使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [hide](#hide)()

<!--Device-KeyboardController-hideKeyboard(): Promise<void>--><!--Device-KeyboardController-hideKeyboard(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
});
```
