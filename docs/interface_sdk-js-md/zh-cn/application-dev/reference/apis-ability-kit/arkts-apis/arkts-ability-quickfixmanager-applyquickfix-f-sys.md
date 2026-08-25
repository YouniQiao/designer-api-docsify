# applyQuickFix（系统接口）

## 导入模块

```TypeScript
import { quickFixManager } from 'kits/@kit.AbilityKit';
```

## applyQuickFix

```TypeScript
function applyQuickFix(hapModuleQuickFixFiles: Array<string>, callback: AsyncCallback<void>): void
```

快速修复的补丁安装接口。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapModuleQuickFixFiles | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18500002](../errorcode-ability.md#18500002-指定的补丁包无效) |
| [18500008](../errorcode-ability.md#18500008-快速修复内部错误) |


## applyQuickFix

```TypeScript
function applyQuickFix(hapModuleQuickFixFiles: Array<string>): Promise<void>
```

快速修复的补丁安装接口。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapModuleQuickFixFiles | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18500002](../errorcode-ability.md#18500002-指定的补丁包无效) |
| [18500008](../errorcode-ability.md#18500008-快速修复内部错误) |
