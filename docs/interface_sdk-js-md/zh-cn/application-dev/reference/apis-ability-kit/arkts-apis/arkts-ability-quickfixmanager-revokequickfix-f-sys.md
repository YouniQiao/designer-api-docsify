# revokeQuickFix（系统接口）

## 导入模块

```TypeScript
import { quickFixManager } from 'kits/@kit.AbilityKit';
```

## revokeQuickFix

```TypeScript
function revokeQuickFix(bundleName: string, callback: AsyncCallback<void>): void
```

撤销快速修复的接口，使用callback方式返回结果。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [18500001](../errorcode-ability.md#18500001-指定的包名无效) |
| [18500009](../errorcode-ability.md#18500009-该应用当前有正在处理的快速修复任务) |


## revokeQuickFix

```TypeScript
function revokeQuickFix(bundleName: string): Promise<void>
```

撤销快速修复的接口。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INSTALL_BUNDLE

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

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
| [18500001](../errorcode-ability.md#18500001-指定的包名无效) |
| [18500009](../errorcode-ability.md#18500009-该应用当前有正在处理的快速修复任务) |
