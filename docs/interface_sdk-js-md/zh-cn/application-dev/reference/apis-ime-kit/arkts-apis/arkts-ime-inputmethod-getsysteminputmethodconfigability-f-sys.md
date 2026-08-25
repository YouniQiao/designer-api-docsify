# getSystemInputMethodConfigAbility（系统接口）

## 导入模块

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## getSystemInputMethodConfigAbility

```TypeScript
function getSystemInputMethodConfigAbility(userId?: number): ElementName
```

获取指定用户的系统输入法设置界面Ability信息。用于启动系统输入法配置界面。

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
| [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-输入法管理服务异常) |
| [12800023](../errorcode-inputmethod-framework.md#12800023-指定的用户不存在) |
| [12800024](../errorcode-inputmethod-framework.md#12800024-指定的用户未在前台) |
| [12800025](../errorcode-inputmethod-framework.md#12800025-跨用户操作被拒绝) |
