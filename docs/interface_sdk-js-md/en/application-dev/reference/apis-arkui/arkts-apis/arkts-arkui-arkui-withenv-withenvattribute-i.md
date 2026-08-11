# WithEnvAttribute

Define the WithEnv attribute functions.

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

Notify WithEnv has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-applyAttributesFinish(): void--><!--Device-WithEnvAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## customEnv

```TypeScript
customEnv<T>(key: CustomEnvKey<T>,  value: T): this
```

Defining Custom Environment Variables

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): this--><!--Device-WithEnvAttribute-customEnv<T>(key: CustomEnvKey<T>,  value: T): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [CustomEnvKey](../arkts-components/arkts-arkui-customenvkey-c.md)&lt;T&gt; | Yes | Keys for custom environment variables. |
| value | T | Yes | Values of custom environment variables. |

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute object. |

## env

```TypeScript
env<T>(key: WritableSystemEnvKey<T>, value: T): this
```

Defining System Environment Variables

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): this--><!--Device-WithEnvAttribute-env<T>(key: WritableSystemEnvKey<T>, value: T): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | [WritableSystemEnvKey](../arkts-components/arkts-arkui-writablesystemenvkey-c.md)&lt;T&gt; | Yes | Keys for system environment variables. |
| value | T | Yes | Values of system environment variables. |

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute object. |

## setWithEnvOptions

```TypeScript
setWithEnvOptions(): this
```

Sets WithEnv options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WithEnvAttribute-setWithEnvOptions(): this--><!--Device-WithEnvAttribute-setWithEnvOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | WithEnvAttribute instance |

