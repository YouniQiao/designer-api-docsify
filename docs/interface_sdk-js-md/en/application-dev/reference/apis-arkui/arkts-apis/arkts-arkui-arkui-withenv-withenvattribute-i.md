# WithEnvAttribute

定义WithEnv组件的属性功能。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface WithEnvAttribute--><!--Device-unnamed-export declare interface WithEnvAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { WithEnvAttribute, WithEnv } from 'kits/@kit.ArkUI';
```

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知WithEnv属性设置完成。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-applyAttributesFinish(): void--><!--Device-WithEnvAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## customEnv

```TypeScript
customEnv<T>(key: CustomEnvKey<T>,  value: T): this
```

设置作用域内可被后代自定义组件读取的自定义环境变量。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): this--><!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [CustomEnvKey](../arkts-components/arkts-arkui-customenvkey-c.md)&lt;T&gt; | Yes | 自定义环境变量的键。 |
| value | T | Yes | 自定义环境变量的值。value的类型T对应CustomEnvKey&lt;T&gt;的类型T。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute对象。 |

## env

```TypeScript
env<T>(key: WritableSystemEnvKey<T>, value: T): this
```

设置作用域内的系统环境变量。当前正式支持的系统环境变量键为WritableEnvKey.FONT_SCALE、WritableEnvKey.DIRECTION。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): this--><!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [WritableSystemEnvKey](../arkts-components/arkts-arkui-writablesystemenvkey-c.md)&lt;T&gt; | Yes | 系统环境变量键。当前正式支持WritableEnvKey.FONT_SCALE和WritableEnvKey.DIRECTION。 |
| value | T | Yes | 系统环境变量值。value的类型T对应WritableSystemEnvKey&lt;T&gt;中的类型T。当key为WritableEnvKey.FONT_SCALE时，value类型为number；当key为WritableEnvKey.DIRECTION时，value类型为Direction。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute对象。 |

## setWithEnvOptions

```TypeScript
setWithEnvOptions(): this
```

设置WithEnv选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-setWithEnvOptions(): this--><!--Device-WithEnvAttribute-setWithEnvOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute实例。 |

