# switchInputMethod

## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void
```

切换输入法，使用callback异步回调。

**含义/功能**：将当前输入法切换为指定的目标输入法。

**使用场景：**当前输入法应用需要切换到另一个输入法时使用（如用户在输入法设置中选择了新的输入法）。

**使用后效果**：成功时系统将当前输入法切换为目标输入法，目标输入法成为新的当前输入法；失败时当前输入法不变。

**异步返回方式**：使用callback异步回调。成功时err为undefined，data为true；失败时返回BusinessError对象。

**起始版本：** 9

**需要权限：** 
- API版本9 - 10：ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void--><!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12800005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
});
```


## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty): Promise<boolean>
```

切换输入法，使用promise异步回调。

**含义/功能**：将当前输入法切换为指定的目标输入法。

**使用场景：**当前输入法应用需要切换到另一个输入法时使用。

**使用后效果**：成功时系统将当前输入法切换为目标输入法；失败时当前输入法不变。

**异步返回方式**：使用Promise异步回调。成功时返回true，失败时返回BusinessError对象。

**起始版本：** 9

**需要权限：** 
- API版本9 - 10：ohos.permission.CONNECT_IME_ABILITY

<!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty): Promise<boolean>--><!--Device-inputMethod-function switchInputMethod(target: InputMethodProperty): Promise<boolean>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [12800005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
});
```
