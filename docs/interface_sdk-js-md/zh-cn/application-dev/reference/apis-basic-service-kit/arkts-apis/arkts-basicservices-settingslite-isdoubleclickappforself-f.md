# isDoubleClickAppForSelf

## 导入模块

```TypeScript
import { settingsLite } from 'kits/@kit.BasicServicesKit';
```

## isDoubleClickAppForSelf

```TypeScript
function isDoubleClickAppForSelf(callback: ClickCallback): void
```

1. Checks whether the application started by double-pressing the function key is the application itself.2. This API is triggered to check whether double-pressing the function key starts the application itself.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-settingsLite-function isDoubleClickAppForSelf(callback: ClickCallback): void--><!--Device-settingsLite-function isDoubleClickAppForSelf(callback: ClickCallback): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClickCallback](arkts-basicservices-settingslite-clickcallback-i.md) | 是 | Callback used to return the execution result. |

