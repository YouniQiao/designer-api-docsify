# switchInputMethod

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void
```

切换输入法，使用callback异步回调。 含义/功能：将当前输入法切换为指定的目标输入法。 使用场景：当前输入法应用需要切换到另一个输入法时使用（如用户在输入法设置中选择了新的输入法）。 使用后效果：成功时系统将当前输入法切换为目标输入法，目标输入法成为新的当前输入法；失败时当前输入法不变。

**起始版本：** 9

**需要权限：** 
- API版本9 - 10：ohos.permission.CONNECT_IME_ABILITY

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |


## switchInputMethod

```TypeScript
function switchInputMethod(target: InputMethodProperty): Promise<boolean>
```

切换输入法，使用promise异步回调。 含义/功能：将当前输入法切换为指定的目标输入法。 使用场景：当前输入法应用需要切换到另一个输入法时使用。 使用后效果：成功时系统将当前输入法切换为目标输入法；失败时当前输入法不变。

**起始版本：** 9

**需要权限：** 
- API版本9 - 10：ohos.permission.CONNECT_IME_ABILITY

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
