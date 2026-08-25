# setHyperSnapEnabled

## 导入模块

```TypeScript
import { hyperSnapManager } from '@kit.AbilityKit';
```

## setHyperSnapEnabled

```TypeScript
function setHyperSnapEnabled(enableFlag: boolean): void
```

启用或禁用应用的快启功能。

> **说明：**&gt;
> - 当通过本接口启用应用快启功能时，系统最终会根据应用兼容性、资源可用性和系统策略来决定是否创建或使用快启。当通过本接口禁用快启功能时，可以保证系统不会创建快启。&gt;
> - 设置的值会在重启后保持。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [enableFlag](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hitracechain-enableflag-f.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000150](../errorcode-ability.md#16000150-发送请求失败) |
