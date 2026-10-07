# setAlternateModuleEnabled（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## setAlternateModuleEnabled

```TypeScript
function setAlternateModuleEnabled(bundleName: string, moduleName: string, isEnabled: boolean): Promise<void>
```

启用或禁用备用模块。

**起始版本：** 26.2.0

**需要权限：** ohos.permission.INSTALL_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function setAlternateModuleEnabled(bundleName: string, moduleName: string, isEnabled: boolean): Promise<void>--><!--Device-bundleManager-function setAlternateModuleEnabled(bundleName: string, moduleName: string, isEnabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | Bundle name. |
| moduleName | string | 是 | 模块名称。 |
| isEnabled | boolean | 是 | 是否启用备份模块。**true**表示启用，**false**否则。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 不返回任何值的Promise。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission denied, non-system app called system api. |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) | The specified bundleName is not found. |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) | The specified moduleName is not existed. |
