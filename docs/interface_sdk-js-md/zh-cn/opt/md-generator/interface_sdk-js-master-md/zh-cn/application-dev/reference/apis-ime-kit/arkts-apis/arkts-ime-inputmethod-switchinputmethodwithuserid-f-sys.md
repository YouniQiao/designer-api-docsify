# switchInputMethodWithUserId（系统接口）

## switchInputMethodWithUserId

```TypeScript
function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: number): Promise<void>
```

切换输入法，使用promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONNECT_IME_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>--><!--Device-inputMethod-function switchInputMethodWithUserId(bundleName: string, subtypeId?: string, userId?: int): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| subtypeId | string | 否 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800005](../errorcode-inputmethod-framework.md#12800005-配置持久化失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.switchInputMethodWithUserId('com.example.keyboard', 'subtype_001', 100).then(() => {
  console.info('Succeeded in switching input method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to switchInputMethodWithUserId, code: ${err.code}, message: ${err.message}`);
});
```
