# openDisplaySettingsPage

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## openDisplaySettingsPage

```TypeScript
function openDisplaySettingsPage(context: Context): void
```

Open the display settings page.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-settings-function openDisplaySettingsPage(context: Context): void--><!--Device-settings-function openDisplaySettingsPage(context: Context): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Application context. Only UIAbilityContext and UIExtensionContext are supported. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16900020 | Failed to open the settings page via redirection. |
| 16900010 | Parameter error. |

## 示例

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  settings.openDisplaySettingsPage(context);
} catch (err) {
  console.error(`Failed to open the display settings page. code: ${err?.code}, message: ${err?.message}`);
}
```

