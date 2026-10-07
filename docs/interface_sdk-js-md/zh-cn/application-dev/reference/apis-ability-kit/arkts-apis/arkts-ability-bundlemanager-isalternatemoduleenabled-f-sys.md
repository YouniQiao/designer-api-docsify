# isAlternateModuleEnabled（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## isAlternateModuleEnabled

```TypeScript
function isAlternateModuleEnabled(bundleName: string, moduleName: string): Promise<boolean>
```

查询备用模块使能状态。

**起始版本：** 26.2.0

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function isAlternateModuleEnabled(bundleName: string, moduleName: string): Promise<boolean>--><!--Device-bundleManager-function isAlternateModuleEnabled(bundleName: string, moduleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | Bundle name. |
| moduleName | string | 是 | 模块名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise用于返回结果。**true**表示开启，**false**表示关闭。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission denied. |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission denied, non-system app called system api. |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) | The specified bundleName is not found. |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) | The specified moduleName is not existed. |
