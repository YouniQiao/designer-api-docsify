# WithEnv

## Modules to Import

```TypeScript
import { WithEnvAttribute, WithEnv } from 'kits/@kit.ArkUI';
```

## WithEnv

```TypeScript
export declare function WithEnv(
    content_?: CustomBuilder,
): WithEnvAttribute
```

WithEnv组件用于为子组件树设置局部环境变量作用域。开发者可以通过该组件为后代组件提供自定义环境变量，或设置系统环境变量。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WithEnv(    content_?: CustomBuilder,): WithEnvAttribute--><!--Device-unnamed-export declare function WithEnv(    content_?: CustomBuilder,): WithEnvAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 组件的内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WithEnvAttribute](arkts-arkui-arkui-withenv-withenvattribute-c.md) |  |

