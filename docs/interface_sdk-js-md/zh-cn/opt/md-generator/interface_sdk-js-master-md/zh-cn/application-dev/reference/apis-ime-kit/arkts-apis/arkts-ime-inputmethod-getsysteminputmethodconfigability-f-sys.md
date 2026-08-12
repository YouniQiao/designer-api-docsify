# getSystemInputMethodConfigAbility（系统接口）

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(userId?: number): ElementName
```

获取指定用户的系统输入法设置界面Ability信息。用于启动系统输入法配置界面。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName--><!--Device-inputMethod-function getSystemInputMethodConfigAbility(userId?: int): ElementName-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [12800023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [12800025](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
| [12800008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800024](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ime-kit/errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';

try {
  let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility(100);
  console.info('Succeeded in getting system input method config ability, bundleName: ' + inputMethodConfig.bundleName);
} catch (err) {
  console.error(`Failed to getSystemInputMethodConfigAbility. Code: ${err.code}, message: ${err.message}`);
}
```
